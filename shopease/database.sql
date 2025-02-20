-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: shopease_db
-- ------------------------------------------------------
-- Server version	8.0.41

create database shopease_db;
use shopease_db;

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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add product',7,'add_product'),(26,'Can change product',7,'change_product'),(27,'Can delete product',7,'delete_product'),(28,'Can view product',7,'view_product'),(29,'Can add order item',8,'add_orderitem'),(30,'Can change order item',8,'change_orderitem'),(31,'Can delete order item',8,'delete_orderitem'),(32,'Can view order item',8,'view_orderitem'),(33,'Can add order',9,'add_order'),(34,'Can change order',9,'change_order'),(35,'Can delete order',9,'delete_order'),(36,'Can view order',9,'view_order'),(37,'Can add category',10,'add_category'),(38,'Can change category',10,'change_category'),(39,'Can delete category',10,'delete_category'),(40,'Can view category',10,'view_category');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$tc5yyQkTnxuYYzdfzvv9UI$dXUuyEQgEwJ5otMNSpHnxRknJ3upDvOk8lCBl0plOHo=',NULL,1,'admin','','','vinay@skyllx.com',1,1,'2025-02-19 18:39:41.327458'),(2,'pbkdf2_sha256$870000$6DiCl64qkDefdifxDK6oS8$s7WEJ1iFyQdd0AmASMmnSwhscAWmksxYe6VilzFZxJA=','2025-02-20 21:30:18.540219',1,'vinayhp','','','vinay@skyllx.com',1,1,'2025-02-20 06:24:43.269800');
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-02-20 06:49:38.258432','1','Amazon Echo Dot (5th Gen)',1,'[{\"added\": {}}]',7,2),(2,'2025-02-20 07:08:07.329016','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',1,'[{\"added\": {}}]',7,2),(3,'2025-02-20 19:37:12.947989','3','ELLIPSE Women’s Stylish Solid Full Sleeves Jacket',1,'[{\"added\": {}}]',7,2),(4,'2025-02-20 19:39:01.892017','4','Allen Solly Men\'s Regular Fit Polo',1,'[{\"added\": {}}]',7,2),(5,'2025-02-20 21:08:01.288394','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,2),(6,'2025-02-20 21:08:12.529112','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,2),(7,'2025-02-20 21:08:50.286111','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,2),(8,'2025-02-20 21:09:12.018494','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,2),(9,'2025-02-20 21:22:15.634992','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',2,'[]',7,2),(10,'2025-02-20 21:22:19.406746','2','amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)',2,'[]',7,2),(11,'2025-02-20 21:24:27.088901','5','Raymond Men Slim Fit Structure Pattern Poly Viscose Blend Pleatless Formal Trouser',1,'[{\"added\": {}}]',7,2),(12,'2025-02-20 21:31:02.781568','6','ASIAN Men\'s Wonder-13 Sports Running Shoes',1,'[{\"added\": {}}]',7,2),(13,'2025-02-20 21:33:05.005940','7','HP 15, 13th Gen Intel Core i5-1334U, 16GB DDR4, 512GB SSD',1,'[{\"added\": {}}]',7,2),(14,'2025-02-20 21:34:32.299447','8','boAt Airdopes 91 Prime',1,'[{\"added\": {}}]',7,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(10,'store','category'),(9,'store','order'),(8,'store','orderitem'),(7,'store','product');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-19 17:20:00.309986'),(2,'auth','0001_initial','2025-02-19 17:20:01.619197'),(3,'admin','0001_initial','2025-02-19 17:20:01.928495'),(4,'admin','0002_logentry_remove_auto_add','2025-02-19 17:20:01.949822'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-19 17:20:01.967766'),(6,'contenttypes','0002_remove_content_type_name','2025-02-19 17:20:02.251470'),(7,'auth','0002_alter_permission_name_max_length','2025-02-19 17:20:02.396127'),(8,'auth','0003_alter_user_email_max_length','2025-02-19 17:20:02.454884'),(9,'auth','0004_alter_user_username_opts','2025-02-19 17:20:02.473595'),(10,'auth','0005_alter_user_last_login_null','2025-02-19 17:20:02.633819'),(11,'auth','0006_require_contenttypes_0002','2025-02-19 17:20:02.639428'),(12,'auth','0007_alter_validators_add_error_messages','2025-02-19 17:20:02.659925'),(13,'auth','0008_alter_user_username_max_length','2025-02-19 17:20:02.854543'),(14,'auth','0009_alter_user_last_name_max_length','2025-02-19 17:20:03.024658'),(15,'auth','0010_alter_group_name_max_length','2025-02-19 17:20:03.070196'),(16,'auth','0011_update_proxy_permissions','2025-02-19 17:20:03.090847'),(17,'auth','0012_alter_user_first_name_max_length','2025-02-19 17:20:03.281678'),(18,'sessions','0001_initial','2025-02-19 17:20:03.348529'),(19,'store','0001_initial','2025-02-19 18:39:08.764283'),(20,'store','0002_category_product_stock','2025-02-20 19:50:12.697518');
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
INSERT INTO `django_session` VALUES ('ainjzn9d51er0qrs8u3y9tg1buf1yq1u','.eJxVjEEOwiAQRe_C2pAyHaC4dO8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3EWIE6_W6D44LqDdKd6azK2ui5zkLsiD9rltSV-Xg7376BQL9_aEgFG5EFzNoQmj6ApK6QQRhudHtII4Fg5nNDQZBRpl8gYBw60Dla8P-MlN0g:1tlE7e:H6QsQUuND2F3r5ljz9k2XFTZf_RbEF2aceYfD7QObp8','2025-03-06 21:30:18.544744'),('cgzqogohn1v6ddsut2hja8ymdelaedja','.eJxVjDsOgzAQBe-ydWTB4jWYMj1nQM8fAkkEEjYV4u4JEg3tm5m3k8eaqd2PB_XY8thvKa79FKglptvm4D9xPkF4Y34tyi9zXienTkVdNKluCfH7vNzbwYg0_usaYO11LCQOBtoMFQuGUsO5qvZWilAx21ha3WiDxpQQG2CMZcsirqbjByp4OpQ:1tl1ip:a3vhMARUsLS9TAxP8QPrZPWqe2afyUNRiteSNjgxePo','2025-03-06 08:15:51.524013'),('wxijtw0forns89bcrvc496yo6pi1zhyz','.eJxVjEEOwiAQRe_C2pAyHaC4dO8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3EWIE6_W6D44LqDdKd6azK2ui5zkLsiD9rltSV-Xg7376BQL9_aEgFG5EFzNoQmj6ApK6QQRhudHtII4Fg5nNDQZBRpl8gYBw60Dla8P-MlN0g:1tl1wR:O9KiKbb4_3uoMuAaezTpiII9cJ7RCn9-dCSudrp-4tA','2025-03-06 08:29:55.125690');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_category`
--

DROP TABLE IF EXISTS `store_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_category`
--

LOCK TABLES `store_category` WRITE;
/*!40000 ALTER TABLE `store_category` DISABLE KEYS */;
INSERT INTO `store_category` VALUES (1,'Electronics','electronics'),(2,'Fashion','fashion'),(3,'Home Appliances','home_appliances');
/*!40000 ALTER TABLE `store_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_order`
--

DROP TABLE IF EXISTS `store_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `is_paid` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_order_user_id_ae5f7a5f_fk_auth_user_id` (`user_id`),
  CONSTRAINT `store_order_user_id_ae5f7a5f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_order`
--

LOCK TABLES `store_order` WRITE;
/*!40000 ALTER TABLE `store_order` DISABLE KEYS */;
INSERT INTO `store_order` VALUES (1,'2025-02-20 06:50:11.048201',1,2),(2,'2025-02-20 07:56:10.798913',1,2),(3,'2025-02-20 08:15:51.504286',1,2),(4,'2025-02-20 08:29:09.218130',1,2),(5,'2025-02-20 21:18:49.119550',1,2),(6,'2025-02-20 21:21:52.689152',1,2);
/*!40000 ALTER TABLE `store_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_orderitem`
--

DROP TABLE IF EXISTS `store_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_orderitem_order_id_acf8722d_fk_store_order_id` (`order_id`),
  KEY `store_orderitem_product_id_f2b098d4_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_orderitem_order_id_acf8722d_fk_store_order_id` FOREIGN KEY (`order_id`) REFERENCES `store_order` (`id`),
  CONSTRAINT `store_orderitem_product_id_f2b098d4_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  CONSTRAINT `store_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_orderitem`
--

LOCK TABLES `store_orderitem` WRITE;
/*!40000 ALTER TABLE `store_orderitem` DISABLE KEYS */;
INSERT INTO `store_orderitem` VALUES (1,1,1,1),(2,1,2,1),(3,1,3,2),(4,1,4,1),(5,1,5,2),(6,1,6,2);
/*!40000 ALTER TABLE `store_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_product`
--

DROP TABLE IF EXISTS `store_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `stock` int NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_store_product_category` (`category_id`),
  CONSTRAINT `fk_store_product_category` FOREIGN KEY (`category_id`) REFERENCES `store_category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_product`
--

LOCK TABLES `store_product` WRITE;
/*!40000 ALTER TABLE `store_product` DISABLE KEYS */;
INSERT INTO `store_product` VALUES (1,'Amazon Echo Dot (5th Gen)','Smart speaker with Bigger sound, Motion Detection, Temperature Sensor, Alexa and Bluetooth| Black\r\n\r\n5th (Latest) Generation Echo Dot with Alexa-The best sounding Echo Dot yet! With deeper bass and clearer vocals than all previous generations.\r\nJust ask Alexa to play music from Amazon Music, Spotify, Jio Saavn, Apple Music.(some apps may require subscription)\r\nVoice control Alexa compatible smart appliances like lights, ACs, TVs, geysers. Extend the experience to non-smart appliances using smart plugs (to be purchased separately)\r\nAutomatically turn on light when you enter the room or switch on the AC when it gets hot using in-built motion detection and temperature sensor. Set these experiences using routines feature in Alexa app.\r\nManage your day better by just asking Alexa to set reminders, pay bills, add items to shopping list and much more. Alexa can speak English and Hindi.\r\nPause/resume music, snooze alarms, dismiss timers with just a tap.\r\nUse as a standalone speaker or pair your phone to use it as a Bluetooth speaker.\r\nEcho Dot comes with multiple privacy controls, including a mic off button.',5499.00,'products/echodot.jpg',0,1),(2,'amazon basics Height Adjustable 5-Shelves Heavy Duty Rack - Black Chrome Finish (Steel)','Material	steel\r\nRoom Type	Office\r\nNumber of Shelves	4\r\nSpecial Feature	Adjustable,Durable,Heavy,Heavy Duty\r\nProduct Dimensions	35.6D x 91.4W x 182.9H Centimeters\r\nStyle	Chrome Finish\r\nAge Range (Description)	Adult\r\nBrand	amazon basics\r\nProduct Care Instructions	Dry_Clean_Only\r\nSize	3 Shelves',4149.00,'products/rack.jpg',0,3),(3,'ELLIPSE Women’s Stylish Solid Full Sleeves Jacket','Product details\r\nMaterial compositionPolyster\r\nStyleJacket\r\nFit typeRegular\r\nLengthStandard Length\r\nNeck styleHooded Neck\r\nPatternSolid\r\nCountry of OriginIndia\r\nAbout this item\r\nCare Instructions: Machine Wash\r\nFit Type: Regular\r\nThe jacket is equipped with a reliable zipper closure, ensuring a secure fit and added protection against chilly winds.\r\nIts stylish design makes it suitable for various occasions, while functional pockets offer secure storage.\r\nAdditional Information\r\nManufacturerEllipse\r\nPackerELLIPSE FASHIONS\r\nItem Weight760 g\r\nItem Dimensions LxWxH18 x 28 x 7 Centimeters\r\nNet Quantity1.00 count\r\nGeneric NameWinter Jacket',1135.00,'products/ELLIPSE_Womens_Stylish_Solid_Full_Sleeves_Jacket.jpg',0,2),(4,'Allen Solly Men\'s Regular Fit Polo','Product details\r\nPatternSolid\r\nFit typeRegular Fit\r\nSleeve typeHalf Sleeve\r\nCollar stylePolo Collar\r\nLengthStandard Length\r\nStyleWestern\r\nCountry of OriginIndia\r\nAbout this item\r\nNeck : Polo Neck\r\nFit : Regular Fit\r\nMaterial : 60% Cotton and 40% Polyester\r\nOccasion : Casual\r\nPattern : Solid\r\nBrand: Allen Solly\r\nAdditional Information\r\nManufacturerAllen Solly, Aditya Birla Fashion and Retail Limited. Kh No. 118/110/1, Building 2, Divyasree Technopolis, Yemalur Post, Off HAL Airport Road, Bengaluru-560037\r\nPackerAditya Birla Fashion and Retail Limited\r\nImporterAditya Birla Fashion and Retail Limited\r\nItem Weight200 g\r\nItem Dimensions LxWxH25 x 20 x 2 Centimeters\r\nGeneric NamePolo',712.00,'products/Allen_Solly_Mens_Regular_Fit_Polo.jpg',0,2),(5,'Raymond Men Slim Fit Structure Pattern Poly Viscose Blend Pleatless Formal Trouser','Product details\r\nMaterial typePolyester Blend\r\nLengthStandard Length\r\nStyleRaymond Men\'s Slim Fit Polyester Blend Structure Pattern Flat Front Dark Blue Trouser\r\nClosure typeZipper\r\nOccasion typeFormal\r\nCare instructionsMachine Wash\r\nCountry of OriginIndia\r\nAbout this item\r\nFabric : Pol84%Vsc14%Lyc2%\r\nColor : Dark Blue\r\nFront Style : Flat Front\r\nPattern : Structure Pattern\r\nSupport: support@myraymond.com\r\nAdditional Information\r\nManufacturerRUDEUM INTERNATIONAL LLP, RUDEUM INTERNATIONAL LLP, 111/113, GIRI SHIKHAR, JB NAGAR, ANDHERI EAST-400059\r\nPackerRUDEUM INTERNATIONAL LLP, 111/113, GIRI SHIKHAR, JB NAGAR, ANDHERI EAST-400059\r\nItem Weight510 g\r\nItem Dimensions LxWxH57 x 40 x 0.5 Centimeters\r\nGeneric NamePants',1149.00,'products/Raymond_Men_Slim_Fit_Structure_Pattern_Poly_Viscose_Blend_Pleatless_Formal_Trouser.jpg',5,2),(6,'ASIAN Men\'s Wonder-13 Sports Running Shoes','Product details\r\nMaterial typeMesh\r\nClosure typeLace-Up\r\nHeel typeFlat\r\nWater resistance levelNot Water Resistant\r\nSole materialEthylene Vinyl Acetate\r\nStyleSneaker\r\nCountry of OriginIndia\r\nAbout this item\r\nLightweight & Breathable : Exclusive design and durable materials every step feels light and breezy. Breathable, free-moving fabrics which adjust according to your foot and creates an astoundingly easy-going experience.\r\nNon Slip & Shockproof : Great engineering strikes a balance in style, made in the potent design and latest fashion trends. Made for long-term wear, with extra emphasis on providing cushion to the feet, removing heel strain.\r\nComfort Sole & Flexible Walk : The outsoles are made by an air cushion, doubling the effect of shock absorption. Besides, these shoes perform excellent in durability and are also slip resistant. It provides push cushioning comfort for foot pain relief and helps relieve pressure while conforming to your every step\r\nAdditional Information\r\nManufacturerASIAN, Asian Footwear Pvt Ltd\r\nPackerAsian Retail Ventures\r\nImporterAsian Retail Ventures\r\nItem Weight670 g\r\nItem Dimensions LxWxH31 x 10 x 21 Centimeters\r\nNet Quantity1.00 count\r\nGeneric NameFirst Walker Shoe',599.00,'products/ASIAN_Mens_Wonder-13_Sports_Running_Shoes.jpg',25,2),(7,'HP 15, 13th Gen Intel Core i5-1334U, 16GB DDR4, 512GB SSD','HP 15, 13th Gen Intel Core i5-1334U, 16GB DDR4, 512GB SSD, (Win 11, Office 21, Silver, 1.59kg), Anti-Glare, 15.6-inch(39.6cm) FHD Laptop, Iris Xe Graphics, FHD Camera, Backlit KB, fd0316TU/fd0315TU\r\n\r\nBrand	HP\r\nModel Name	HP Laptop\r\nScreen Size	15.6 Inches\r\nColour	Silver - MSO 2021\r\nHard Disk Size	512 GB\r\nCPU Model	Intel Core i5\r\nRAM Memory Installed Size	16 GB\r\nOperating System	Windows 11 Home\r\nSpecial Feature	Anti Glare Screen\r\nGraphics Card Description	Integrated\r\nSee more\r\nAbout this item\r\n【10-core 13th Gen Intel Core i5-1334U】Unleash superior performance with a processor optimized for efficiency. Its 12 threads, and 12MB L3 cache offer smooth multitasking and quick response times.\r\n【Intel Iris Xe graphics】Experience dynamic visuals with Intel Iris Xe Graphics, perfect for high-definition video playback, casual gaming, and graphic-intensive tasks.\r\n【High-capacity memory and storage】Work with ease on the 16GB DDR4-3200 MHz RAM. The 512GB PCIe NVMe M.2 SSD provides generous storage, facilitating a smoother user experience.\r\n【Micro-edge display】Experience vivid details on the 15.6-inch, FHD anti-glare display. Revel in the stunning clarity and immersive visuals that elevate your viewing experience.\r\n【Extended battery life】Stay unplugged with a 3-cell, 41Wh battery. HP Fast Charge replenishes up to 50% battery in just 45 minutes, keeping you productive longer.\r\n【Ultra-fast connectivity】Experience seamless connections with Wi-Fi 6 (1x1) and Bluetooth 5.3. It also features a variety of ports including 1 x USB Type-C, 2 x USB Type-A, and 1 x HDMI 1.4b.\r\n【HD conferencing】Engage in clear video calls with HP True Vision 1080p FHD camera with temporal noise reduction and integrated dual array digital mics, ideal for work or catching up with loved ones.',54990.00,'products/HP_15_13th_Gen_Intel_Core_i5-1334U_16GB_DDR4_512GB_SSD.jpg',2,1),(8,'boAt Airdopes 91 Prime','boAt Airdopes 91 Prime, 45HRS Battery, 13mm Drivers, Metallic Finish, Low Latency,ENx Tech, Fast Charge, v5.3 Bluetooth TWS in Ear Earbuds Wireless Earphones with mic (Midnight Black)\r\n\r\nBrand	boAt\r\nColour	Midnight Black\r\nEar Placement	In Ear\r\nForm Factor	True Wireless\r\nModel Name	Airdopes 91\r\nAbout this item\r\n13 mm Drivers with boAt Signature Sound: High-performance 13 mm drivers in the boAt Airdopes 91 Prime TWS Earbuds are your gateway to the audio realm. Feel your favorite tunes come alive with the powerful bass of boAt Signature Sound every time you plug in your Airdopes.\r\n45 Hours of Playtime: Watch live games, listen to podcasts, or work out to your playlist for around 45 hours non-stop with these earbuds. Charge less and enjoy more!\r\n50 ms Latency BEAST Mode: Take out lag from the mix while gaming with BEAST mode. Once activated, the 50 ms low latency syncs virtual frames with power-packed audio for adrenaline-raising gaming sessions.\r\nDual Mics with ENx Technology: Make calls on the go with the ENx-powered dual mics. Join work calls or catch up with friends from the airport lounge, café, metro, etc., without annoying background noise.\r\nASAP Charge: Airdopes 91 Prime is your movie marathon partner for the long haul with its fast charging which lends a whopping 120 minutes of playtime when you charge the earbuds for just 10 minutes.',799.00,'products/boAt_Airdopes_91_Prime.jpg',5,1);
/*!40000 ALTER TABLE `store_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'shopease_db'
--

--
-- Dumping routines for database 'shopease_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-21  3:06:50
