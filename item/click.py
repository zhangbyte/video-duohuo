#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.item.ttypes import BaseResponse
from db.db import Item


class ClickHandler(object):

    def __init__(self, req):
        self.item_id = req.item_id

    def mk_response(self, success=True, msg=None):
        return BaseResponse(
            success=success,
            msg=msg
        )

    def execute(self):

        try:
            Item.update(click=Item.click + 1).where(
                Item.id == self.item_id
            ).execute()
        except Exception, e:
            return self.mk_response(False, str(e))

        return self.mk_response()
