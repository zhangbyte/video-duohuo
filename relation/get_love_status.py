#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import StatusResponse
from db.db import Love


class GetLoveStatusHandler(object):
    def __init__(self, req):
        self.user_id = req.user_id
        self.item_ids = req.item_ids

    def mk_response(self, status):
        return StatusResponse(
            status=status
        )

    def execute(self):
        items = Love.select(Love.item_id).where(
            Love.from_user_id == self.user_id,
            Love.item_id.in_(self.item_ids),
        )
        relation_dict = {}
        for item in items:
            relation_dict[item.item_id] = True

        status = [relation_dict.get(item_id, False) for item_id in self.item_ids]

        return self.mk_response(status)
