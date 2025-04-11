CREATE DATABASE  IF NOT EXISTS `reciperealm_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `reciperealm_db`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: reciperealm_db
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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add recipe',5,'add_recipe'),(18,'Can change recipe',5,'change_recipe'),(19,'Can delete recipe',5,'delete_recipe'),(20,'Can view recipe',5,'view_recipe'),(21,'Can add rating',6,'add_rating'),(22,'Can change rating',6,'change_rating'),(23,'Can delete rating',6,'delete_rating'),(24,'Can view rating',6,'view_rating'),(25,'Can add log entry',7,'add_logentry'),(26,'Can change log entry',7,'change_logentry'),(27,'Can delete log entry',7,'delete_logentry'),(28,'Can view log entry',7,'view_logentry'),(29,'Can add session',8,'add_session'),(30,'Can change session',8,'change_session'),(31,'Can delete session',8,'delete_session'),(32,'Can view session',8,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$8EC02D1LTQ3ebfU1I3hYOz$iehTTFxfwn9tHLjm432XxZ9yb5wejzOFxoflAUJXv38=','2025-03-23 05:31:14.736162',1,'admin','','','admin@gmail.com',1,1,'2025-03-21 11:21:12.408187'),(2,'pbkdf2_sha256$870000$DaHzlezZBQ1yhxSn87FNaz$i7dzqTtgC62xZ4RUhck2LjX0CU79C/7bxvAxa8xtIMQ=','2025-03-24 04:42:55.358553',0,'sahana','','','sahana@gmail.com',0,1,'2025-03-24 04:42:40.426753'),(3,'pbkdf2_sha256$870000$V9OaBpo8iBHunCVUbkixcw$1dLakV3zt8uFdEFU55VO1KGIENVkzya1p+iODSausas=','2025-03-24 04:57:31.655158',0,'vinay','','','vinay@gmail.com',0,1,'2025-03-24 04:54:17.566925'),(5,'pbkdf2_sha256$870000$k81u7RoWzq6CoMtjBkTKu2$QWYzp6i6uFkX4LMyGmpobXBFLm1DpplSvqN3eUGwP2Q=','2025-03-24 04:56:27.816532',0,'testuser','','','vinay@skyllx.com',0,1,'2025-03-24 04:56:06.027527');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-03-21 12:10:46.024140','5','Mango Smoothie',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(2,'2025-03-21 12:11:51.195276','4','Grilled Chicken Salad',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(3,'2025-03-21 12:12:16.508881','3','Chocolate Chip Cookies',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(4,'2025-03-21 12:12:30.608863','2','Spaghetti Bolognese',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(5,'2025-03-21 12:12:59.949553','1','Classic Pancakes',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(6,'2025-03-22 17:03:21.058195','5','Mango Smoothie',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(7,'2025-03-22 17:03:40.361277','4','Grilled Chicken Salad',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(8,'2025-03-22 17:03:50.475478','3','Chocolate Chip Cookies',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(9,'2025-03-22 17:04:07.073922','2','Spaghetti Bolognese',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(10,'2025-03-22 17:04:15.797179','1','Classic Pancakes',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',5,1),(11,'2025-03-23 04:14:54.630170','1','admin rated Classic Pancakes as 9/5',1,'[{\"added\": {}}]',9,1),(12,'2025-03-23 04:15:19.332323','1','admin rated Classic Pancakes as 4/5',2,'[{\"changed\": {\"fields\": [\"Rating\"]}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(3,'auth','user'),(4,'contenttypes','contenttype'),(6,'recipes','rating'),(5,'recipes','recipe'),(9,'recipes','reciperating'),(8,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-21 08:46:10.006145'),(2,'auth','0001_initial','2025-03-21 08:46:11.591329'),(3,'recipes','0001_initial','2025-03-21 08:46:11.924220'),(4,'admin','0001_initial','2025-03-21 11:12:33.551176'),(5,'admin','0002_logentry_remove_auto_add','2025-03-21 11:12:33.583349'),(6,'admin','0003_logentry_add_action_flag_choices','2025-03-21 11:12:33.611794'),(7,'contenttypes','0002_remove_content_type_name','2025-03-21 11:12:33.938433'),(8,'auth','0002_alter_permission_name_max_length','2025-03-21 11:12:34.085189'),(9,'auth','0003_alter_user_email_max_length','2025-03-21 11:12:34.195144'),(10,'auth','0004_alter_user_username_opts','2025-03-21 11:12:34.224431'),(11,'auth','0005_alter_user_last_login_null','2025-03-21 11:12:34.445404'),(12,'auth','0006_require_contenttypes_0002','2025-03-21 11:12:34.452781'),(13,'auth','0007_alter_validators_add_error_messages','2025-03-21 11:12:34.486792'),(14,'auth','0008_alter_user_username_max_length','2025-03-21 11:12:34.733879'),(15,'auth','0009_alter_user_last_name_max_length','2025-03-21 11:12:34.856824'),(16,'auth','0010_alter_group_name_max_length','2025-03-21 11:12:34.895894'),(17,'auth','0011_update_proxy_permissions','2025-03-21 11:12:34.914307'),(18,'auth','0012_alter_user_first_name_max_length','2025-03-21 11:12:35.068030'),(19,'sessions','0001_initial','2025-03-21 11:12:35.169090');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('xcbgn4q09qlkp2a3yptmmilunvpxgck5','.eJxVjMsOwiAQRf-FtSGDPAou3fcbyMAwUjU0Ke3K-O_apAvd3nPOfYmI21rj1ssSJxIXocXpd0uYH6XtgO7YbrPMc1uXKcldkQftcpypPK-H-3dQsddvHRxbzwWKcSGTdoW1NwxgmfJgjUqOaWBjggZNmhh8BjyjUqw4eWPF-wPucDgP:1twZsR:vkSSNrJPrhbJxeYQMn6kIrFYLaeUi1EyclQyTY3vN8I','2025-04-07 04:57:31.662072');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recipes_rating`
--

LOCK TABLES `recipes_rating` WRITE;
/*!40000 ALTER TABLE `recipes_rating` DISABLE KEYS */;
INSERT INTO `recipes_rating` VALUES (1,4,1,1),(2,4,1,2),(3,3,1,3),(4,5,5,4),(5,2,3,4);
/*!40000 ALTER TABLE `recipes_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recipes_recipe`
--

LOCK TABLES `recipes_recipe` WRITE;
/*!40000 ALTER TABLE `recipes_recipe` DISABLE KEYS */;
INSERT INTO `recipes_recipe` VALUES (1,'Classic Pancakes','Fluffy and delicious homemade pancakes. Perfect for breakfast!','recipe_images/Classic_Pancakes.jpeg','breakfast','2025-03-21 12:03:32.689681','Flour, Eggs, Milk, Sugar, Baking Powder, Butter, Vanilla Extract',1),(2,'Spaghetti Bolognese','A rich and hearty Italian-style pasta with meat sauce.','recipe_images/Spaghetti_Carbonara.jpg','dinner','2025-03-21 12:03:32.706871','Spaghetti, Ground Beef, Tomato Sauce, Garlic, Onion, Olive Oil, Basil',1),(3,'Chocolate Chip Cookies','Soft and chewy cookies packed with chocolate chips.','recipe_images/Chocolate_Chip_Cookies.jpeg','dessert','2025-03-21 12:03:32.717139','Flour, Butter, Sugar, Eggs, Baking Soda, Vanilla Extract, Chocolate Chips',1),(4,'Grilled Chicken Salad','A healthy and fresh salad with grilled chicken.','recipe_images/Grilled_Chicken_Salad.jpeg','lunch','2025-03-21 12:03:32.724202','Chicken Breast, Lettuce, Cherry Tomatoes, Cucumber, Olive Oil, Lemon Juice, Feta Cheese',1),(5,'Mango Smoothie','A refreshing tropical smoothie made with mango and yogurt.','recipe_images/Mango_Smoothie.jpeg','breakfast','2025-03-21 12:03:32.731726','Mango, Yogurt, Honey, Ice Cubes',1);
/*!40000 ALTER TABLE `recipes_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'reciperealm_db'
--

--
-- Dumping routines for database 'reciperealm_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-24 10:39:25
