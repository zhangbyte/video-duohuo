#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import FollowListResponse
from db.db import Relation


class GetFollowingListHandler(object):
    def __init__(self, req):
        self.user_id = req.user_id
        self.offset = req.offset
        self.count = req.count

    def mk_response(self, ids):
        return FollowListResponse(
            ids=ids
        )

    def execute(self):
        items = Relation.select(Relation.to_user_id).where(
            Relation.from_user_id == self.user_id
        ).order_by(Relation.create_time.desc()).limit(self.count).offset(self.offset)

        ids = []
        for item in items:
            ids.append(item.to_user_id)

        return self.mk_response(ids)
