#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from gen.relation.RelationService import Client
from gen.relation.ttypes import *

__HOST = 'localhost'
__PORT = 7003


def __get_client():
    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    return Client(protocol)


def following(from_user_id, to_user_id):
    client = __get_client()
    req = BaseFollowRequest(from_user_id, to_user_id)

    return client.Following(req)


def un_following(from_user_id, to_user_id):
    client = __get_client()
    req = BaseFollowRequest(from_user_id, to_user_id)

    return client.UnFollowing(req)


def love(user_id, item_id):
    client = __get_client()
    req = BaseLoveRequest(user_id, item_id)

    return client.Love(req)


def un_love(user_id, item_id):
    client = __get_client()
    req = BaseLoveRequest(user_id, item_id)

    return client.UnLove(req)


def get_following_list(user_id, offset=0, count=10):
    client = __get_client()
    req = FollowListRequest(user_id, offset, count)

    return client.GetFollowingList(req).ids


def get_follower_list(user_id, offset=0, count=10):
    client = __get_client()
    req = FollowListRequest(user_id, offset, count)

    return client.GetFollowerList(req).ids


def get_follow_status(from_user_id, to_user_ids):
    client = __get_client()
    req = FollowStatusRequest(from_user_id, to_user_ids)

    return client.GetFollowStatus(req).status


def get_love_status(user_id, item_ids):
    client = __get_client()
    req = LoveStatusRequest(user_id, item_ids)

    return client.GetLoveStatus(req).status


def get_follow_count(user_id, type=1):
    client = __get_client()
    req = FollowCountRequest(user_id, type)

    return client.GetFollowCount(req).count


def get_love_count(item_ids):
    client = __get_client()
    req = LoveCountRequest(item_ids)

    return client.GetLoveCount(req).counts
