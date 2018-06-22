#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class BaseFollowRequest(object):
    """
    Attributes:
     - from_user_id
     - to_user_id

    """


    def __init__(self, from_user_id=None, to_user_id=None,):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.from_user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.to_user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BaseFollowRequest')
        if self.from_user_id is not None:
            oprot.writeFieldBegin('from_user_id', TType.I64, 1)
            oprot.writeI64(self.from_user_id)
            oprot.writeFieldEnd()
        if self.to_user_id is not None:
            oprot.writeFieldBegin('to_user_id', TType.I64, 2)
            oprot.writeI64(self.to_user_id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.from_user_id is None:
            raise TProtocolException(message='Required field from_user_id is unset!')
        if self.to_user_id is None:
            raise TProtocolException(message='Required field to_user_id is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BaseLoveRequest(object):
    """
    Attributes:
     - user_id
     - item_id

    """


    def __init__(self, user_id=None, item_id=None,):
        self.user_id = user_id
        self.item_id = item_id

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.item_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BaseLoveRequest')
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 1)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.item_id is not None:
            oprot.writeFieldBegin('item_id', TType.I64, 2)
            oprot.writeI64(self.item_id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user_id is None:
            raise TProtocolException(message='Required field user_id is unset!')
        if self.item_id is None:
            raise TProtocolException(message='Required field item_id is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BaseResponse(object):
    """
    Attributes:
     - success
     - msg

    """


    def __init__(self, success=None, msg=None,):
        self.success = success
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BaseResponse')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 1)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 2)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.success is None:
            raise TProtocolException(message='Required field success is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FollowStatusRequest(object):
    """
    Attributes:
     - from_user_id
     - to_user_ids

    """


    def __init__(self, from_user_id=None, to_user_ids=None,):
        self.from_user_id = from_user_id
        self.to_user_ids = to_user_ids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.from_user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.to_user_ids = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI64()
                        self.to_user_ids.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FollowStatusRequest')
        if self.from_user_id is not None:
            oprot.writeFieldBegin('from_user_id', TType.I64, 1)
            oprot.writeI64(self.from_user_id)
            oprot.writeFieldEnd()
        if self.to_user_ids is not None:
            oprot.writeFieldBegin('to_user_ids', TType.LIST, 2)
            oprot.writeListBegin(TType.I64, len(self.to_user_ids))
            for iter6 in self.to_user_ids:
                oprot.writeI64(iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.from_user_id is None:
            raise TProtocolException(message='Required field from_user_id is unset!')
        if self.to_user_ids is None:
            raise TProtocolException(message='Required field to_user_ids is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoveStatusRequest(object):
    """
    Attributes:
     - user_id
     - item_ids

    """


    def __init__(self, user_id=None, item_ids=None,):
        self.user_id = user_id
        self.item_ids = item_ids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.item_ids = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = iprot.readI64()
                        self.item_ids.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LoveStatusRequest')
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 1)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.item_ids is not None:
            oprot.writeFieldBegin('item_ids', TType.LIST, 2)
            oprot.writeListBegin(TType.I64, len(self.item_ids))
            for iter13 in self.item_ids:
                oprot.writeI64(iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user_id is None:
            raise TProtocolException(message='Required field user_id is unset!')
        if self.item_ids is None:
            raise TProtocolException(message='Required field item_ids is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class StatusResponse(object):
    """
    Attributes:
     - status

    """


    def __init__(self, status=None,):
        self.status = status

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.status = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readBool()
                        self.status.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('StatusResponse')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.LIST, 1)
            oprot.writeListBegin(TType.BOOL, len(self.status))
            for iter20 in self.status:
                oprot.writeBool(iter20)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.status is None:
            raise TProtocolException(message='Required field status is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FollowListRequest(object):
    """
    Attributes:
     - user_id
     - offset
     - count

    """


    def __init__(self, user_id=None, offset=0, count=10,):
        self.user_id = user_id
        self.offset = offset
        self.count = count

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.offset = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FollowListRequest')
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 1)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.offset is not None:
            oprot.writeFieldBegin('offset', TType.I32, 2)
            oprot.writeI32(self.offset)
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I32, 3)
            oprot.writeI32(self.count)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user_id is None:
            raise TProtocolException(message='Required field user_id is unset!')
        if self.offset is None:
            raise TProtocolException(message='Required field offset is unset!')
        if self.count is None:
            raise TProtocolException(message='Required field count is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FollowListResponse(object):
    """
    Attributes:
     - ids

    """


    def __init__(self, ids=None,):
        self.ids = ids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.ids = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = iprot.readI64()
                        self.ids.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FollowListResponse')
        if self.ids is not None:
            oprot.writeFieldBegin('ids', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.ids))
            for iter27 in self.ids:
                oprot.writeI64(iter27)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.ids is None:
            raise TProtocolException(message='Required field ids is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FollowCountRequest(object):
    """
    Attributes:
     - user_id
     - type

    """


    def __init__(self, user_id=None, type=1,):
        self.user_id = user_id
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FollowCountRequest')
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 1)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user_id is None:
            raise TProtocolException(message='Required field user_id is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FollowCountResponse(object):
    """
    Attributes:
     - count

    """


    def __init__(self, count=None,):
        self.count = count

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.count = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FollowCountResponse')
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I64, 1)
            oprot.writeI64(self.count)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.count is None:
            raise TProtocolException(message='Required field count is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoveCountRequest(object):
    """
    Attributes:
     - item_ids

    """


    def __init__(self, item_ids=None,):
        self.item_ids = item_ids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.item_ids = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = iprot.readI64()
                        self.item_ids.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LoveCountRequest')
        if self.item_ids is not None:
            oprot.writeFieldBegin('item_ids', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.item_ids))
            for iter34 in self.item_ids:
                oprot.writeI64(iter34)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.item_ids is None:
            raise TProtocolException(message='Required field item_ids is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoveCountResponse(object):
    """
    Attributes:
     - counts

    """


    def __init__(self, counts=None,):
        self.counts = counts

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.counts = []
                    (_etype38, _size35) = iprot.readListBegin()
                    for _i39 in range(_size35):
                        _elem40 = iprot.readI64()
                        self.counts.append(_elem40)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('LoveCountResponse')
        if self.counts is not None:
            oprot.writeFieldBegin('counts', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.counts))
            for iter41 in self.counts:
                oprot.writeI64(iter41)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.counts is None:
            raise TProtocolException(message='Required field counts is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(BaseFollowRequest)
BaseFollowRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'from_user_id', None, None, ),  # 1
    (2, TType.I64, 'to_user_id', None, None, ),  # 2
)
all_structs.append(BaseLoveRequest)
BaseLoveRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'user_id', None, None, ),  # 1
    (2, TType.I64, 'item_id', None, None, ),  # 2
)
all_structs.append(BaseResponse)
BaseResponse.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'success', None, None, ),  # 1
    (2, TType.STRING, 'msg', 'UTF8', None, ),  # 2
)
all_structs.append(FollowStatusRequest)
FollowStatusRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'from_user_id', None, None, ),  # 1
    (2, TType.LIST, 'to_user_ids', (TType.I64, None, False), None, ),  # 2
)
all_structs.append(LoveStatusRequest)
LoveStatusRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'user_id', None, None, ),  # 1
    (2, TType.LIST, 'item_ids', (TType.I64, None, False), None, ),  # 2
)
all_structs.append(StatusResponse)
StatusResponse.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'status', (TType.BOOL, None, False), None, ),  # 1
)
all_structs.append(FollowListRequest)
FollowListRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'user_id', None, None, ),  # 1
    (2, TType.I32, 'offset', None, 0, ),  # 2
    (3, TType.I32, 'count', None, 10, ),  # 3
)
all_structs.append(FollowListResponse)
FollowListResponse.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'ids', (TType.I64, None, False), None, ),  # 1
)
all_structs.append(FollowCountRequest)
FollowCountRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'user_id', None, None, ),  # 1
    (2, TType.I32, 'type', None, 1, ),  # 2
)
all_structs.append(FollowCountResponse)
FollowCountResponse.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'count', None, None, ),  # 1
)
all_structs.append(LoveCountRequest)
LoveCountRequest.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'item_ids', (TType.I64, None, False), None, ),  # 1
)
all_structs.append(LoveCountResponse)
LoveCountResponse.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'counts', (TType.I64, None, False), None, ),  # 1
)
fix_spec(all_structs)
del all_structs
