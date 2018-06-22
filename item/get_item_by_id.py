#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gen.item.ttypes import GetItemByIdResponse
from gen.item.ttypes import Item as ThriftItem
from db.db import Item
from util import utils


class GetItemByIdHandler(object):
    def __init__(self, req):
        self.item_id = req.item_id

    def mk_response(self, item):
        return GetItemByIdResponse(
            item=item
        )

    def execute(self):
        item = Item.get(
            Item.id == self.item_id
        )

        item = ThriftItem(
            item_id=item.id,
            user_id=item.user_id,
            video=item.video,
            text=item.text,
            click=item.click,
            create_time=utils.datetime2timestamp(item.create_time)
        )

        return self.mk_response(item)
