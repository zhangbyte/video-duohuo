namespace py comment
namespace go comment

struct Comment {
    1: optional i64 comment_id,
    2: required i64 item_id,
    3: required i64 user_id,
    4: required string text,
    5: optional i64 create_time,
}

struct BaseResponse {
    1: required bool success,
    2: optional string msg,
}

struct GetCommentListRequest {
    1: required i64 item_id,
    2: optional i32 offset = 0,
    3: optional i32 count = 10,
}

struct GetCommentListResponse {
    1: required list<Comment> comment_list,
}

struct AddCommentRequest {
    1: required Comment comment,
}

service CommentService {
    GetCommentListResponse GetCommentList(1:GetCommentListRequest req),
    BaseResponse AddComment(1:AddCommentRequest req),
}
