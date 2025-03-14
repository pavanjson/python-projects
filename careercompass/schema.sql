CREATE DATABASE  IF NOT EXISTS `careercompass` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `careercompass`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: careercompass
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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add company',7,'add_company'),(26,'Can change company',7,'change_company'),(27,'Can delete company',7,'delete_company'),(28,'Can view company',7,'view_company'),(29,'Can add job',8,'add_job'),(30,'Can change job',8,'change_job'),(31,'Can delete job',8,'delete_job'),(32,'Can view job',8,'view_job'),(33,'Can add application',9,'add_application'),(34,'Can change application',9,'change_application'),(35,'Can delete application',9,'delete_application'),(36,'Can view application',9,'view_application'),(37,'Can add user profile',10,'add_userprofile'),(38,'Can change user profile',10,'change_userprofile'),(39,'Can delete user profile',10,'delete_userprofile'),(40,'Can view user profile',10,'view_userprofile');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$lwYr8MT4Cm9KeZzU43tDvQ$jskSmsccBT8QCBumxSHye0k8o3hmLILu2tgaVb6qTlA=','2025-03-14 05:48:35.748477',1,'admin','','','vinay@skyllx.com',1,1,'2025-02-23 12:57:40.708964'),(2,'pbkdf2_sha256$870000$6DjpPXddi7gztUTczz6dXF$Tu7avONYD5eqJD9/UKj61jaAYSs1VV5r/zYFOiE2G70=','2025-03-14 05:51:42.111106',0,'vinayhp','','','',0,1,'2025-02-23 13:17:35.151759');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-02-23 13:24:25.264302','10','Beta Innovations',2,'[{\"changed\": {\"fields\": [\"Logo\"]}}]',7,1),(2,'2025-02-24 05:49:41.420104','2','vinayhp',2,'[{\"changed\": {\"fields\": [\"Bio\"]}}]',10,1),(3,'2025-02-24 05:50:51.618119','2','vinayhp',2,'[{\"changed\": {\"fields\": [\"Resume\"]}}]',10,1),(4,'2025-03-12 05:34:55.300832','6','vinayhp - Software Engineer',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',9,1),(5,'2025-03-12 05:45:42.007503','6','vinayhp - Software Engineer',3,'',9,1),(6,'2025-03-12 05:45:42.007544','5','vinayhp - Software Engineer',3,'',9,1),(7,'2025-03-12 05:45:42.007566','3','admin - Software Engineer',3,'',9,1),(8,'2025-03-12 05:45:42.007584','2','admin - Software Engineer',3,'',9,1),(9,'2025-03-14 05:49:07.492297','7','vinayhp - Frontend Developer',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',9,1),(10,'2025-03-14 05:49:33.505652','1','vinayhp - Software Engineer',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',9,1);
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
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'jobs','application'),(7,'jobs','company'),(8,'jobs','job'),(10,'jobs','userprofile'),(6,'sessions','session');
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
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-23 12:56:26.219342'),(2,'auth','0001_initial','2025-02-23 12:56:27.494711'),(3,'admin','0001_initial','2025-02-23 12:56:27.813005'),(4,'admin','0002_logentry_remove_auto_add','2025-02-23 12:56:27.829839'),(5,'admin','0003_logentry_add_action_flag_choices','2025-02-23 12:56:27.846282'),(6,'contenttypes','0002_remove_content_type_name','2025-02-23 12:56:28.109409'),(7,'auth','0002_alter_permission_name_max_length','2025-02-23 12:56:28.278828'),(8,'auth','0003_alter_user_email_max_length','2025-02-23 12:56:28.316240'),(9,'auth','0004_alter_user_username_opts','2025-02-23 12:56:28.330430'),(10,'auth','0005_alter_user_last_login_null','2025-02-23 12:56:28.462265'),(11,'auth','0006_require_contenttypes_0002','2025-02-23 12:56:28.468639'),(12,'auth','0007_alter_validators_add_error_messages','2025-02-23 12:56:28.485876'),(13,'auth','0008_alter_user_username_max_length','2025-02-23 12:56:28.658803'),(14,'auth','0009_alter_user_last_name_max_length','2025-02-23 12:56:28.842100'),(15,'auth','0010_alter_group_name_max_length','2025-02-23 12:56:28.891476'),(16,'auth','0011_update_proxy_permissions','2025-02-23 12:56:28.911647'),(17,'auth','0012_alter_user_first_name_max_length','2025-02-23 12:56:29.079932'),(18,'jobs','0001_initial','2025-02-23 12:56:29.896271'),(19,'sessions','0001_initial','2025-02-23 12:56:29.955333'),(20,'jobs','0002_userprofile_current_company_userprofile_location_and_more','2025-03-11 05:20:08.823944');
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
INSERT INTO `django_session` VALUES ('6bd53i5rsqtunwpdv5e1sn4l3e7r0iw4','.eJxVjEEOwiAQRe_C2hDotIAu3fcMZJgZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uLsur0uyWkh9Qd8B3rbdY013WZkt4VfdCmx5nleT3cv4OCrXxrD77vxWUjxBmYCU0nkM-hM0A8DBkDANkkBmwOIXi0gZhd8hbEJVHvD_n_OJI:1tsEjn:Y9hp7rKh7gyGgESP3JhEJukLu5ND6NZ76k0uwuMQzqY','2025-03-26 05:34:39.359864'),('8eg5kpqxyuvgvf8mw2uspbpa4qmhwd2p','.eJxVjEEOwiAQRe_C2hDotIAu3fcMZJgZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uLsur0uyWkh9Qd8B3rbdY013WZkt4VfdCmx5nleT3cv4OCrXxrD77vxWUjxBmYCU0nkM-hM0A8DBkDANkkBmwOIXi0gZhd8hbEJVHvD_n_OJI:1tsxuN:4Y580p-sik-4tvtkVCL3DDuMQ4bX_ymcB3RRWN5U7SI','2025-03-28 05:48:35.754672'),('8mnfcr4w24va7625l67xcldle31ai9rm','.eJxVjMsOgjAUBf-la9P0trSAS_d-Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexZyNN6ffjZAfOu1A7jjdZsvztC4j2V2xB632Oos-L4f7dzBgHb51aZ0XAYC-TRgbDooUpIlIGrnEgkAuOd-zD06p4-CL4yZKJ0AJtDfvD_C-OEU:1tmRM8:xdTB4qXtV6BazCBw81n-1okdhKvMy0KgaPdOSR_ZKsk','2025-03-10 05:50:16.597711'),('i5v42q3l1am5hl6xvulac2buk8eiy415','.eJxVjMsOgjAUBf-la9P0trSAS_d-Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexZyNN6ffjZAfOu1A7jjdZsvztC4j2V2xB632Oos-L4f7dzBgHb51aZ0XAYC-TRgbDooUpIlIGrnEgkAuOd-zD06p4-CL4yZKJ0AJtDfvD_C-OEU:1tsxxO:A4R3VI6ecIRb9wLu7eubZ8cZwVF2OnJx6umtI6k9d40','2025-03-28 05:51:42.115636'),('vjfwkxae3szhrff4190xwt1ckro7uqw8','.eJxVjEEOwiAQRe_C2hDotIAu3fcMZJgZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uLsur0uyWkh9Qd8B3rbdY013WZkt4VfdCmx5nleT3cv4OCrXxrD77vxWUjxBmYCU0nkM-hM0A8DBkDANkkBmwOIXi0gZhd8hbEJVHvD_n_OJI:1tsxkK:Px8eDkuEZMsvd6xEW6yAWhFOw7O9p65G9crz8TuGyjw','2025-03-28 05:38:12.296923'),('yiv097nuoe67kqe3cb6r1gzn27o0rbpq','.eJxVjEEOwiAQRe_C2hDotIAu3fcMZJgZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uLsur0uyWkh9Qd8B3rbdY013WZkt4VfdCmx5nleT3cv4OCrXxrD77vxWUjxBmYCU0nkM-hM0A8DBkDANkkBmwOIXi0gZhd8hbEJVHvD_n_OJI:1tmBvt:lOm1NhmYBwbO-01cSQayMS8UT1i1mHN81pwvRAv-L8A','2025-03-09 13:22:09.991506');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_application`
--

DROP TABLE IF EXISTS `jobs_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_application` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cover_letter` longtext NOT NULL,
  `resume` varchar(100) DEFAULT NULL,
  `applied_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `user_id` int NOT NULL,
  `job_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_application_user_id_59477d51_fk_auth_user_id` (`user_id`),
  KEY `jobs_application_job_id_7bb7e966_fk_jobs_job_id` (`job_id`),
  CONSTRAINT `jobs_application_job_id_7bb7e966_fk_jobs_job_id` FOREIGN KEY (`job_id`) REFERENCES `jobs_job` (`id`),
  CONSTRAINT `jobs_application_user_id_59477d51_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_application`
--

LOCK TABLES `jobs_application` WRITE;
/*!40000 ALTER TABLE `jobs_application` DISABLE KEYS */;
INSERT INTO `jobs_application` VALUES (1,'','applications/resumes/report_2025-01.pdf','2025-02-23 13:19:12.858774','accepted',2,1),(4,'','','2025-03-10 12:27:32.264940','pending',1,1),(7,'','applications/resumes/design3.jpg','2025-03-14 05:46:48.354255','reviewed',2,2);
/*!40000 ALTER TABLE `jobs_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_company`
--

DROP TABLE IF EXISTS `jobs_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `website` varchar(200) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_company`
--

LOCK TABLES `jobs_company` WRITE;
/*!40000 ALTER TABLE `jobs_company` DISABLE KEYS */;
INSERT INTO `jobs_company` VALUES (1,'Tech Solutions Inc.','A leading technology firm specializing in innovative solutions.','https://www.techsolutions.com',NULL),(2,'Innovative Designs LLC','Designing creative solutions for modern businesses.','https://www.innovativedesigns.com',NULL),(3,'Global Ventures','Expanding business horizons across the globe.','https://www.globalventures.com',NULL),(4,'NextGen Software','Developing next-generation software solutions.','https://www.nextgensoftware.com',NULL),(5,'Creative Minds','Empowering creativity with innovative technology.','https://www.creativeminds.com',NULL),(6,'Enterprise Dynamics','Dynamic enterprise solutions for modern challenges.','https://www.enterprisedynamics.com',NULL),(7,'Digital Horizon','Shaping the digital future with cutting-edge tech.','https://www.digitalhorizon.com',NULL),(8,'FutureTech','Innovations that drive the future of technology.','https://www.futuretech.com',NULL),(9,'Alpha Systems','Pioneering system solutions for global enterprises.','https://www.alphasystems.com',NULL),(10,'Beta Innovations','Transforming ideas into reality with innovative tech.','https://www.betainnovations.com','company_logos/beta_innovations.png');
/*!40000 ALTER TABLE `jobs_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_job`
--

DROP TABLE IF EXISTS `jobs_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_job` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `location` varchar(255) NOT NULL,
  `posted_date` datetime(6) NOT NULL,
  `application_deadline` datetime(6) DEFAULT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_job_company_id_1f42ea7c_fk_jobs_company_id` (`company_id`),
  CONSTRAINT `jobs_job_company_id_1f42ea7c_fk_jobs_company_id` FOREIGN KEY (`company_id`) REFERENCES `jobs_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_job`
--

LOCK TABLES `jobs_job` WRITE;
/*!40000 ALTER TABLE `jobs_job` DISABLE KEYS */;
INSERT INTO `jobs_job` VALUES (1,'Software Engineer','Develop and maintain cutting-edge web applications.','New York, NY','2025-02-23 18:46:43.000000','2025-03-25 18:46:43.000000',1),(2,'Frontend Developer','Create responsive and engaging user interfaces.','San Francisco, CA','2025-02-23 18:46:43.000000','2025-03-20 18:46:43.000000',2),(3,'Backend Developer','Design robust server-side logic and APIs.','Austin, TX','2025-02-23 18:46:43.000000','2025-03-15 18:46:43.000000',3),(4,'Full Stack Developer','Work on both frontend and backend to build scalable applications.','Seattle, WA','2025-02-23 18:46:43.000000','2025-03-30 18:46:43.000000',4),(5,'Project Manager','Manage project timelines, deliverables, and team coordination.','Boston, MA','2025-02-23 18:46:43.000000','2025-04-04 18:46:43.000000',5),(6,'Data Scientist','Analyze and interpret complex data to drive business insights.','Chicago, IL','2025-02-23 18:46:43.000000','2025-03-25 18:46:43.000000',6),(7,'UX/UI Designer','Design intuitive user interfaces and enhance user experience.','Denver, CO','2025-02-23 18:46:43.000000','2025-03-23 18:46:43.000000',7),(8,'DevOps Engineer','Automate and streamline development and deployment processes.','Atlanta, GA','2025-02-23 18:46:43.000000','2025-03-27 18:46:43.000000',8),(9,'Quality Assurance Engineer','Test and ensure the quality of software applications.','Los Angeles, CA','2025-02-23 18:46:43.000000','2025-03-22 18:46:43.000000',9),(10,'Product Manager','Lead product strategy and manage product lifecycle.','Miami, FL','2025-02-23 18:46:43.000000','2025-03-25 18:46:43.000000',10);
/*!40000 ALTER TABLE `jobs_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_userprofile`
--

DROP TABLE IF EXISTS `jobs_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_userprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `resume` varchar(100) DEFAULT NULL,
  `bio` longtext NOT NULL,
  `user_id` int NOT NULL,
  `current_company` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `skills` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `jobs_userprofile_user_id_2e767d7c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_userprofile`
--

LOCK TABLES `jobs_userprofile` WRITE;
/*!40000 ALTER TABLE `jobs_userprofile` DISABLE KEYS */;
INSERT INTO `jobs_userprofile` VALUES (1,'','',1,NULL,NULL,NULL),(2,'','Software Developer',2,'SkyllX Technologies pvt','BTM Layout, Bengaluru','Java, Python, PHP');
/*!40000 ALTER TABLE `jobs_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'careercompass'
--

--
-- Dumping routines for database 'careercompass'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-14 11:24:32
