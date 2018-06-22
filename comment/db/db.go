package db

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"time"
)

type Comment struct {
	Id         int64
	ItemId     int64 `orm:"item_id"`
	UserId     int64 `orm:"user_id"`
	Text       string
	CreateTime time.Time `gorm:"-"`
}

func (Comment) TableName() string {
	return "comment"
}

func AddComment(itemId int64, userId int64, text string) {
	db, err := gorm.Open("mysql", "video:video@/video?charset=utf8&parseTime=True&loc=Local")
	defer db.Close()
	if err != nil {
		panic(err)
	}

	comment := Comment{
		ItemId: itemId,
		UserId: userId,
		Text: text,
	}

	db.Create(&comment)
}

func GetCommentList(itemId int64, offset int32, count int32) (comments []Comment) {
	db, err := gorm.Open("mysql", "video:video@/video?charset=utf8&parseTime=True&loc=Local")
	defer db.Close()
	if err != nil {
		panic(err)
	}

	comments = []Comment{}
	db.Where("item_id = ?", itemId).Order("create_time desc").Offset(offset).Limit(count).Find(&comments)

	return
}
