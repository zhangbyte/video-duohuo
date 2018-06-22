namespace py item

struct Item {
    1: optional i64 item_id,
    2: required i64 user_id,
    3: required string video,
    4: required string text,
    5: optional i64 click,
    6: optional i64 create_time,
}

struct BaseResponse {
    1: required bool success,
    2: optional string msg,
}

struct GetItemByIdRequest {
    1: required i64 item_id,
}

struct GetItemByIdResponse {
    1: required Item item,
}

struct GetItemListRequest {
    1: optional i32 type = 1, // 1:按时间 2:按热度
    2: optional i32 offset = 0,
    3: optional i32 count = 10,
    4: optional i64 user_id,
}

struct GetItemListResponse {
    1: required list<Item> item_list,
}

struct AddItemRequest {
    1: required Item item,
}

struct DeleteItemRequest {
    1: required i64 item_id,
}

struct ClickRequest {
    1: required i64 item_id,
}

service ItemService {
    GetItemByIdResponse GetItemById(1:GetItemByIdRequest req),
    GetItemListResponse GetItemList(1:GetItemListRequest req),
    BaseResponse AddItem(1:AddItemRequest req),
    BaseResponse DeleteItem(1:DeleteItemRequest req),

    BaseResponse Click(1:ClickRequest req),
}
