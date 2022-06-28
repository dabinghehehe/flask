# note笔记数据库设计

## 进入mysql容器

```shell
docker exec -it mysql env LANG=C.UTF-8 /bin/bash
```

## 创建数据库

```sql
CREATE DATABASE note
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

## 用户表users

| 字段名称   | 字段类型    | 字段约束                                                     | 字段说明                                 |
| ---------- | ----------- | ------------------------------------------------------------ | ---------------------------------------- |
| userid     | int(11)     | 自增长、主键、不为空                                         | 用户唯一编号                             |
| username   | varchar(50) | 字符串、最长50、不为空                                       | 登录账号，可为有效的邮箱地址或者电话号码 |
| password   | varchar(32) | MD5加密字符串、不为空                                        | 密码登录                                 |
| nickname   | varchar(30) | 字符串、最长30、可为空                                       | 用户昵称                                 |
| avatar     | varchar(20) | 字符串、最长20、可为空                                       | 用户头像的图片文件名                     |
| qq         | varchar(15) | 字符串、最长15、可为空                                       | 用户的qq                                 |
| role       | varchar(10) | 字符串、不为空，admin表示管理员，editor表示作者，user表示普通用户 | 用户的角色                               |
| credit     | int(11)     | 整数类型、默认50，不为空,表示用户注册时即赠送50积分          | 用户的剩余积分                           |
| createtime | datetime    | 时间日期类型、格式为yyyy-mm-dd hh:mm:ss                      | 该条数据的新增时间                       |
| updatetime | datetime    | 时间日期类型、格式为yyyy-mm-dd hh:mm:ss                      | 该条数据修改时间                         |

```sql
CREATE TABLE users(
    userid INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(32) NOT NULL,
    nickname VARCHAR(30),
    avatar VARCHAR(20),
    qq VARCHAR(15),
    role VARCHAR(10) NOT NULL,
    credit INT(11) NOT NULL DEFAULT 50,
    createtime datetime,
    updatetime datetime,
    PRIMARY KEY (userid)
);
```

数据插入

```sql
INSERT INTO users VALUES(1,'woniu@woniuxy.com','e10adc3949ba59abbe56e057f20f883e','蜗牛','1.png','12345678','admin',0,'2022-06-28 15:08:54','2022-06-28 18:01:54');

INSERT INTO users VALUES(2,'qiang@woniuxy.com','e10adc3949ba59abbe56e057f20f883e','强哥','2.png','33445566','editor',50,'2022-06-28 15:08:54',NOW());

INSERT INTO users VALUES(3,'bing@woniuxy.com','e10adc3949ba59abbe56e057f20f883e','大兵','3.png','55667788','user',100,NOW(),NOW());
```

## 文章表articles

| 字段名称    | 字段类型     | 字段约束                                | 字段说明           |
| ----------- | ------------ | --------------------------------------- | ------------------ |
| articleid   | int(11)      | 自增长、主键、不为空                    | 文章唯一编号       |
| userid      | int(11)      | users表外键、不为空                     | 关联发布者信息     |
| type        | tinyint      | 整数、无默认值、不为空                  | 关联文章类型       |
| headline    | varchar(100) | 字符串、最长100、不为空                 | 文章标题           |
| content     | mediumtext   | 字符串、最大16777216字符                | 文章内容           |
| thumbnail   | varchar(20)  | 字符串、最大20字符                      | 缩略图文件名       |
| credit      | int(11)      | 整数类型、默认0                         | 文章消耗的积分数   |
| readcount   | int(11)      | 整数类型、默认0                         | 文章阅读次数       |
| replycount  | int(11)      | 整数类型、默认0                         | 评论回复次数       |
| recommended | tinyint      | 整数类型、默认0（不推荐）               | 是否设为推荐文章   |
| hidden      | tinyint      | 整数类型、默认0（不隐藏）               | 文章是否被隐藏     |
| drafted     | tinyint      | 整数类型、默认0（非草稿）               | 文章是否是草稿     |
| checked     | tinyint      | 整数类型、默认1（正式文章）             | 文章是否被审核     |
| createtime  | datetime     | 时间日期类型、格式为yyyy-mm-dd hh:mm:ss | 该条数据的新增时间 |
| updatetime  | datetime     | 时间日期类型、格式为yyyy-mm-dd hh:mm:ss | 该条数据修改时间   |

```mysql
CREATE TABLE article(
    articleid int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userid int(11) NOT NULL,
    type tinyint NOT NULL,
    headline varchar(100) NOT NULL,
    content mediumtext,
    thumbnail varchar(20),
    credit int(11) NOT NULL DEFAULT 0,
    readcount int(11) NOT NULL DEFAULT 0,
    replycount int(11) NOT NULL DEFAULT 0,
    recommended tinyint NOT NULL DEFAULT 0,
    hidden tinyint NOT NULL DEFAULT 0,
    drafted tinyint NOT NULL DEFAULT 0,
    checked tinyint NOT NULL DEFAULT 1,
    createtime datetime,
    updatetime datetime,
    FOREIGN KEY (userid) REFERENCES users (userid)
);
```

```mysql
INSERT INTO article(userid,type,headline,content,thumbnail,createtime,updatetime) VALUES(1,1,'flask学习','hello，小伙伴们','a-1.png',NOW(),NOW());
INSERT INTO article(userid,type,headline,content,thumbnail,createtime,updatetime) VALUES(2,1,'django学习','hello，小伙scs产地四川省的山地车山地车伴们','a-2.png',NOW(),NOW());
INSERT INTO article(userid,type,headline,content,thumbnail,createtime,updatetime) VALUES(3,1,'python学习','hello，小伙scs产地四川省的山地车山地车伴们','a-3.png',NOW(),NOW());
```

## 用户评论表comment

## 积分表credit

## 收藏表favorite

