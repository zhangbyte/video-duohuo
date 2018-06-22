#! /usr/bin/env python
# -*- coding: utf-8 -*-

import oss2

auth = oss2.Auth('LTAIIhM0E6hdpIIe', 'jPuPJMLKAL5bJoseM6JpByqpq4C9qx')

# service = oss2.Service(auth, 'oss-cn-shenzhen-internal.aliyuncs.com')
# print([b.name for b in oss2.BucketIterator(service)])

bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'video-duohuo')

VIDEO_URL = 'https://video-duohuo.oss-cn-shenzhen.aliyuncs.com/videos/{0}'
IMG_URL = 'https://video-duohuo.oss-cn-shenzhen.aliyuncs.com/imgs/{0}.jpg'


def upload_video(video, random_str, suffix):
    bucket.put_object('videos/{0}'.format(random_str + '.' + suffix), video)


def upload_img(img, random_str):
    bucket.put_object('imgs/{0}'.format(random_str + '.jpg'), img)


def get(video_name):
    return bucket.sign_url('GET', 'videos/{0}'.format(video_name), 60)


def get_video_url(video_name):
    return VIDEO_URL.format(video_name)


def get_img_url(video_name):
    return IMG_URL.format(video_name.rsplit('.', 1)[0])
