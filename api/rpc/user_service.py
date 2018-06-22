#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from gen.user.UserService import Client
from gen.user.ttypes import *

__HOST = 'localhost'
__PORT = 7001


def __get_client():
    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    return Client(protocol)


def update_user_info(user_id, nickname, head_img_url):
    client = __get_client()
    req = UpdateUserInfoRequest(UserInfo(
        user_id=int(user_id),
        nickname=nickname,
        head_img_url=head_img_url
    ))

    return client.UpdateUserInfo(req)


def get_user_info(user_id):
    client = __get_client()
    req = GetUserInfoRequest(int(user_id))

    return client.GetUserInfo(req).user


def get_user_info_for_openid(openid):
    client = __get_client()
    req = GetUserInfoForOpenidRequest(openid)

    return client.GetUserInfoForOpenid(req).user


def get_user_info_list(ids):
    client = __get_client()
    req = GetUserInfoListRequest(ids)

    return client.GetUserInfoList(req).user_info_list
