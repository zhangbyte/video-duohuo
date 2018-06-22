#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import StatusResponse
from db.db import Relation


class GetFollowStatusHandler(object):
    def __init__(self, req):
        self.from_user_id = req.from_user_id
        self.to_user_ids = req.to_user_ids

    def mk_response(self, status):
        return StatusResponse(
            status=status
        )

    def execute(self):
        items = Relation.select(Relation.to_user_id).where(
            Relation.from_user_id == self.from_user_id,
            Relation.to_user_id.in_(self.to_user_ids),
        )
        relation_dict = {}
        for item in items:
            relation_dict[item.to_user_id] = True

        status = [relation_dict.get(to_user_id, False) for to_user_id in self.to_user_ids]

        return self.mk_response(status)
