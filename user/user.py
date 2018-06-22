#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

from gen.user import UserService
from get_user_info import GetUserInfoHandler
from get_user_info_for_openid import GetUserInfoForOpenidHandler
from get_user_info_list import GetUserInfoListHandler
from update_user_info import UpdateUserInfoHandler

__HOST = 'localhost'
__PORT = 7001


class UserServiceHandler(object):

    def GetUserInfo(self, req):
        return GetUserInfoHandler(req).execute()

    def GetUserInfoForOpenid(self, req):
        return GetUserInfoForOpenidHandler(req).execute()

    def GetUserInfoList(self, req):
        return GetUserInfoListHandler(req).execute()

    def UpdateUserInfo(self, req):
        return UpdateUserInfoHandler(req).execute()


if __name__ == '__main__':
    handler = UserServiceHandler()

    processor = UserService.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the user server at', __HOST, ':', __PORT)
    rpcServer.serve()
