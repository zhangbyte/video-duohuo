#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

from gen.item import ItemService
from get_item_by_id import GetItemByIdHandler
from add_item import AddItemHandler
from delete_item import DeleteItemHandler
from get_item_list import GetItemListHandler
from click import ClickHandler

__HOST = 'localhost'
__PORT = 7000


class ItemServiceHandler(object):
    def GetItemById(self, req):
        return GetItemByIdHandler(req).execute()

    def GetItemList(self, req):
        return GetItemListHandler(req).execute()

    def AddItem(self, req):
        return AddItemHandler(req).execute()

    def DeleteItem(self, req):
        return DeleteItemHandler(req).execute()

    def Click(self, req):
        return ClickHandler(req).execute()


if __name__ == '__main__':
    handler = ItemServiceHandler()

    processor = ItemService.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the item server at', __HOST, ':', __PORT)
    rpcServer.serve()
