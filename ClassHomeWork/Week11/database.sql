-- auto-generated definition
create table books
(
  Id          int auto_increment
    primary key,
  BookID      varchar(255) null,
  BookName    varchar(255) null,
  Author      varchar(255) null,
  Publisher   varchar(255) null,
  OriginName  varchar(255) null,
  Translatoer varchar(255) null,
  YearPublish varchar(255) null,
  PageNumber  varchar(255) null,
  Price       varchar(255) null,
  Binding     varchar(255) null,
  Collection  varchar(255) null,
  ISBN        varchar(255) null,
  Rates       varchar(255) null,
  CommentNum  varchar(255) null
);
