# COVID19_Flask
## 基于Flask的COVID-19中国历史数据和当前数据爬虫&相关新闻报道数据爬虫
---
### 项目信息
本项目基于Bilibil视频[（BV177411j7qJ）](https://www.bilibili.com/video/BV177411j7qJ)的基础上而来，由于原项目部分功能的接口已经失效，部分功能（热搜词云）未完整实现，部分功能实现和数据获取采用了其他方法进行代替。
#### 作者
@xmx-xmx-xmx-xmx
#### 演示地址
http://159.75.26.43:8889/
---
[我的邮箱](yimin710273791@gmail.com)
#### 发布日期
2021/02/17
#### 版本
V1.0

---

### 基于平台
#### 代码：
1. Python 3.9.0
2. Javascript
3. HTML
4. CSS
#### 开发工具：
VS Code
#### 数据库：
MySQL
#### 使用的Python库：
Flask, time, json, simplejson, requests, traceback, pymysql

---

### 食用指南
1. 数据库创建：
使用MySQL创建数据库，用于存放疫情数据和热搜数据（这个功能被取消了）
修改`utils.py`中的数据库连接字符串为你自己的用户名和密码
```
CREATE TABLE `history`(
	`ds` datetime NOT NULL COMMENT '日期',
	`confirm_add` int(11) DEFAULT NULL COMMENT '新增确诊',
	`suspect_add` int(11) DEFAULT NULL COMMENT '新增疑似',
	`dead_add` int(11) DEFAULT NULL COMMENT '新增死亡',
	`heal_add` int(11) DEFAULT NULL COMMENT '新增治愈',
	PRIMARY KEY (`ds`) USING BTREE
	)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
	
CREATE TABLE `detail`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`update_time` datetime DEFAULT NULL COMMENT '更新时间',
	`province` varchar(50) DEFAULT NULL COMMENT '省份',
	`city` varchar(50) DEFAULT NULL COMMENT '城市',
	`confirm` int(11) DEFAULT NULL COMMENT '确诊',
	`confirm_add` int(11) DEFAULT NULL COMMENT '新增确诊',
	`heal` int(11) DEFAULT NULL COMMENT '治愈',
	`dead` int(11) DEFAULT NULL COMMENT '死亡',
	PRIMARY KEY (`id`)
	)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
2. 代码部署：
安装需要的第三方库，（创建python虚拟环境），通过flask run运行项目，项目运行在本地服务器上
3. 服务器部署：
可以（通过宝塔面板等方法）部署项目在服务器上，设置定时任务，定时运行爬虫，爬虫获取的结果将存放在数据库内，前台调用数据就可以实现数据更新。
---
### 支持

1. 有任何问题可以在Git上提交issue联系我，我将及时回复。
2. 感谢支持~
