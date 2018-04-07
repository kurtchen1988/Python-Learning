-- MySQL dump 10.13  Distrib 5.5.53, for Win32 (AMD64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	5.5.53

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `abstract` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `uid` int(10) unsigned DEFAULT NULL,
  `pcount` int(10) unsigned DEFAULT '0',
  `flag` tinyint(3) unsigned DEFAULT '0',
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'Background statement','These pages show two examples of typical abstracts from honours theses. Notice that the stages of the abstracts have been labelled, so that you can see the function of each sentence or part-sentence.','These pages show two examples of typical abstracts from honours theses. Notice that the stages of the abstracts have been labelled, so that you can see the function of each sentence or part-sentence.',1,153,2,'2015-04-06 00:00:00'),(2,'Narrowing statement','You can also see that there are differences in the type of information that is included in each abstract, as well as differences in level of detail.','These methods include injection and trenching.',4,142,1,'2016-08-19 00:00:00'),(3,'Elaboration of narrowing',' The spread of antibiotic resistance is aided by mobile elements such as transposons and conjugative plasmids.',' The spread of antibiotic resistance is aided by mobile elements such as transposons and conjugative plasmids.',3,354,2,'2013-02-16 00:00:00'),(4,'Aims','Recently, integrons have been recognised as genetic elements that have the capacity to contribute to the spread of resistance. ','Recently, integrons have been recognised as genetic elements that have the capacity to contribute to the spread of resistance. ',2,142,0,'2017-06-25 00:00:00'),(5,'Extended aim','Integrons constitute an efficient means of capturing gene cassettes and allow expression of encoded resistance.','Integrons constitute an efficient means of capturing gene cassettes and allow expression of encoded resistance.',2,432,2,'2018-03-26 00:00:00'),(6,'Justification of results','The aims of this study were to screen clinical isolates for integrons, characterise gene cassettes and extended spectrum b-lactamase (ESBL) genes. ','The aims of this study were to screen clinical isolates for integrons, characterise gene cassettes and extended spectrum b-lactamase (ESBL) genes. ',5,234,2,'2014-03-26 00:00:00'),(7,'Background statement','Subsequent to this, genetic linkage between ESBL genes and gentamicin resistance was investigated.  ','Subsequent to this, genetic linkage between ESBL genes and gentamicin resistance was investigated.  ',6,214,1,'2014-05-23 00:00:00'),(8,'Narrowing statement','In this study, 41 % of multiple antibiotic resistant bacteria and 79 % of extended-spectrum b-lactamase producing organisms were found to carry either one or two integrons, as detected by PCR.','In this study, 41 % of multiple antibiotic resistant bacteria and 79 % of extended-spectrum b-lactamase producing organisms were found to carry either one or two integrons, as detected by PCR.',8,234,2,'2018-03-26 00:00:00'),(9,'Elaboration of aim',' A novel gene cassette contained within an integron was identified from Stenotrophomonas maltophilia, encoding a protein that belongs to the small multidrug resistance (SMR) family of transporters.',' A novel gene cassette contained within an integron was identified from Stenotrophomonas maltophilia, encoding a protein that belongs to the small multidrug resistance (SMR) family of transporters.',4,345,0,'2015-06-19 00:00:00'),(10,'Methods','pLJ1, a transferable plasmid that was present in 86 % of the extended-spectrum b-lactamase producing collection, was found to harbour an integron carrying aadB, a gene cassette for gentamicin, kanamyc','pLJ1, a transferable plasmid that was present in 86 % of the extended-spectrum b-lactamase producing collection, was found to harbour an integron carrying aadB, a gene cassette for gentamicin, kanamycin and tobramycin resistance and a blaSHV-12 gene for third generation cephalosporin resistance.',6,123,1,'2018-01-05 00:00:00'),(11,'Results','The presence of this plasmid accounts for the gentamicin resistance phenotype that is often associated with organisms displaying an extended-spectrum b-lactamase phenotype.','The presence of this plasmid accounts for the gentamicin resistance phenotype that is often associated with organisms displaying an extended-spectrum b-lactamase phenotype.',7,123,1,'2014-06-12 00:00:00'),(12,'Future applications and research','A review of groundwater remediation in use today shows that new techniques are required that solve the problems of pump and treat, containment and in-situ treatment. ','The presence of this plasmid accounts for the gentamicin resistance phenotype that is often associated with organisms displaying an extended-spectrum b-lactamase phenotype.',8,6354,2,'2010-03-27 00:00:00'),(13,'Future applications and research','A review of groundwater remediation in use today shows that new techniques are required that solve the problems of pump and treat, containment and in-situ treatment. ','A review of groundwater remediation in use today shows that new techniques are required that solve the problems of pump and treat, containment and in-situ treatment. ',2,235,2,'2014-09-23 00:00:00'),(14,'Significance of results','One such technique is the method that involves the use of permeable treatment walls. ','One such technique is the method that involves the use of permeable treatment walls. ',5,263,1,'2013-08-26 00:00:00'),(15,'Future research','Several methods of implementing this remediation strategy have been described.','These methods include injection and trenching.',3,324,0,'2013-06-27 00:00:00');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'zhangsan','zhangsan@qq.com','2015-05-01 00:00:00'),(2,'lisi','lisi@ww.com','2016-05-08 00:00:00'),(3,'wangwu','wangwu@rr.com','2017-06-08 00:00:00'),(4,'zhagojiu','zhagojiu@ff.com','2016-12-08 00:00:00'),(5,'qianliu','qianliu@jj.com','2017-06-08 00:00:00'),(6,'qijiu','qijiu@ww.com','2015-04-15 00:00:00'),(7,'liusan','liusan@qq.com','2018-01-08 00:00:00'),(8,'wangxiao','wangxiao@nn.com','2018-02-08 00:00:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-07 11:44:48
