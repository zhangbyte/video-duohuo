namespace py user

struct UserInfo {
    1: optional i64 user_id,
    2: optional string openid,
    3: optional string nickname,
    4: optional string head_img_url,
    5: optional i64 create_time,
}

struct BaseResponse {
    1: required bool success,
    2: optional string msg,
}

struct GetUserInfoRequest {
    1: required i64 user_id,
}

struct UserInfoResponse {
    1: required UserInfo user,
}

struct GetUserInfoForOpenidRequest {
    1: required string openid,
}

struct GetUserInfoListRequest {
    1: required list<i64> ids,
}

struct UserInfoListResponse {
    1: required list<UserInfo> user_info_list,
}

struct UpdateUserInfoRequest {
    1: required UserInfo user,
}

service UserService {
    UserInfoResponse GetUserInfo(1:GetUserInfoRequest req),
    UserInfoResponse GetUserInfoForOpenid(1:GetUserInfoForOpenidRequest req),
    UserInfoListResponse GetUserInfoList(1:GetUserInfoListRequest req),
    BaseResponse UpdateUserInfo(1:UpdateUserInfoRequest req),
}
