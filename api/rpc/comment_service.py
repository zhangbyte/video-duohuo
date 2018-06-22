#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from gen.comment.CommentService import Client
from gen.comment.ttypes import *

__HOST = 'localhost'
__PORT = 7002


def __get_client():
    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    return Client(protocol)


def add_comment(item_id, user_id, text):
    client = __get_client()
    req = AddCommentRequest(Comment(
        item_id=item_id,
        user_id=user_id,
        text=text
    ))

    return client.AddComment(req)


def get_comment_list(item_id, offset=0, count=10):
    client = __get_client()
    req = GetCommentListRequest(item_id, offset, count)

    return client.GetCommentList(req).comment_list
