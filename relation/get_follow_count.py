#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.relation.ttypes import FollowCountResponse
from db.db import Relation
from util.const import FOLLOWING_COUNT, FOLLOWER_COUNT
from peewee import fn


class GetFollowCountHandler(object):
    def __init__(self, req):
        self.user_id = req.user_id
        self.type = req.type

    def mk_response(self, count=0):
        return FollowCountResponse(
            count=count
        )

    def execute(self):
        if self.type == FOLLOWING_COUNT:
            count = Relation.select(fn.COUNT(Relation.id)).where(
                Relation.from_user_id == self.user_id
            ).scalar()
        elif self.type == FOLLOWER_COUNT:
            count = Relation.select(fn.COUNT(Relation.id)).where(
                Relation.to_user_id == self.user_id
            ).scalar()
        else:
            count = 0

        return self.mk_response(count)
