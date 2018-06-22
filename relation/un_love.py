#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import BaseResponse
from db.db import Love


class UnLoveHandler(object):
    def __init__(self, req):
        self.user_id = req.user_id
        self.item_id = req.item_id

    def mk_response(self, success=True, msg=None):
        return BaseResponse(
            success=success,
            msg=msg
        )

    def execute(self):

        try:
            Love.delete().where(
                Love.from_user_id == self.user_id,
                Love.item_id == self.item_id,
            ).execute()
        except Exception, e:
            return self.mk_response(False, str(e))

        return self.mk_response()
