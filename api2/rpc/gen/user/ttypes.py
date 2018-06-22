#
# Autogenerated by Thrift Compiler (0.11.0)
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


class UserInfo(object):
    """
    Attributes:
     - user_id
     - openid
     - nickname
     - head_img_url
     - create_time
    """


    def __init__(self, user_id=None, openid=None, nickname=None, head_img_url=None, create_time=None,):
        self.user_id = user_id
        self.openid = openid
        self.nickname = nickname
        self.head_img_url = head_img_url
        self.create_time = create_time

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
                if ftype == TType.STRING:
                    self.openid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.nickname = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.head_img_url = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.create_time = iprot.readI64()
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
        oprot.writeStructBegin('UserInfo')
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 1)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.openid is not None:
            oprot.writeFieldBegin('openid', TType.STRING, 2)
            oprot.writeString(self.openid.encode('utf-8') if sys.version_info[0] == 2 else self.openid)
            oprot.writeFieldEnd()
        if self.nickname is not None:
            oprot.writeFieldBegin('nickname', TType.STRING, 3)
            oprot.writeString(self.nickname.encode('utf-8') if sys.version_info[0] == 2 else self.nickname)
            oprot.writeFieldEnd()
        if self.head_img_url is not None:
            oprot.writeFieldBegin('head_img_url', TType.STRING, 4)
            oprot.writeString(self.head_img_url.encode('utf-8') if sys.version_info[0] == 2 else self.head_img_url)
            oprot.writeFieldEnd()
        if self.create_time is not None:
            oprot.writeFieldBegin('create_time', TType.I64, 5)
            oprot.writeI64(self.create_time)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
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


class GetUserInfoRequest(object):
    """
    Attributes:
     - user_id
    """


    def __init__(self, user_id=None,):
        self.user_id = user_id

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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('GetUserInfoRequest')
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 1)
            oprot.writeI64(self.user_id)
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


class UserInfoResponse(object):
    """
    Attributes:
     - user
    """


    def __init__(self, user=None,):
        self.user = user

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
                if ftype == TType.STRUCT:
                    self.user = UserInfo()
                    self.user.read(iprot)
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
        oprot.writeStructBegin('UserInfoResponse')
        if self.user is not None:
            oprot.writeFieldBegin('user', TType.STRUCT, 1)
            self.user.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user is None:
            raise TProtocolException(message='Required field user is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetUserInfoForOpenidRequest(object):
    """
    Attributes:
     - openid
    """


    def __init__(self, openid=None,):
        self.openid = openid

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
                if ftype == TType.STRING:
                    self.openid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('GetUserInfoForOpenidRequest')
        if self.openid is not None:
            oprot.writeFieldBegin('openid', TType.STRING, 1)
            oprot.writeString(self.openid.encode('utf-8') if sys.version_info[0] == 2 else self.openid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.openid is None:
            raise TProtocolException(message='Required field openid is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetUserInfoListRequest(object):
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
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI64()
                        self.ids.append(_elem5)
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
        oprot.writeStructBegin('GetUserInfoListRequest')
        if self.ids is not None:
            oprot.writeFieldBegin('ids', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.ids))
            for iter6 in self.ids:
                oprot.writeI64(iter6)
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


class UserInfoListResponse(object):
    """
    Attributes:
     - user_info_list
    """


    def __init__(self, user_info_list=None,):
        self.user_info_list = user_info_list

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
                    self.user_info_list = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = UserInfo()
                        _elem12.read(iprot)
                        self.user_info_list.append(_elem12)
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
        oprot.writeStructBegin('UserInfoListResponse')
        if self.user_info_list is not None:
            oprot.writeFieldBegin('user_info_list', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.user_info_list))
            for iter13 in self.user_info_list:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user_info_list is None:
            raise TProtocolException(message='Required field user_info_list is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UpdateUserInfoRequest(object):
    """
    Attributes:
     - user
    """


    def __init__(self, user=None,):
        self.user = user

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
                if ftype == TType.STRUCT:
                    self.user = UserInfo()
                    self.user.read(iprot)
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
        oprot.writeStructBegin('UpdateUserInfoRequest')
        if self.user is not None:
            oprot.writeFieldBegin('user', TType.STRUCT, 1)
            self.user.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.user is None:
            raise TProtocolException(message='Required field user is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(UserInfo)
UserInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'user_id', None, None, ),  # 1
    (2, TType.STRING, 'openid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'nickname', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'head_img_url', 'UTF8', None, ),  # 4
    (5, TType.I64, 'create_time', None, None, ),  # 5
)
all_structs.append(BaseResponse)
BaseResponse.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'success', None, None, ),  # 1
    (2, TType.STRING, 'msg', 'UTF8', None, ),  # 2
)
all_structs.append(GetUserInfoRequest)
GetUserInfoRequest.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'user_id', None, None, ),  # 1
)
all_structs.append(UserInfoResponse)
UserInfoResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'user', [UserInfo, None], None, ),  # 1
)
all_structs.append(GetUserInfoForOpenidRequest)
GetUserInfoForOpenidRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'openid', 'UTF8', None, ),  # 1
)
all_structs.append(GetUserInfoListRequest)
GetUserInfoListRequest.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'ids', (TType.I64, None, False), None, ),  # 1
)
all_structs.append(UserInfoListResponse)
UserInfoListResponse.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'user_info_list', (TType.STRUCT, [UserInfo, None], False), None, ),  # 1
)
all_structs.append(UpdateUserInfoRequest)
UpdateUserInfoRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'user', [UserInfo, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
