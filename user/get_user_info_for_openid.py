#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.user.ttypes import UserInfoResponse, UserInfo
from db.db import User
from util import utils
from peewee import DoesNotExist


class GetUserInfoForOpenidHandler(object):
    def __init__(self, req):
        self.openid = req.openid

    def mk_response(self, user):
        return UserInfoResponse(
            user=user
        )

    def execute(self):

        try:
            user = User.get(openid=self.openid)
        except DoesNotExist:
            user = User(
                openid=self.openid,
            )
            user.save()
            return self.mk_response(UserInfo(
                user_id=user.id
            ))
        except:
            return self.mk_response(None)

        user_info = UserInfo(
            user_id=user.id,
            openid=user.openid,
            nickname=user.nickname,
            head_img_url=user.head_img_url,
            create_time=utils.datetime2timestamp(user.create_time)
        )

        return self.mk_response(user_info)
