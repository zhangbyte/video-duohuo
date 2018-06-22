#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.item.ttypes import BaseResponse
from db.db import Item


class AddItemHandler(object):

    def __init__(self, req):
        self.user_id = req.item.user_id
        self.video = req.item.video
        self.text = req.item.text

    def mk_response(self, success=True, msg=None):
        return BaseResponse(
            success=success,
            msg=msg
        )

    def execute(self):

        try:
            Item(
                user_id=self.user_id,
                video=self.video,
                text=self.text
            ).save()
        except Exception, e:
            return self.mk_response(False, str(e))

        return self.mk_response()
