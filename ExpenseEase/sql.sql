CREATE DATABASE  IF NOT EXISTS `expenseease_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `expenseease_db`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: expenseease_db
-- ------------------------------------------------------
-- Server version	8.0.41

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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add budget',8,'add_budget'),(30,'Can change budget',8,'change_budget'),(31,'Can delete budget',8,'delete_budget'),(32,'Can view budget',8,'view_budget'),(33,'Can add expense',9,'add_expense'),(34,'Can change expense',9,'change_expense'),(35,'Can delete expense',9,'delete_expense'),(36,'Can view expense',9,'view_expense'),(37,'Can add recurring expense',10,'add_recurringexpense'),(38,'Can change recurring expense',10,'change_recurringexpense'),(39,'Can delete recurring expense',10,'delete_recurringexpense'),(40,'Can view recurring expense',10,'view_recurringexpense');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$2jAoKq9cpZIhc7V10WFd1Y$1jXSvep+bD0kjXeFfNDFVPDwUh2gQIYOkgNMyK7a7Kg=','2025-02-23 11:10:11.068152',1,'admin','','','vinay@skyllx.com',1,1,'2025-02-23 10:01:17.319792'),(2,'pbkdf2_sha256$870000$vpiD6EnqnJ2mP2fFENfp7c$s3+PMByGJEY7bt9R5jFLFgAaaM7W4ggAaJgEu0AUrg4=','2025-02-23 10:46:25.237780',0,'admin1','','','',0,1,'2025-02-23 10:46:24.383932');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'tracker','budget'),(7,'tracker','category'),(9,'tracker','expense'),(10,'tracker','recurringexpense');
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
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-23 10:00:47.340044'),(2,'auth','0001_initial','2025-02-23 10:00:48.293473'),(3,'admin','0001_initial','2025-02-23 10:00:48.510344'),(4,'admin','0002_logentry_remove_auto_add','2025-02-23 10:00:48.519688'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-23 10:00:48.530415'),(6,'contenttypes','0002_remove_content_type_name','2025-02-23 10:00:48.691098'),(7,'auth','0002_alter_permission_name_max_length','2025-02-23 10:00:48.781708'),(8,'auth','0003_alter_user_email_max_length','2025-02-23 10:00:48.812543'),(9,'auth','0004_alter_user_username_opts','2025-02-23 10:00:48.822037'),(10,'auth','0005_alter_user_last_login_null','2025-02-23 10:00:48.904147'),(11,'auth','0006_require_contenttypes_0002','2025-02-23 10:00:48.908356'),(12,'auth','0007_alter_validators_add_error_messages','2025-02-23 10:00:48.917177'),(13,'auth','0008_alter_user_username_max_length','2025-02-23 10:00:49.019847'),(14,'auth','0009_alter_user_last_name_max_length','2025-02-23 10:00:49.119236'),(15,'auth','0010_alter_group_name_max_length','2025-02-23 10:00:49.143390'),(16,'auth','0011_update_proxy_permissions','2025-02-23 10:00:49.152562'),(17,'auth','0012_alter_user_first_name_max_length','2025-02-23 10:00:49.250990'),(18,'sessions','0001_initial','2025-02-23 10:00:49.304210'),(19,'tracker','0001_initial','2025-02-23 10:00:49.666878'),(20,'tracker','0002_budget_user_expense_user_recurringexpense_user_and_more','2025-02-23 10:07:28.180310');
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracker_budget`
--

DROP TABLE IF EXISTS `tracker_budget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracker_budget` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `category_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tracker_budget_category_id_9063dc9d_fk_tracker_category_id` (`category_id`),
  KEY `tracker_budget_user_id_7987a501_fk_auth_user_id` (`user_id`),
  CONSTRAINT `tracker_budget_category_id_9063dc9d_fk_tracker_category_id` FOREIGN KEY (`category_id`) REFERENCES `tracker_category` (`id`),
  CONSTRAINT `tracker_budget_user_id_7987a501_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracker_budget`
--

LOCK TABLES `tracker_budget` WRITE;
/*!40000 ALTER TABLE `tracker_budget` DISABLE KEYS */;
INSERT INTO `tracker_budget` VALUES (1,2000.00,'2025-02-01','2025-02-28',2,1);
/*!40000 ALTER TABLE `tracker_budget` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracker_category`
--

DROP TABLE IF EXISTS `tracker_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracker_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracker_category`
--

LOCK TABLES `tracker_category` WRITE;
/*!40000 ALTER TABLE `tracker_category` DISABLE KEYS */;
INSERT INTO `tracker_category` VALUES (1,'Food & Dining'),(2,'Groceries'),(3,'Utilities'),(4,'Transportation'),(5,'Entertainment'),(6,'Healthcare'),(7,'Rent/Mortgage'),(8,'Shopping'),(9,'Travel'),(10,'Education'),(11,'Personal Care'),(12,'Miscellaneous');
/*!40000 ALTER TABLE `tracker_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracker_expense`
--

DROP TABLE IF EXISTS `tracker_expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracker_expense` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `currency` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `description` longtext,
  `category_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tracker_expense_category_id_173a94b6_fk_tracker_category_id` (`category_id`),
  KEY `tracker_expense_user_id_ec1a4ee0_fk_auth_user_id` (`user_id`),
  CONSTRAINT `tracker_expense_category_id_173a94b6_fk_tracker_category_id` FOREIGN KEY (`category_id`) REFERENCES `tracker_category` (`id`),
  CONSTRAINT `tracker_expense_user_id_ec1a4ee0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracker_expense`
--

LOCK TABLES `tracker_expense` WRITE;
/*!40000 ALTER TABLE `tracker_expense` DISABLE KEYS */;
INSERT INTO `tracker_expense` VALUES (1,'Onions',100.00,'INR','2025-02-23','Onions',1,1),(3,'Groceries #2',120.00,'INR','2024-11-04','Weekly grocery run',2,1),(4,'Utilities #3',480.00,'INR','2024-11-06','Electricity bill',3,1),(5,'Transportation #4',90.00,'INR','2024-11-07','Cab fare',4,1),(6,'Entertainment #5',320.00,'INR','2024-11-08','Movie tickets',5,1),(7,'Healthcare #6',150.00,'INR','2024-11-10','Pharmacy purchase',6,1),(8,'Rent/Mortgage #7',1000.00,'INR','2024-11-11','Monthly rent',7,1),(9,'Shopping #8',360.00,'INR','2024-11-13','Clothes shopping',8,1),(10,'Travel #9',420.00,'INR','2024-11-15','Train ticket',9,1),(11,'Education #10',200.00,'INR','2024-11-17','Books & supplies',10,1),(12,'Personal Care #11',180.00,'INR','2024-11-18','Salon visit',11,1),(13,'Miscellaneous #12',75.00,'INR','2024-11-19','Random purchase',12,1),(14,'Food & Dining #13',250.00,'INR','2024-11-20','Restaurant outing',1,1),(15,'Groceries #14',140.00,'INR','2024-11-21','Vegetables & fruits',2,1),(16,'Utilities #15',320.00,'INR','2024-11-22','Water bill',3,1),(17,'Transportation #16',70.00,'INR','2024-11-23','Metro pass',4,1),(18,'Entertainment #17',410.00,'INR','2024-11-24','Concert ticket',5,1),(19,'Healthcare #18',200.00,'INR','2024-11-25','Doctor visit',6,1),(20,'Rent/Mortgage #19',1000.00,'INR','2024-11-26','Apartment rent',7,1),(21,'Shopping #20',380.00,'INR','2024-11-27','Online purchase',8,1),(22,'Travel #21',450.00,'INR','2024-12-01','Flight booking',9,1),(23,'Education #22',210.00,'INR','2024-12-02','Online course fee',10,1),(24,'Personal Care #23',160.00,'INR','2024-12-03','Haircut & styling',11,1),(25,'Miscellaneous #24',95.00,'INR','2024-12-04','Random expense',12,1),(26,'Food & Dining #25',290.00,'INR','2024-12-05','Lunch outing',1,1),(27,'Groceries #26',110.00,'INR','2024-12-06','Supermarket run',2,1),(28,'Utilities #27',500.00,'INR','2024-12-07','Gas bill',3,1),(29,'Transportation #28',120.00,'INR','2024-12-08','Rideshare',4,1),(30,'Entertainment #29',380.00,'INR','2024-12-09','Theater show',5,1),(31,'Healthcare #30',250.00,'INR','2024-12-10','Dental checkup',6,1),(32,'Rent/Mortgage #31',1000.00,'INR','2024-12-11','Monthly rent',7,1),(33,'Shopping #32',270.00,'INR','2024-12-12','Electronics',8,1),(34,'Travel #33',490.00,'INR','2024-12-13','Bus pass',9,1),(35,'Education #34',200.00,'INR','2024-12-14','Online seminar',10,1),(36,'Personal Care #35',130.00,'INR','2024-12-15','Cosmetics',11,1),(37,'Miscellaneous #36',85.00,'INR','2024-12-16','Gift purchase',12,1),(38,'Food & Dining #37',350.00,'INR','2024-12-17','Dinner party',1,1),(39,'Groceries #38',200.00,'INR','2024-12-18','Monthly groceries',2,1),(40,'Utilities #39',450.00,'INR','2024-12-19','Internet bill',3,1),(41,'Transportation #40',60.00,'INR','2024-12-20','Taxi fare',4,1),(42,'Entertainment #41',300.00,'INR','2024-12-21','Live music event',5,1),(43,'Healthcare #42',220.00,'INR','2024-12-22','Therapy session',6,1),(44,'Rent/Mortgage #43',1000.00,'INR','2024-12-23','Rent payment',7,1),(45,'Shopping #44',340.00,'INR','2024-12-24','Holiday gifts',8,1),(46,'Travel #45',460.00,'INR','2024-12-25','Out-of-town bus',9,1),(47,'Education #46',180.00,'INR','2024-12-26','E-learning subscription',10,1),(48,'Personal Care #47',140.00,'INR','2024-12-27','Spa session',11,1),(49,'Miscellaneous #48',70.00,'INR','2024-12-28','Random spending',12,1),(50,'Food & Dining #49',260.00,'INR','2024-12-29','Fast food',1,1),(51,'Groceries #50',190.00,'INR','2024-12-30','Fruit & veggies',2,1),(52,'Utilities #51',490.00,'INR','2025-01-02','Phone bill',3,1),(53,'Transportation #52',100.00,'INR','2025-01-03','Ride share',4,1),(54,'Entertainment #53',320.00,'INR','2025-01-04','Gaming subscription',5,1),(55,'Healthcare #54',280.00,'INR','2025-01-05','Specialist visit',6,1),(56,'Rent/Mortgage #55',1000.00,'INR','2025-01-06','Monthly rent',7,1),(57,'Shopping #56',390.00,'INR','2025-01-07','New shoes',8,1),(58,'Travel #57',470.00,'INR','2025-01-08','Flight ticket',9,1),(59,'Education #58',220.00,'INR','2025-01-09','Course materials',10,1),(60,'Personal Care #59',155.00,'INR','2025-01-10','Skincare products',11,1),(61,'Miscellaneous #60',95.00,'INR','2025-01-11','Household items',12,1),(62,'Food & Dining #61',310.00,'INR','2025-01-12','Dinner outing',1,1),(63,'Groceries #62',170.00,'INR','2025-01-13','Weekly supplies',2,1),(64,'Utilities #63',420.00,'INR','2025-01-14','Gas bill',3,1),(65,'Transportation #64',85.00,'INR','2025-01-15','Public transport',4,1),(66,'Entertainment #65',290.00,'INR','2025-01-16','Concert pass',5,1),(67,'Healthcare #66',200.00,'INR','2025-01-17','Hospital checkup',6,1),(68,'Rent/Mortgage #67',1000.00,'INR','2025-01-18','Apartment rent',7,1),(69,'Shopping #68',340.00,'INR','2025-01-19','Online order',8,1),(70,'Travel #69',495.00,'INR','2025-01-20','Bus ticket',9,1),(71,'Education #70',210.00,'INR','2025-01-21','Exam fees',10,1),(72,'Personal Care #71',180.00,'INR','2025-01-22','Massage therapy',11,1),(73,'Miscellaneous #72',50.00,'INR','2025-01-23','Random items',12,1),(74,'Food & Dining #73',220.00,'INR','2025-01-24','Restaurant meal',1,1),(75,'Groceries #74',160.00,'INR','2025-01-25','Bulk groceries',2,1),(76,'Utilities #75',410.00,'INR','2025-01-26','Water bill',3,1),(77,'Transportation #76',95.00,'INR','2025-01-27','Taxi ride',4,1),(78,'Entertainment #77',370.00,'INR','2025-01-28','Streaming services',5,1),(79,'Healthcare #78',270.00,'INR','2025-01-29','Clinic visit',6,1),(80,'Rent/Mortgage #79',1000.00,'INR','2025-01-30','Monthly rent',7,1),(81,'Shopping #80',310.00,'INR','2025-01-31','Clothes & accessories',8,1),(82,'Travel #81',420.00,'INR','2025-02-01','Outstation bus',9,1),(83,'Education #82',190.00,'INR','2025-02-02','Online workshop',10,1),(84,'Personal Care #83',140.00,'INR','2025-02-03','Hair products',11,1),(85,'Miscellaneous #84',85.00,'INR','2025-02-04','Pet supplies',12,1),(86,'Food & Dining #85',230.00,'INR','2025-02-05','Takeaway lunch',1,1),(87,'Groceries #86',130.00,'INR','2025-02-06','Grocery haul',2,1),(88,'Utilities #87',470.00,'INR','2025-02-07','Internet recharge',3,1),(89,'Transportation #88',120.00,'INR','2025-02-08','Bus pass renewal',4,1),(90,'Entertainment #89',340.00,'INR','2025-02-09','Video game purchase',5,1),(91,'Healthcare #90',180.00,'INR','2025-02-10','Over-the-counter meds',6,1),(92,'Rent/Mortgage #91',1000.00,'INR','2025-02-11','Rent due',7,1),(93,'Shopping #92',390.00,'INR','2025-02-12','Online gadgets',8,1),(94,'Travel #93',450.00,'INR','2025-02-13','Flight booking',9,1),(95,'Education #94',230.00,'INR','2025-02-14','E-book purchase',10,1),(96,'Personal Care #95',160.00,'INR','2025-02-15','Spa session',11,1),(97,'Miscellaneous #96',60.00,'INR','2025-02-16','Key cutting',12,1),(98,'Food & Dining #97',280.00,'INR','2025-02-17','Family dinner',1,1),(99,'Groceries #98',140.00,'INR','2025-02-18','Vegetables & fruits',2,1),(100,'Utilities #99',430.00,'INR','2025-02-19','Electricity bill',3,1),(101,'Transportation #100',80.00,'INR','2025-02-20','Auto fare',4,1);
/*!40000 ALTER TABLE `tracker_expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracker_recurringexpense`
--

DROP TABLE IF EXISTS `tracker_recurringexpense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracker_recurringexpense` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `recurrence_interval` varchar(50) NOT NULL,
  `next_occurrence` date NOT NULL,
  `expense_id` bigint NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tracker_recurringexp_expense_id_5b992ff0_fk_tracker_e` (`expense_id`),
  KEY `tracker_recurringexpense_user_id_23a3b14d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `tracker_recurringexp_expense_id_5b992ff0_fk_tracker_e` FOREIGN KEY (`expense_id`) REFERENCES `tracker_expense` (`id`),
  CONSTRAINT `tracker_recurringexpense_user_id_23a3b14d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracker_recurringexpense`
--

LOCK TABLES `tracker_recurringexpense` WRITE;
/*!40000 ALTER TABLE `tracker_recurringexpense` DISABLE KEYS */;
/*!40000 ALTER TABLE `tracker_recurringexpense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'expenseease_db'
--

--
-- Dumping routines for database 'expenseease_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-23 17:37:38
