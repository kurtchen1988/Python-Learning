CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE `machine` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(10) NOT NULL DEFAULT '' COMMENT '名称',
`ip` varchar(50) NOT NULL DEFAULT '' COMMENT 'IP地址',
`user` varchar(50) NOT NULL DEFAULT '' COMMENT '用户',
`password` varchar(50) NOT NULL DEFAULT '' COMMENT '密码',
`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='主机';

insert into machine (id,name,ip,user,password) values (1,'test','192.168.137.131','root','root1988824');

CREATE TABLE monitor (
id int(11) NOT NULL AUTO_INCREMENT,
machine_id int(10) NOT NULL,
cpu varchar(255) NOT NULL DEFAULT '',
memory varchar(255) NOT NULL DEFAULT '',
harddrive VARCHAR(255) NOT NULL DEFAULT '',
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
PRIMARY KEY (id),
KEY(machine_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='监控';