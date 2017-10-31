*MySQL 是最流行的关系型数据库管理系统之一,属于 Oracle 旗下产品*

## 安装启动操作
1.安装mysql命令 ：$ `sudo apt-get install -y mysql-server`  
2.查看mysql的版本命令（注意-V是大写，不然会出现如下错误）：$ `mysql -V`  
3.启动mysql命令(关闭，重启等只需将start换成stop,restart等即可)：$`sudo service mysql start`  
4.登录mysql命令为：$ `mysql -u用户名 -p密码`  
5.连接远程数据库：$ `mysql -h <host> -P <port> -u<username> -p<password>`

## 数据库操作
1.查看数据库：> `show databases;` （注意分号“；”不要落下）  
2.新建一个数据库命令：> `create database 数据库名称;`  
&nbsp;&nbsp;&nbsp;删除一个数据库命令：> `drop database 数据库名称;`  
3.使用某个数据库：> `use 数据库名称;`

## 表操作
1.查看表命令：> `show tables;`  
2.建立一个新表：> `create table 表名 （字段参数）;` 或 >`create table if not exists 表名（字段参数）；`  
&nbsp;&nbsp;&nbsp;删除一个旧表：> `drop table 表名；` 或 >`drop table if exists 表名；`  
3.查看表结构：> `desc 表名称;` 或 >`show columns from 表名称;`  
4.对表数据的操作：  
&nbsp;&nbsp;&nbsp;增：>`insert into 表名称 (字段名1，字段名2，字段名3......) values(字段名1的值，字段名2的值，字段名3的值......);`  
&nbsp;&nbsp;&nbsp;删：>`delete from 表名称 where 表达式;`  
&nbsp;&nbsp;&nbsp;改：>`update 表名称 set 字段名=“新值” where 表达式；`  
&nbsp;&nbsp;&nbsp;查：>`select 字段名1,字段名2,字段名3..... from 表名称;`  
5.增加字段：>`alter table 表名称 add 字段名 数据类型 其它;` (其它包括默认初始值的设定等等)  
6.删除字段：>`alter table 表名称 drop 字段名;`


## 用户相关操作
注：以下命令均需先以root身份登录mysql：`mysql -uroot -p`  
1.添加新用户  
（1）创建新用户：> `insert into mysql.user(Host,User,Password) values("localhost","user1",password("password1"));`    
（2）为用户分配权限：  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;设置用户可以在本地访问mysql：`grant all privileges on *.* to username@localhost identified by "password" ;`  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;设置用户只能访问指定数据库：`grant all privileges on 数据库名.* to username@localhost identified by "password" ;`     
（3）刷新系统权限表：>`flush privileges;`  
2.查看MySql当前所有的用户：>`SELECT DISTINCT User FROM mysql.user;`  
3.删除用户及其数据字典中包含的数据：>`drop user 'xbb'@'localhost';`

