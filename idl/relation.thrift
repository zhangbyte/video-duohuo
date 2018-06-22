namespace py relation

struct BaseFollowRequest {
    1: required i64 from_user_id,
    2: required i64 to_user_id,
}

struct BaseLoveRequest {
    1: required i64 user_id,
    2: required i64 item_id,
}

struct BaseResponse {
    1: required bool success,
    2: optional string msg,
}

struct FollowStatusRequest {
    1: required i64 from_user_id,
    2: required list<i64> to_user_ids,
}

struct LoveStatusRequest {
    1: required i64 user_id,
    2: required list<i64> item_ids,
}

struct StatusResponse {
    1: required list<bool> status,
}

struct FollowListRequest {
    1: required i64 user_id,
    2: required i32 offset = 0,
    3: required i32 count = 10,
}

struct FollowListResponse {
    1: required list<i64> ids,
}

struct FollowCountRequest {
    1: required i64 user_id,
    2: optional i32 type = 1, // 1:关注数 2:粉丝数
}

struct FollowCountResponse {
    1: required i64 count,
}

struct LoveCountRequest {
    1: required list<i64> item_ids,
}

struct LoveCountResponse {
    1: required list<i64> counts,
}

service RelationService {
    BaseResponse Following(1:BaseFollowRequest req),
    BaseResponse UnFollowing(1:BaseFollowRequest req),
    
    BaseResponse Love(1:BaseLoveRequest req),
    BaseResponse UnLove(1:BaseLoveRequest req),
    
    StatusResponse GetFollowStatus(1:FollowStatusRequest req),
    StatusResponse GetLoveStatus(1:LoveStatusRequest req),
    
    FollowListResponse GetFollowingList(1:FollowListRequest req),
    FollowListResponse GetFollowerList(1:FollowListRequest req),

    FollowCountResponse GetFollowCount(1:FollowCountRequest req),
    LoveCountResponse GetLoveCount(1:LoveCountRequest req)
}
