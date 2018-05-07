/*
SQLyog Trial v11.01 (32 bit)
MySQL - 5.5.53 : Database - shopdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`shopdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `shopdb`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `detail` */

DROP TABLE IF EXISTS `detail`;

CREATE TABLE `detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `orderid` int(11) unsigned DEFAULT NULL,
  `goodsid` int(11) unsigned DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `num` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `detail` */

insert  into `detail`(`id`,`orderid`,`goodsid`,`name`,`price`,`num`) values (1,1,6,'wtert',45.00,3),(2,1,4,'6426',274.00,4),(3,1,7,'wertwert',245.00,5);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(2,'auth','user'),(3,'auth','group'),(4,'auth','permission'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2018-04-20 17:52:55'),(2,'auth','0001_initial','2018-04-20 17:53:01'),(3,'admin','0001_initial','2018-04-20 17:53:03'),(4,'admin','0002_logentry_remove_auto_add','2018-04-20 17:53:03'),(5,'contenttypes','0002_remove_content_type_name','2018-04-20 17:53:03'),(6,'auth','0002_alter_permission_name_max_length','2018-04-20 17:53:03'),(7,'auth','0003_alter_user_email_max_length','2018-04-20 17:53:04'),(8,'auth','0004_alter_user_username_opts','2018-04-20 17:53:04'),(9,'auth','0005_alter_user_last_login_null','2018-04-20 17:53:04'),(10,'auth','0006_require_contenttypes_0002','2018-04-20 17:53:04'),(11,'auth','0007_alter_validators_add_error_messages','2018-04-20 17:53:04'),(12,'auth','0008_alter_user_username_max_length','2018-04-20 17:53:04'),(13,'auth','0009_alter_user_last_name_max_length','2018-04-20 17:53:05'),(14,'sessions','0001_initial','2018-04-20 17:53:05');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('hydhz9bcsexzuvuwq3fda3k1ztab7i7x','NDUzNjVjNGMyNmVlOWUwZmE1NGY1ZjM0Yzc4NGQ5YzdmOTlkOWYxMjp7InNob3BsaXN0Ijp7IjIiOnsic3RhdGUiOjEsImdvb2RzIjoiMTIzIiwiY29tcGFueSI6IjIzNDUiLCJwcmljZSI6MTIzLjAsImNsaWNrbnVtIjo0LCJudW0iOjAsImlkIjoyLCJwaWNuYW1lIjoiMTUyNDM0MzExNC4yMzI1OTI4LmpwZyIsInN0b3JlIjoxMjMsInR5cGVpZCI6MywibSI6MX19LCJhZG1pbnVzZXIiOnsidXNlcm5hbWUiOiIxMjMiLCJpZCI6NCwicGFzc3dvcmQiOiIyMDJjYjk2MmFjNTkwNzViOTY0YjA3MTUyZDIzNGI3MCIsImVtYWlsIjoiMTIzIiwibmFtZSI6IjEyMyIsImFkZHJlc3MiOiIxMjMiLCJwaG9uZSI6IjEyMyIsInN0YXRlIjowfSwib3JkZXJzbGlzdCI6eyIyIjp7InN0YXRlIjoxLCJnb29kcyI6IjEyMyIsImNvbXBhbnkiOiIyMzQ1IiwicHJpY2UiOjEyMy4wLCJjbGlja251bSI6NCwibnVtIjowLCJpZCI6MiwicGljbmFtZSI6IjE1MjQzNDMxMTQuMjMyNTkyOC5qcGciLCJzdG9yZSI6MTIzLCJ0eXBlaWQiOjMsIm0iOjF9fSwidmVyaWZ5Y29kZSI6IjMwNDciLCJ0b3RhbCI6MTIzLjAsInZpcHVzZXIiOnsidXNlcm5hbWUiOiIxMjMiLCJwYXNzd29yZCI6IjIwMmNiOTYyYWM1OTA3NWI5NjRiMDcxNTJkMjM0YjcwIiwiaWQiOjQsInN0YXRlIjowLCJuYW1lIjoiMTIzIiwiYWRkcmVzcyI6IjEyMyIsInBob25lIjoiMTIzIiwiZW1haWwiOiIxMjMifX0=','2018-05-12 15:58:49');

/*Table structure for table `goods` */

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `typeid` int(11) unsigned NOT NULL,
  `goods` varchar(32) NOT NULL,
  `company` varchar(50) DEFAULT NULL,
  `content` text,
  `price` double(6,2) unsigned NOT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `store` int(11) unsigned NOT NULL DEFAULT '0',
  `num` int(11) unsigned NOT NULL DEFAULT '0',
  `clicknum` int(11) unsigned NOT NULL DEFAULT '0',
  `state` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `typeid` (`typeid`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `goods` */

insert  into `goods`(`id`,`typeid`,`goods`,`company`,`content`,`price`,`picname`,`store`,`num`,`clicknum`,`state`,`addtime`) values (6,6,'wtert','wert','wrtertertewrt',45.00,'1523416690.8561788.jpg',345,0,10,1,'2018-04-21 20:42:59'),(2,3,'123','2345','123123',123.00,'1523416625.352381.jpg',123,0,5,1,'2018-04-21 15:43:12'),(4,7,'6426','36','                    dfa',274.00,'1523416548.696832.jpg',77,0,2,1,'2018-04-21 16:00:15'),(5,8,'456aa','456','35463456',456.00,'1523416469.7021515.jpg',456,0,1,1,'2018-04-21 16:06:13'),(7,5,'wertwert','wertwert','ertu4y345y',245.00,'1523268691.237927.jpg',546,0,1,1,'2018-04-21 20:43:20'),(1,3,'连衣裙','香奈儿','香奈儿的连衣裙',380.00,'1523268599.5389268.jpg',20,0,0,1,'2018-04-09 10:09:59'),(8,7,'456354','2432','<p>3456</p>',435.00,'1524944703.0423374.jpg',354,0,0,1,'2018-04-28 19:45:03'),(9,7,'2345','325','<p>324</p>',463.00,'1524944718.2400918.jpg',5634,0,0,1,'2018-04-28 19:45:18'),(10,7,'245','1234','<p>3245</p>',1234.00,'1524944731.4028432.jpg',2346,0,0,1,'2018-04-28 19:45:31'),(11,9,'4536','3456','<p>34563</p>',3456.00,'1524945005.9417977.jpg',3456,0,0,1,'2018-04-28 19:50:06'),(12,7,'34523','2345','<p>大夫都说</p>',2345.00,'1524945064.0038624.jpg',234,0,0,1,'2018-04-28 19:51:04');

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) unsigned DEFAULT NULL,
  `linkman` varchar(32) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `total` double(8,2) unsigned DEFAULT NULL,
  `state` tinyint(1) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `orders` */

insert  into `orders`(`id`,`uid`,`linkman`,`address`,`code`,`phone`,`addtime`,`total`,`state`) values (1,4,'123','123','','123','2018-04-26 13:27:13',2456.00,3);

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT '0',
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `type` */

insert  into `type`(`id`,`name`,`pid`,`path`) values (1,'服装',0,'0,'),(2,'数码',0,'0,'),(3,'数码相机',2,'0,2,'),(4,'食品',0,'0'),(5,'电脑',2,'0,2,'),(6,'女装',1,'0,1,'),(7,'儿童装',1,'0,1,'),(8,'手机',3,'0,2,3,'),(9,'男装',1,'0,1,');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `password` char(32) NOT NULL,
  `sex` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `state` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`name`,`password`,`sex`,`address`,`code`,`phone`,`email`,`state`,`addtime`) values (9,'135','135','7f1de29e6da19d22b51c68001e7e0e54',0,'135','135','135','135',1,'2018-04-21 17:03:34'),(10,'abs','abb','202cb962ac59075b964b07152d234b70',1,'asdf','a223','1243','asdf',1,'2018-04-21 22:03:01'),(4,'123','123','202cb962ac59075b964b07152d234b70',1,'123','123','12345678','123',1,'2018-04-28 16:37:41'),(5,'456','456','81dc9bdb52d04dc20036dbd8313ed055',0,'456','456','456','568',1,'2018-04-20 16:49:04'),(6,'kurt','admin','202cb962ac59075b964b07152d234b70',1,NULL,NULL,NULL,NULL,0,NULL),(7,'678','678','9fe8593a8a330607d76796b35c64c600',1,'678','678','678','678',1,'2018-04-21 13:49:15'),(8,'567','567','99c5e07b4d5de9d18c350cdf64c5aa3d',0,'567','567','567','567',1,'2018-04-21 13:49:33'),(11,'rth','123','577ef1154f3240ad5b9b413aa7346a1e',0,'2145','234','5g','ret',1,'2018-04-21 22:36:20'),(12,'chenlihai','','202cb962ac59075b964b07152d234b70',1,'','','','',1,'2018-04-28 13:35:10'),(13,'chenwi','','202cb962ac59075b964b07152d234b70',1,'','','','',1,'2018-04-28 13:36:59');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
