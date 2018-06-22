#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import BaseResponse
from db.db import Relation


class UnFollowingHandler(object):
    def __init__(self, req):
        self.from_user_id = req.from_user_id
        self.to_user_id = req.to_user_id

    def mk_response(self, success=True, msg=None):
        return BaseResponse(
            success=success,
            msg=msg
        )

    def execute(self):

        try:
            Relation.delete().where(
                Relation.from_user_id == self.from_user_id,
                Relation.to_user_id == self.to_user_id,
            ).execute()
        except Exception, e:
            return self.mk_response(False, str(e))

        return self.mk_response()
