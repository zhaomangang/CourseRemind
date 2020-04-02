

# 课程提醒系统（CourseRemind）

### 一、项目简介

CourseRemind是一款用于提醒学生上课的服务系统。通过对已录入系统的课程和当前系统的时间进行比对，发送邮件提醒用户。目的是为了解决课程繁多容易遗漏的问题。话说“懒惰是人类进步的阶梯hahahhahahha”

#### 功能列表

- 注册、登录
- 手动录入课程
- 导入相同班级
- 邮件提醒上课

### 二、开发文档

#### 系统架构

#### 数据库

数据库版本：MySql8.0

创建数据库

```mysql
CREATE DATABASE courseRemindSystem
```

user_info(用户信息表)

```mysql
CREATE TABLE IF NOT EXISTS `user_info`(
                `user_id` INT UNSIGNED AUTO_INCREMENT,
                `user_name` VARCHAR(20) NOT NULL,
                `password` VARCHAR(16) NOT NULL,
                `e-mail` VARCHAR(32) NOT NULL,
                `reserve_1` VARCHAR(20),
                `reserve_2` VARCHAR(20),
                `reserve_3` VARCHAR(20),
                PRIMARY KEY ( `user_id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

| 字段名 | user_id                                                      | username                | password               | e-mail               | reserve_1 | reserve_2 | reserve_3 |
| ------ | ------------------------------------------------------------ | ----------------------- | ---------------------- | -------------------- | --------- | --------- | --------- |
| 说明   | 用户id                                                       | 用户名                  | 密码                   | 邮箱                 | 预留位1   | 预留位2   | 预留位3   |
| 属性   | INT                               PRIMARY KEY  NOT NULL  AUTO_INCREMENT | VARCHAR(20)    NOT NULL | VARCHAR(16)   NOT NULL | VARCHAR(32) NOT NULL |           |           |           |

course_info(课程信息表)

```mysql
CREATE TABLE IF NOT EXISTS `course_info`(
                `course_id` INT UNSIGNED AUTO_INCREMENT,
                `course_name` VARCHAR(40) NOT NULL,
                `begin_time` VARCHAR(26) NOT NULL,
                `teacher` VARCHAR(10) NOT NULL,
                `belong_class` VARCHAR(30),
                `enter_user` INT UNSIGNED,
                `classroom` VARCHAR(40),
                `reserve_1` VARCHAR(20),
                `reserve_2` VARCHAR(20),
                `reserve_3` VARCHAR(20),
                PRIMARY KEY ( `course_id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

| 字段名 | course_id                                                    | course_name          | begin_time                                     | teacher     | belong_class                               | enter_user               | classroom   | reserve_1 | reserve_2 | reserve_3 |
| ------ | ------------------------------------------------------------ | -------------------- | ---------------------------------------------- | ----------- | ------------------------------------------ | ------------------------ | ----------- | --------- | --------- | --------- |
| 说明   | 课程id                                                       | 课程名               | 上课时间（格式1：202004021600  格式2：041600） | 老师        | 所属班级(此字段作为用户导入现成课表的依据) | 录入人(自动填入上传者id) | 上课教室    | 预留位1   | 预留位2   | 预留位3   |
| 属性   | INT              PRIMARY KEY               NOT NULL   AUTO_INCREMENT | VARCHAR(40) NOT NULL | VARCHAR(20) NOT NULL                           | VARCHAR(10) | VARCHAR(30)                                | INT                      | VARCHAR(40) |           |           |           |

relation_course_user(用户课程关系表)

```mysql
CREATE TABLE IF NOT EXISTS `relation_course_user`(
                `index` INT UNSIGNED AUTO_INCREMENT,
                `user_id` INT UNSIGNED NOT NULL,
                `course_id` INT UNSIGNED NOT NULL,
                `reserve_1` VARCHAR(20),
                `reserve_2` VARCHAR(20),
                PRIMARY KEY ( `index` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

| 字段名 | index                                                        | user_id      | course_id       | reserve_1 | reserve_2 |
| ------ | ------------------------------------------------------------ | ------------ | --------------- | --------- | --------- |
| 说明   | 序列                                                         | 用户id       | 课程id          | 预留位1   | 预留位2   |
| 属性   | INT                                                             PRIMARY KEY                                                                   NOT NULL                                          AUTO_INCREMENT | INT  NOTNULL | INT     NOTNULL |           |           |

#### 编译和安装

#### 系统测试



### 三、更新日志

### 四、BUG反馈

### 五、联系方式

