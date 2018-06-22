#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import LoveCountResponse
from db.db import Love
from peewee import fn


class GetLoveCountHandler(object):
    def __init__(self, req):
        self.item_ids = req.item_ids

    def mk_response(self, counts):
        return LoveCountResponse(
            counts=counts
        )

    def execute(self):
        counts = []
        for item_id in self.item_ids:
            count = Love.select(fn.COUNT(Love.id)).where(
                Love.item_id == item_id
            ).scalar()
            counts.append(count)

        return self.mk_response(counts)
