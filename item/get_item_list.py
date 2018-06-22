#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.item.ttypes import GetItemListResponse
from gen.item.ttypes import Item as ThriftItem
from db.db import Item
from util import const, utils


class GetItemListHandler(object):

    def __init__(self, req):
        self.type = req.type
        self.offset = req.offset
        self.count = req.count
        self.user_id = req.user_id

    def mk_response(self, item_list):
        return GetItemListResponse(
            item_list=item_list
        )

    def execute(self):

        if self.user_id != 0:
            items = Item.select().where(
                Item.user_id == self.user_id
            ).order_by(Item.create_time.desc()).limit(self.count).offset(self.offset)
        else:
            order_type = Item.create_time.desc() if self.type == const.SORT_TYPE_TIME else Item.click.desc()
            items = Item.select().order_by(order_type).limit(self.count).offset(self.offset)

        item_list = []
        for item in items:
            item_list.append(ThriftItem(
                item_id=item.id,
                user_id=item.user_id,
                video=item.video,
                text=item.text,
                click=item.click,
                create_time=utils.datetime2timestamp(item.create_time)
            ))

        return self.mk_response(item_list)
