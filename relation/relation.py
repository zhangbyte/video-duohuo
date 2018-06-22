#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

from gen.relation import RelationService
from following import FollowingHandler
from un_following import UnFollowingHandler
from love import LoveHandler
from un_love import UnLoveHandler
from get_following_list import GetFollowingListHandler
from get_follower_list import GetFollowerListHandler
from get_follow_status import GetFollowStatusHandler
from get_love_status import GetLoveStatusHandler
from get_follow_count import GetFollowCountHandler
from get_love_count import GetLoveCountHandler

__HOST = 'localhost'
__PORT = 7003


class RelationServiceHandler(object):
    def Following(self, req):
        return FollowingHandler(req).execute()

    def UnFollowing(self, req):
        return UnFollowingHandler(req).execute()

    def Love(self, req):
        return LoveHandler(req).execute()

    def UnLove(self, req):
        return UnLoveHandler(req).execute()

    def GetFollowingList(self, req):
        return GetFollowingListHandler(req).execute()

    def GetFollowerList(self, req):
        return GetFollowerListHandler(req).execute()

    def GetFollowStatus(self, req):
        return GetFollowStatusHandler(req).execute()

    def GetLoveStatus(self, req):
        return GetLoveStatusHandler(req).execute()

    def GetFollowCount(self, req):
        return GetFollowCountHandler(req).execute()

    def GetLoveCount(self, req):
        return GetLoveCountHandler(req).execute()


if __name__ == '__main__':
    handler = RelationServiceHandler()

    processor = RelationService.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the relation server at', __HOST, ':', __PORT)
    rpcServer.serve()
