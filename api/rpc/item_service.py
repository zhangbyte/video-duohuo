#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from gen.item.ItemService import Client
from gen.item.ttypes import *

__HOST = 'localhost'
__PORT = 7000


def __get_client():
    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    return Client(protocol)


def get_item_by_id(item_id):
    client = __get_client()
    req = GetItemByIdRequest(item_id)

    return client.GetItemById(req).item


def get_item_list(type=1, offset=0, count=10, user_id=0):
    client = __get_client()
    req = GetItemListRequest(type, offset, count, user_id)
    res = client.GetItemList(req)

    return res.item_list


def add_item(user_id, video, text):
    client = __get_client()
    req = AddItemRequest(Item(
        user_id=int(user_id),
        video=video,
        text=text
    ))

    return client.AddItem(req)


def delete_item(item_id):
    client = __get_client()
    req = DeleteItemRequest(item_id)

    return client.DeleteItem(req)


def click_item(item_id):
    client = __get_client()
    req = ClickRequest(item_id)

    return client.Click(req)
