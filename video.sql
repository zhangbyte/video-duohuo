# DROP database if EXISTS video;
#
# CREATE database video;

use video;

# GRANT SELECT, INSERT, UPDATE, DELETE ON video.* TO 'video'@'localhost' identified BY 'video';

# CREATE TABLE user(
# `id` bigint NOT NULL AUTO_INCREMENT COMMENT '用户id',
# `openid` varchar(50) NOT NULL COMMENT '微信openid',
# `nickname` varchar(50) NOT NULL DEFAULT '' COMMENT '微信昵称',
# `head_img_url` varchar(255) NOT NULL DEFAULT '' COMMENT '微信头像地址',
# `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
# PRIMARY KEY (id),
# KEY (openid)
# )ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='用户信息表';

# CREATE TABLE item(
#   `id` bigint NOT NULL AUTO_INCREMENT COMMENT '短视频id',
#   `user_id` bigint NOT NULL COMMENT '用户id',
#   `video` varchar(255) NOT NULL COMMENT '短视频地址',
#   `text` varchar(255) NOT NULL COMMENT '短视频描述',
#   `click` int NOT NULL DEFAULT 0 COMMENT '点击数',
#   `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
#   PRIMARY KEY (id)
# )ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='短视频信息表';

CREATE TABLE relation(
`id` bigint NOT NULL AUTO_INCREMENT COMMENT '点赞id',
`from_user_id` bigint NOT NULL COMMENT '关注用户id',
`to_user_id` bigint NOT NULL COMMENT '被关注用户id',
`create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
PRIMARY KEY (id)
)ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='关注关系表';

CREATE TABLE love(
`id` bigint NOT NULL AUTO_INCREMENT COMMENT '点赞id',
`from_user_id` bigint NOT NULL COMMENT '用户id',
`item_id` bigint NOT NULL COMMENT '被点赞的短视频id',
`create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
PRIMARY KEY (id)
)ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='点赞关系表';

CREATE TABLE comment(
`id` bigint NOT NULL AUTO_INCREMENT COMMENT '评论id',
`item_id` bigint NOT NULL COMMENT '短视频id',
`user_id` bigint NOT NULL COMMENT '用户id',
`text` varchar(255) NOT NULL COMMENT '评论内容',
`create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
PRIMARY KEY (id)
)ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='评论信息表';