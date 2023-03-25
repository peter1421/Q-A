CREATE DATABASE  IF NOT EXISTS `qa` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `qa`;
-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: qa
-- ------------------------------------------------------
-- Server version	5.7.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` int(11) NOT NULL,
  `answer` varchar(255) NOT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  `pkey` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`pkey`),
  KEY `id_idx` (`id`),
  CONSTRAINT `id` FOREIGN KEY (`id`) REFERENCES `question` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (4,'哦，窩以前元神豚現在原黑了，所以呢？','2023-03-25 12:37:01',89),(7,'哦，窩以前元神豚現在原黑了，所以呢？','2023-03-25 12:37:22',90),(2,'哦，窩以前元神豚現在原黑了，所以呢？哦，窩以前元神豚現在原黑了，所以呢？哦，窩以前元神豚現在原黑了，所以呢？','2023-03-25 12:38:42',91),(8,'沒有一種可能，更多的原黑沒在追最新情報呢？','2023-03-25 12:44:44',92),(8,'沒有一種可能，更多的原黑沒在追最新情報呢？','2023-03-25 12:44:47',93),(8,'我說真的\n原黑還要去追第一手情報\n\n一有預告逐幀分析\n定格觀看有沒有什麼物件哪一幀是抄襲的\n對比原神廚花的心力\n原黑說不定才是最愛原神的人\n\n版上一堆原神廚可能只是饞人家身子罷了\n好好反省','2023-03-25 12:44:54',94),(8,'???','2023-03-25 12:45:28',95),(4,'33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333','2023-03-25 12:47:20',96),(6,'333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333','2023-03-25 12:48:08',97),(6,'33','2023-03-25 12:50:22',98),(7,'33','2023-03-25 12:50:36',99),(7,'33','2023-03-25 12:50:38',100),(7,'33','2023-03-25 12:50:40',101),(7,'33','2023-03-25 12:51:21',102),(4,'dfsdf','2023-03-25 13:10:39',103),(5,'sa','2023-03-25 13:11:12',104),(6,'aaa','2023-03-25 13:11:44',105),(4,'2323','2023-03-25 13:12:06',106),(4,'dfgdfgdfg','2023-03-25 13:12:24',107),(6,'222','2023-03-25 13:22:22',108),(5,'我說真的\n原黑還要去追第一手情報\n\n一有預告逐幀分析\n定格觀看有沒有什麼物件哪一幀是抄襲的\n對比原神廚花的心力\n原黑說不定才是最愛原神的人\n\n版上一堆原神廚可能只是饞人家身子罷了\n好好反省\n\n','2023-03-25 13:23:25',109),(5,'ˇˇˇ','2023-03-25 13:25:29',110),(1,'ss','2023-03-25 13:26:33',111),(10,'323423','2023-03-25 13:29:10',112),(1,'323423','2023-03-25 13:29:15',113),(1,'我說真的\n原黑還要去追第一手情報\n\n一有預告逐幀分析\n定格觀看有沒有什麼物件哪一幀是抄襲的\n對比原神廚花的心力\n原黑說不定才是最愛原神的人\n\n版上一堆原神廚可能只是饞人家身子罷了\n好好反省','2023-03-25 13:29:30',114),(2,'我說真的\n原黑還要去追第一手情報\n\n一有預告逐幀分析\n定格觀看有沒有什麼物件哪一幀是抄襲的\n對比原神廚花的心力\n原黑說不定才是最愛原神的人\n\n版上一堆原神廚可能只是饞人家身子罷了\n好好反省','2023-03-25 13:29:40',115),(3,'我說真的\n原黑還要去追第一手情報\n\n一有預告逐幀分析\n定格觀看有沒有什麼物件哪一幀是抄襲的\n對比原神廚花的心力\n原黑說不定才是最愛原神的人\n\n版上一堆原神廚可能只是饞人家身子罷了\n好好反省','2023-03-25 13:29:46',116),(9,'我說真的\n原黑還要去追第一手情報\n\n一有預告逐幀分析\n定格觀看有沒有什麼物件哪一幀是抄襲的\n對比原神廚花的心力\n原黑說不定才是最愛原神的人\n\n版上一堆原神廚可能只是饞人家身子罷了\n好好反省','2023-03-25 13:29:58',117);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip`
--

DROP TABLE IF EXISTS `ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip` (
  `ip` varchar(45) NOT NULL,
  `time` datetime DEFAULT NULL,
  `post` int(11) NOT NULL,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip`
--

LOCK TABLES `ip` WRITE;
/*!40000 ALTER TABLE `ip` DISABLE KEYS */;
INSERT INTO `ip` VALUES ('0.0.0.0',NULL,2),('111.83.25.212',NULL,73);
/*!40000 ALTER TABLE `ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'1+3=?',NULL,'2023-03-23 13:49:42'),(2,'5+5=?','aad@gmail.com','2023-03-23 13:49:42'),(3,'44-33=?','dd@gmail.com','2023-03-23 13:49:42'),(4,'44*8=?','asd@gmail.com','2023-03-23 13:49:42'),(5,'66/3=?','rtrt@gmail.com','2023-03-23 13:49:42'),(6,'88-9=?','aaaa@gmail.com','2023-03-23 13:49:42'),(7,'99-9','aa@gmail.com','2023-03-23 22:24:26'),(8,'dd@gamail.com','dd@gamail.com','2023-03-23 23:55:51'),(9,'ttytry@fsdf','ttytry@fsdf','2023-03-24 00:11:00'),(10,'ssda','sdasd@fdsfsdf','2023-03-24 19:42:36'),(11,'dfsdfsdfweffffffffffffffffffffffffffffffffffffffff','fffwef@sdfsdfsdfsdfsdf','2023-03-25 13:14:18');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-25 13:36:49
