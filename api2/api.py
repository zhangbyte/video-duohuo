#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from util import oss, utils, ffmpeg, const
import urllib2
import json
import os
from rpc import item_service, user_service, comment_service, relation_service

app = Flask(__name__)


def success_response(data=None):
    return json.dumps({
        'error': False,
        'msg': None,
        'data': data
    })


def error_response(msg=None):
    return json.dumps({
        'error': True,
        'msg': msg,
        'data': None
    })


@app.route('/')
def hello_world():
    return 'api 2; 127.0.0.1:5001'


def get_user_info_dict_for_ids(ids):
    user_info_list = user_service.get_user_info_list(ids)
    user_info_dict = {}
    for user_info in user_info_list:
        user_info_dict[user_info.user_id] = user_info

    return user_info_dict


# 登录
@app.route('/login', methods=['POST'])
def login():
    code = request.form.get('code', None)
    if not code:
        return error_response('Error code!')

    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
        APPID='wx9122b10baa3794ac', SECRET='d7ef2c84e18550e80cf97274edf150d9', JSCODE=code
    )
    res = urllib2.urlopen(url).read()
    user_info = json.loads(res)

    if user_info.get('errcode', None):
        return error_response(user_info.get('errmsg', 'Error code!'))

    user = user_service.get_user_info_for_openid(user_info['openid'])
    if user:
        return success_response({
            'user_id': user.user_id,
            'nickname': user.nickname,
            'head_img_url': user.head_img_url
        })

    return success_response(None)


# 更新用户信息
@app.route('/user', methods=['POST'])
def user_update():
    user_id = request.form['user_id']
    nickname = request.form['nickname']
    head_img_url = request.form['head_img_url']

    res = user_service.update_user_info(user_id, nickname, head_img_url)
    if res.success:
        return success_response()
    else:
        return error_response(res.msg)


# 上传短视频
@app.route('/item/upload', methods=['POST'])
def item_upload():
    user_id = request.form['user_id']
    video = request.files['video']
    text = request.form['text']

    ffmpeg.get_screenshot(video)

    random_str = utils.random_str()
    suffix = video.filename.rsplit('.', 1)[1]
    oss.upload_img(open(ffmpeg.get_tmp_img_path(video.filename), 'rb'), random_str)
    oss.upload_video(open(ffmpeg.get_tmp_video_path(video.filename), 'rb'), random_str, suffix)

    os.remove(ffmpeg.get_tmp_img_path(video.filename))
    os.remove(ffmpeg.get_tmp_video_path(video.filename))

    item_service.add_item(user_id, '{0}.{1}'.format(random_str, suffix), text)

    return success_response()


# 短视频列表
@app.route('/item/list', methods=['GET'])
def item_list():
    user_id = int(request.args['user_id'])
    type = int(request.args.get('type', 1))
    offset = int(request.args.get('offset', 0))
    count = int(request.args.get('count', 10))

    # 获取短视频信息
    items = item_service.get_item_list(type=type, offset=offset, count=count)

    # 获取用户身份信息
    ids = [item.user_id for item in items]
    user_info_dict = get_user_info_dict_for_ids(ids)

    item_ids = [item.item_id for item in items]
    # 获取点赞关系（非核心）
    try:
        status = relation_service.get_love_status(user_id, item_ids)
    except:
        status = [False for item in items]

    # 获取点赞数（非核心）
    try:
        counts = relation_service.get_love_count(item_ids)
    except:
        counts = [0 for item in items]

    item_list = []
    for i, item in enumerate(items):
        item_list.append({
            'item_id': item.item_id,
            'user_id': item.user_id,
            'nickname': user_info_dict[item.user_id].nickname,
            'head_img_url': user_info_dict[item.user_id].head_img_url,
            'img': oss.get_img_url(item.video),
            'video': oss.get_video_url(item.video),
            'text': item.text,
            'click': item.click,
            'create_time': item.create_time,

            'love_status': status[i],
            'love_count': counts[i],
        })

    return success_response(item_list)


# 短视频详情
@app.route('/item', methods=['GET'])
def item_one():
    user_id = int(request.args['user_id'])
    item_id = int(request.args['item_id'])

    item = item_service.get_item_by_id(item_id)
    user_info = user_service.get_user_info(item.user_id)

    # 获取关注关系（非核心）
    try:
        follow_status = relation_service.get_follow_status(user_id, [item.user_id])[0]
    except:
        follow_status = False

    # 获取点赞关系（非核心）
    try:
        status = relation_service.get_love_status(user_id, [item.item_id])[0]
    except:
        status = False

    # 获取点赞数（非核心）
    try:
        love_count = relation_service.get_love_count([item.item_id])[0]
    except:
        love_count = 0

    item_info = {
        'item_id': item.item_id,
        'user_id': item.user_id,
        'nickname': user_info.nickname,
        'head_img_url': user_info.head_img_url,
        'img': oss.get_img_url(item.video),
        'video': oss.get_video_url(item.video),
        'text': item.text,
        'click': item.click,
        'create_time': item.create_time,

        'love_status': status,
        'love_count': love_count,
        'follow_status': follow_status,
    }

    return success_response(item_info)


# 个人信息(关注、粉丝数、关注关系)
@app.route('/user/info', methods=['GET'])
def user_info():
    user_id = int(request.args['user_id'])
    to_user_id = int(request.args['to_user_id'])

    following_count = relation_service.get_follow_count(to_user_id, const.FOLLOWING_COUNT)
    follower_count = relation_service.get_follow_count(to_user_id, const.FOLLOWER_COUNT)

    # 获取关注关系（非核心）
    try:
        if user_id == to_user_id:
            follow_status = False
        else:
            follow_status = relation_service.get_follow_status(user_id, [to_user_id])[0]
    except:
        follow_status = False

    return success_response({
        'following_count': following_count,
        'follower_count': follower_count,

        'follow_status': follow_status,
    })


# 个人页视频列表
@app.route('/item/list/user', methods=['GET'])
def item_list_for_user():
    user_id = int(request.args['user_id'])
    offset = request.args.get('offset', 0)
    count = request.args.get('count', 10)

    items = item_service.get_item_list(offset=offset, count=count, user_id=user_id)

    item_list = []
    for i, item in enumerate(items):
        item_list.append({
            'item_id': item.item_id,
            'user_id': item.user_id,
            'img': oss.get_img_url(item.video),
            'video': oss.get_video_url(item.video),
            'text': item.text,
            'click': item.click,
            'create_time': item.create_time
        })

    return success_response(item_list)


# 删除短视频
@app.route('/item/delete', methods=['POST'])
def item_delete():
    item_id = int(request.form['item_id'])

    item_service.delete_item(item_id)
    return success_response()


# 点击数更新
@app.route('/item/click', methods=['POST'])
def item_click():
    item_id = int(request.form['item_id'])

    item_service.click_item(item_id)
    return success_response()


# 添加评论
@app.route('/comment/add', methods=['POST'])
def comment_add():
    user_id = int(request.form['user_id'])
    item_id = int(request.form['item_id'])
    text = request.form['text']

    comment_service.add_comment(item_id, user_id, text)
    return success_response()


# 评论列表
@app.route('/comment/list', methods=['GET'])
def comment_list():
    item_id = int(request.args['item_id'])
    offset = int(request.args.get('offset', 0))
    count = int(request.args.get('count', 10))

    comments = comment_service.get_comment_list(item_id, offset, count)

    ids = [comment.user_id for comment in comments]

    user_info_dict = get_user_info_dict_for_ids(ids)

    comment_list = []
    for comment in comments:
        comment_list.append({
            "comment_id": comment.comment_id,
            "user_id": comment.user_id,
            'nickname': user_info_dict[comment.user_id].nickname,
            'head_img_url': user_info_dict[comment.user_id].head_img_url,
            "text": comment.text,
            "create_time": comment.create_time
        })

    return success_response(comment_list)


# 关注
@app.route('/relation/following', methods=['POST'])
def following():
    user_id = int(request.form['user_id'])
    to_user_id = int(request.form['to_user_id'])

    relation_service.following(user_id, to_user_id)
    return success_response()


# 取消关注
@app.route('/relation/un_following', methods=['POST'])
def un_following():
    user_id = int(request.form['user_id'])
    to_user_id = int(request.form['to_user_id'])

    relation_service.un_following(user_id, to_user_id)
    return success_response()


# 点赞
@app.route('/relation/love', methods=['POST'])
def love():
    user_id = int(request.form['user_id'])
    item_id = int(request.form['item_id'])

    relation_service.love(user_id, item_id)
    return success_response()


# 取消点赞
@app.route('/relation/un_love', methods=['POST'])
def un_love():
    user_id = int(request.form['user_id'])
    item_id = int(request.form['item_id'])

    relation_service.un_love(user_id, item_id)
    return success_response()


# 关注列表
@app.route('/relation/following/list', methods=['GET'])
def following_list():
    user_id = int(request.args['user_id'])
    offset = int(request.args.get('offset', 0))
    count = int(request.args.get('count', 10))

    ids = relation_service.get_following_list(user_id, offset, count)
    user_info_dict = get_user_info_dict_for_ids(ids)

    following_list = []
    for id in ids:
        following_list.append({
            "user_id": id,
            'nickname': user_info_dict[id].nickname,
            'head_img_url': user_info_dict[id].head_img_url,
        })

    return success_response(following_list)


# 粉丝列表
@app.route('/relation/follower/list', methods=['GET'])
def follower_list():
    user_id = int(request.args['user_id'])
    offset = int(request.args.get('offset', 0))
    count = int(request.args.get('count', 10))

    ids = relation_service.get_follower_list(user_id, offset, count)
    user_info_dict = get_user_info_dict_for_ids(ids)

    follower_list = []
    for id in ids:
        follower_list.append({
            "user_id": id,
            'nickname': user_info_dict[id].nickname,
            'head_img_url': user_info_dict[id].head_img_url,
        })

    return success_response(follower_list)


if __name__ == '__main__':
    app.run(port=5001)
