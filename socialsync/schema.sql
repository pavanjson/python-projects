-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: socialsync_db
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add follow',7,'add_follow'),(26,'Can change follow',7,'change_follow'),(27,'Can delete follow',7,'delete_follow'),(28,'Can view follow',7,'view_follow'),(29,'Can add post',8,'add_post'),(30,'Can change post',8,'change_post'),(31,'Can delete post',8,'delete_post'),(32,'Can view post',8,'view_post'),(33,'Can add like',9,'add_like'),(34,'Can change like',9,'change_like'),(35,'Can delete like',9,'delete_like'),(36,'Can view like',9,'view_like'),(37,'Can add comment',10,'add_comment'),(38,'Can change comment',10,'change_comment'),(39,'Can delete comment',10,'delete_comment'),(40,'Can view comment',10,'view_comment'),(41,'Can add profile',11,'add_profile'),(42,'Can change profile',11,'change_profile'),(43,'Can delete profile',11,'delete_profile'),(44,'Can view profile',11,'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$EE8LRgtYij59aADT33JrEN$s7JZIQOnLIOJzQizWrVCo47G6y2kAlFF5HHq7g29VVU=','2025-04-02 16:00:46.999197',0,'Sahana','','','',0,1,'2025-03-28 16:37:48.538324'),(2,'pbkdf2_sha256$870000$k6obg6X1xWrtBl1ShcgEmz$Q4h+g6d/FAqh+eiaPNn9NEhymumY4kb3uheGEYaZmQM=','2025-04-02 08:11:53.754072',0,'Dhruthi','','','',0,1,'2025-03-28 18:03:31.214887'),(3,'pbkdf2_sha256$870000$DTSAqj3pSv0cY0JfO6G8xF$b0uE9BLldll9cguUlo58lEYa7+EjkE608RL5ZTTf9lQ=','2025-03-29 05:06:52.812456',1,'admin','','','admin@gmail.com',1,1,'2025-03-29 05:06:20.280385'),(4,'pbkdf2_sha256$870000$60S6GK0ElznJGfMgmyLfSl$YSourPJMJqKAUIwCvZe72JytCoMEgIJ4QHfHX4yer8c=','2025-04-02 05:32:53.923874',0,'Janu','','','janu@gmail.com',0,1,'2025-04-02 05:32:35.741210'),(5,'pbkdf2_sha256$870000$ZB1WesUWz3n8Q2QY6ybGwn$ivtBsBir5tb/Pv6HZLIZDvSlk41nC1knKFJ99ofUgT8=','2025-04-02 10:26:48.133392',0,'Bharath','','','',0,1,'2025-04-02 10:26:33.696293'),(6,'pbkdf2_sha256$870000$tvdgY80QtnFGjUd99370UB$yS3HZiqdrERCQ5d0s/O3GXY3K6w9J+mMafwReAyD/k0=','2025-04-02 15:26:15.356202',0,'Shreya','','','shreya@gmail.com',0,1,'2025-04-02 12:33:44.845935');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_comment`
--

DROP TABLE IF EXISTS `core_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `post_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_comment_user_id_a9a9430c_fk_auth_user_id` (`user_id`),
  KEY `core_comment_post_id_a75a789c_fk_core_post_id` (`post_id`),
  CONSTRAINT `core_comment_post_id_a75a789c_fk_core_post_id` FOREIGN KEY (`post_id`) REFERENCES `core_post` (`id`),
  CONSTRAINT `core_comment_user_id_a9a9430c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_comment`
--

LOCK TABLES `core_comment` WRITE;
/*!40000 ALTER TABLE `core_comment` DISABLE KEYS */;
INSERT INTO `core_comment` VALUES (1,'good','2025-03-28 18:13:43.104513',2,1),(2,'looks good','2025-04-02 06:05:28.198724',1,3);
/*!40000 ALTER TABLE `core_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_follow`
--

DROP TABLE IF EXISTS `core_follow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_follow` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `follower_id` int NOT NULL,
  `following_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_follow_follower_id_695d5f81_fk_auth_user_id` (`follower_id`),
  KEY `core_follow_following_id_e468b475_fk_auth_user_id` (`following_id`),
  CONSTRAINT `core_follow_follower_id_695d5f81_fk_auth_user_id` FOREIGN KEY (`follower_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `core_follow_following_id_e468b475_fk_auth_user_id` FOREIGN KEY (`following_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_follow`
--

LOCK TABLES `core_follow` WRITE;
/*!40000 ALTER TABLE `core_follow` DISABLE KEYS */;
INSERT INTO `core_follow` VALUES (1,2,1),(7,1,4),(8,1,2),(9,1,3),(11,1,6);
/*!40000 ALTER TABLE `core_follow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_like`
--

DROP TABLE IF EXISTS `core_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_like` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `post_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_like_user_id_0580bca0_fk_auth_user_id` (`user_id`),
  KEY `core_like_post_id_83b37050_fk_core_post_id` (`post_id`),
  CONSTRAINT `core_like_post_id_83b37050_fk_core_post_id` FOREIGN KEY (`post_id`) REFERENCES `core_post` (`id`),
  CONSTRAINT `core_like_user_id_0580bca0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_like`
--

LOCK TABLES `core_like` WRITE;
/*!40000 ALTER TABLE `core_like` DISABLE KEYS */;
INSERT INTO `core_like` VALUES (2,2,1);
/*!40000 ALTER TABLE `core_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_post`
--

DROP TABLE IF EXISTS `core_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `video` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_post_user_id_ae5590f8_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_post_user_id_ae5590f8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_post`
--

LOCK TABLES `core_post` WRITE;
/*!40000 ALTER TABLE `core_post` DISABLE KEYS */;
INSERT INTO `core_post` VALUES (1,'Choco chips','posts/Chocolate_Chip_Cookies.jpeg','2025-03-28 18:02:12.079163',1,NULL),(2,'mango','posts/Mango_Smoothie.jpeg','2025-03-28 18:04:11.822751',2,NULL),(3,'Mango','posts/Mango_Smoothie_jEwtFZ1.jpeg','2025-04-02 05:37:07.714570',4,NULL),(5,'Pizza','posts/Margherita_Pizz.jpeg','2025-04-02 10:24:59.415960',1,NULL),(7,'video 1','','2025-04-02 12:50:22.808123',6,'post_videos/video1_DnAFg6t.mp4'),(8,'video2','','2025-04-02 12:54:37.664668',6,'post_videos/video2.mp4'),(9,'Vidoe1','','2025-04-02 15:24:45.500757',1,'post_videos/video1_odxWlSA.mp4');
/*!40000 ALTER TABLE `core_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_profile`
--

DROP TABLE IF EXISTS `core_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bio` longtext NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `core_profile_user_id_bf8ada58_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_profile`
--

LOCK TABLES `core_profile` WRITE;
/*!40000 ALTER TABLE `core_profile` DISABLE KEYS */;
INSERT INTO `core_profile` VALUES (1,'','profile_pics/default.jpg',1),(2,'','profile_pics/default.png',2),(3,'','profile_pics/default.png',4);
/*!40000 ALTER TABLE `core_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'core','comment'),(7,'core','follow'),(9,'core','like'),(8,'core','post'),(11,'core','profile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-26 13:28:17.856908'),(2,'auth','0001_initial','2025-03-26 13:28:19.012017'),(3,'admin','0001_initial','2025-03-26 13:28:19.191891'),(4,'admin','0002_logentry_remove_auto_add','2025-03-26 13:28:19.203206'),(5,'admin','0003_logentry_add_action_flag_choices','2025-03-26 13:28:19.214421'),(6,'contenttypes','0002_remove_content_type_name','2025-03-26 13:28:19.333028'),(7,'auth','0002_alter_permission_name_max_length','2025-03-26 13:28:19.411255'),(8,'auth','0003_alter_user_email_max_length','2025-03-26 13:28:19.445350'),(9,'auth','0004_alter_user_username_opts','2025-03-26 13:28:19.451580'),(10,'auth','0005_alter_user_last_login_null','2025-03-26 13:28:19.529629'),(11,'auth','0006_require_contenttypes_0002','2025-03-26 13:28:19.532566'),(12,'auth','0007_alter_validators_add_error_messages','2025-03-26 13:28:19.544756'),(13,'auth','0008_alter_user_username_max_length','2025-03-26 13:28:19.643547'),(14,'auth','0009_alter_user_last_name_max_length','2025-03-26 13:28:19.724246'),(15,'auth','0010_alter_group_name_max_length','2025-03-26 13:28:19.747488'),(16,'auth','0011_update_proxy_permissions','2025-03-26 13:28:19.757889'),(17,'auth','0012_alter_user_first_name_max_length','2025-03-26 13:28:19.890703'),(18,'core','0001_initial','2025-03-26 13:28:20.579969'),(19,'sessions','0001_initial','2025-03-26 13:28:20.634739'),(20,'core','0002_alter_profile_profile_pic','2025-03-29 04:48:00.932456'),(21,'core','0003_post_video_alter_post_content_alter_post_image','2025-04-02 12:46:21.421750');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('55xit4yo3ogtxvjglzz6wgfvbb7ll2rl','.eJxVjMsOwiAUBf-FtSG8Hy7d9xvIBS5SNZCUdmX8d9ukC92emTlvEmBba9gGLmHO5Eo4ufxuEdIT2wHyA9q909TbusyRHgo96aBTz_i6ne7fQYVR91ok0KA0s6pwVVh2XCZhtAWzA56VidEm4UAjgudCaV5AFq9cROYdSvL5AtsqN8g:1u007c:arb5l0aoH7ky5AKrWZ-Q_eKndwLJPHFjF2d_KXJbsic','2025-04-16 15:35:20.480619'),('6jve4jwzzanmdlaa9m9xlttogcv56r5f','.eJxVjMsOwiAUBf-FtSG8Hy7d9xvIBS5SNZCUdmX8d9ukC92emTlvEmBba9gGLmHO5Eo4ufxuEdIT2wHyA9q909TbusyRHgo96aBTz_i6ne7fQYVR91ok0KA0s6pwVVh2XCZhtAWzA56VidEm4UAjgudCaV5AFq9cROYdSvL5AtsqN8g:1u00WF:tAw5mkbbPrmPJZ89rHkFmjSiZemDi63VhVpH7h8l8DY','2025-04-16 16:00:47.010200'),('t55a08vtcqxm77g5htctfd9wawqrthab','.eJxVjMsOwiAUBf-FtSG8Hy7d9xvIBS5SNZCUdmX8d9ukC92emTlvEmBba9gGLmHO5Eo4ufxuEdIT2wHyA9q909TbusyRHgo96aBTz_i6ne7fQYVR91ok0KA0s6pwVVh2XCZhtAWzA56VidEm4UAjgudCaV5AFq9cROYdSvL5AtsqN8g:1tzux6:whNOw5h8ZpfYbho5-eg1mGH3Cv9slBkpimmD_dfZwdo','2025-04-16 10:04:08.366699'),('x1bcgg0k0emvx4qd4wepuwchvpncpjx2','.eJxVjDsOwjAQBe_iGllZZ_GHkj5niNZeLw4gR4qTCnF3iJQC2jcz76VG2tYybi0v48TqokCdfrdI6ZHrDvhO9TbrNNd1maLeFX3QpoeZ8_N6uH8HhVr51s4Dmxj7XoJ4i4kwOcrBIwoEMSZ1YLsk0lvmjk04Awk6CzGAQxNAvT_ldTd6:1tyEDs:sQIhWkqrcDpG6wnQTpIYJGIWsH6pRE8eji1OAPNDzwc','2025-04-11 18:14:28.368560'),('z8whpfxiozsc7vi8x6k9fkekhrkagwnw','.eJxVjMsOwiAQRf-FtSE8ChSX7vsNZJgZpWogKe3K-O_apAvd3nPOfYkE21rS1nlJM4mzsOL0u2XAB9cd0B3qrUlsdV3mLHdFHrTLqRE_L4f7d1Cgl2_N3sAVTIDRD4hovVLoRm_ygI4ZIqDhqNkG1I5DjOSUQc0K85CJIoj3B_riOLg:1tyOPE:0Yhbdp8RzR3uZsMTVHseOVBaYci_g3aA3eJq5lNRrRQ','2025-04-12 05:06:52.825338');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'socialsync_db'
--

--
-- Dumping routines for database 'socialsync_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-02 21:46:37
