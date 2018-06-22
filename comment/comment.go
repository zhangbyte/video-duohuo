package main

import (
	gen "comment/gen/comment"
	"fmt"
	"git.apache.org/thrift.git/lib/go/thrift"
	"golang.org/x/net/context"
	"comment/db"
)

type CommentServiceHandler struct {
}

func (handler *CommentServiceHandler) GetCommentList(ctx context.Context, req *gen.GetCommentListRequest) (res *gen.GetCommentListResponse, err error) {
	comments := db.GetCommentList(req.ItemID, req.Offset, req.Count)
	commentList := []*gen.Comment{}
	for _, item := range comments {
		commentId := item.Id
		createTime := item.CreateTime.Unix()
		commentList = append(commentList, &gen.Comment{
			CommentID: &commentId,
			ItemID: item.ItemId,
			UserID: item.UserId,
			Text: item.Text,
			CreateTime: &createTime,
		})
	}

	return &gen.GetCommentListResponse{
		CommentList: commentList,
	}, nil
}

func (handler *CommentServiceHandler) AddComment(ctx context.Context, req *gen.AddCommentRequest) (res *gen.BaseResponse, err error) {
	fmt.Printf("AddComment")

	db.AddComment(req.Comment.ItemID, req.Comment.UserID, req.Comment.Text)
	return &gen.BaseResponse{
		Success: true,
	}, nil
}

func main() {
	serverTransport, err := thrift.NewTServerSocket("127.0.0.1:7002")
	if err != nil {
		fmt.Println("Error!", err)
		return
	}
	handler := &CommentServiceHandler{}
	processor := gen.NewCommentServiceProcessor(handler)
	server := thrift.NewTSimpleServer2(processor, serverTransport)
	fmt.Println("thrift server in localhost:7002")

	server.Serve()
}
