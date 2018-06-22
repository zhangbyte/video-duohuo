#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.user.ttypes import BaseResponse
from db.db import User


class UpdateUserInfoHandler(object):

    def __init__(self, req):
        self.user_id = req.user.user_id
        self.nickname = req.user.nickname
        self.head_img_url = req.user.head_img_url

    def mk_response(self, success=True, msg=None):
        return BaseResponse(
            success=success,
            msg=msg
        )

    def execute(self):

        try:
            user = User.get(id=self.user_id)
            user.nickname = self.nickname if self.nickname else user.nickname
            user.head_img_url = self.head_img_url if self.head_img_url else user.head_img_url
            user.save()
        except Exception, e:
            return self.mk_response(False, str(e))

        return self.mk_response()
