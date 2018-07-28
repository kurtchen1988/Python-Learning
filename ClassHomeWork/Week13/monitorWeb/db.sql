CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

create table machine
(
  id         int auto_increment
    primary key,
  name       varchar(10) default ''              not null
  comment '名称',
  ip         varchar(50) default ''              not null
  comment 'IP地址',
  user       varchar(50) default ''              not null
  comment '用户',
  password   varchar(50) default ''              not null
  comment '密码',
  created_at timestamp default CURRENT_TIMESTAMP not null
  comment '新增时间'
)
  comment '主机'
  engine = InnoDB;

create table monitor
(
  id         int auto_increment
    primary key,
  machine_id varchar(255)                        not null,
  cpu        varchar(255) default ''             not null,
  memory     varchar(255) default ''             not null,
  harddrive  varchar(255) default ''             not null,
  created_at timestamp default CURRENT_TIMESTAMP not null
  comment '新增时间'
)
  comment '监控'
  engine = InnoDB;

create index machine_id
  on monitor (machine_id);