#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.user.ttypes import UserInfoListResponse, UserInfo
from db.db import User
from util import utils


class GetUserInfoListHandler(object):

    def __init__(self, req):
        self.ids = req.ids

    def mk_response(self, user_info_list):
        return UserInfoListResponse(
            user_info_list=user_info_list
        )

    def execute(self):

        try:
            users = User.select().where(
                User.id.in_(self.ids)
            )
        except:
            pass

        user_info_list = []
        for user in users:
            user_info_list.append(UserInfo(
                user_id=user.id,
                openid=user.openid,
                nickname=user.nickname,
                head_img_url=user.head_img_url,
                create_time=utils.datetime2timestamp(user.create_time)
            ))

        return self.mk_response(user_info_list)
