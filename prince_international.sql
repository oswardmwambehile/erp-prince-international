-- MySQL dump 10.13  Distrib 8.0.46, for Linux (x86_64)
--
-- Host: localhost    Database: prince_international
-- ------------------------------------------------------
-- Server version	8.0.46-0ubuntu0.24.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounting_accounttype`
--

DROP TABLE IF EXISTS `accounting_accounttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounting_accounttype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting_accounttype`
--

LOCK TABLES `accounting_accounttype` WRITE;
/*!40000 ALTER TABLE `accounting_accounttype` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounting_accounttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounting_chartofaccount`
--

DROP TABLE IF EXISTS `accounting_chartofaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounting_chartofaccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `account_code` varchar(50) NOT NULL,
  `account_name` varchar(255) NOT NULL,
  `opening_balance` decimal(18,2) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `account_type_id` bigint NOT NULL,
  `company_id` bigint NOT NULL,
  `parent_account_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounting_chartofaccount_company_id_account_code_8f65a06f_uniq` (`company_id`,`account_code`),
  KEY `accounting_chartofac_account_type_id_919ce7b8_fk_accountin` (`account_type_id`),
  KEY `accounting_chartofac_parent_account_id_43065cef_fk_accountin` (`parent_account_id`),
  CONSTRAINT `accounting_chartofac_account_type_id_919ce7b8_fk_accountin` FOREIGN KEY (`account_type_id`) REFERENCES `accounting_accounttype` (`id`),
  CONSTRAINT `accounting_chartofac_company_id_9a313f90_fk_accounts_` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`),
  CONSTRAINT `accounting_chartofac_parent_account_id_43065cef_fk_accountin` FOREIGN KEY (`parent_account_id`) REFERENCES `accounting_chartofaccount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting_chartofaccount`
--

LOCK TABLES `accounting_chartofaccount` WRITE;
/*!40000 ALTER TABLE `accounting_chartofaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounting_chartofaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounting_journalentry`
--

DROP TABLE IF EXISTS `accounting_journalentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounting_journalentry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `journal_number` varchar(100) NOT NULL,
  `reference` varchar(255) DEFAULT NULL,
  `description` longtext,
  `posting_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounting_journalentry_company_id_journal_number_0a77d3f9_uniq` (`company_id`,`journal_number`),
  CONSTRAINT `accounting_journalen_company_id_9e360981_fk_accounts_` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting_journalentry`
--

LOCK TABLES `accounting_journalentry` WRITE;
/*!40000 ALTER TABLE `accounting_journalentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounting_journalentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounting_journalentryline`
--

DROP TABLE IF EXISTS `accounting_journalentryline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounting_journalentryline` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `debit` decimal(18,2) NOT NULL,
  `credit` decimal(18,2) NOT NULL,
  `account_id` bigint NOT NULL,
  `journal_entry_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounting_journalen_account_id_521eb404_fk_accountin` (`account_id`),
  KEY `accounting_journalen_journal_entry_id_78ed6ea5_fk_accountin` (`journal_entry_id`),
  CONSTRAINT `accounting_journalen_account_id_521eb404_fk_accountin` FOREIGN KEY (`account_id`) REFERENCES `accounting_chartofaccount` (`id`),
  CONSTRAINT `accounting_journalen_journal_entry_id_78ed6ea5_fk_accountin` FOREIGN KEY (`journal_entry_id`) REFERENCES `accounting_journalentry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting_journalentryline`
--

LOCK TABLES `accounting_journalentryline` WRITE;
/*!40000 ALTER TABLE `accounting_journalentryline` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounting_journalentryline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_branch`
--

DROP TABLE IF EXISTS `accounts_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_branch` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(50) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `accounts_branch_company_id_92f5727a_fk_accounts_company_id` (`company_id`),
  CONSTRAINT `accounts_branch_company_id_92f5727a_fk_accounts_company_id` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_branch`
--

LOCK TABLES `accounts_branch` WRITE;
/*!40000 ALTER TABLE `accounts_branch` DISABLE KEYS */;
INSERT INTO `accounts_branch` VALUES (1,'Mbezi beach(Jogoo)','BE20','Dar es salaam','2026-06-18 06:30:41.416047',1,1);
/*!40000 ALTER TABLE `accounts_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_company`
--

DROP TABLE IF EXISTS `accounts_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(50) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `address` longtext,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_company`
--

LOCK TABLES `accounts_company` WRITE;
/*!40000 ALTER TABLE `accounts_company` DISABLE KEYS */;
INSERT INTO `accounts_company` VALUES (1,'Prince International','DS01','princeinternational@gmail.com','0689869255','Kyela',1,'2026-06-08 12:04:47.371190','2026-06-08 12:04:47.371211');
/*!40000 ALTER TABLE `accounts_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_department`
--

DROP TABLE IF EXISTS `accounts_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `accounts_department_company_id_51470d70_fk_accounts_company_id` (`company_id`),
  CONSTRAINT `accounts_department_company_id_51470d70_fk_accounts_company_id` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_department`
--

LOCK TABLES `accounts_department` WRITE;
/*!40000 ALTER TABLE `accounts_department` DISABLE KEYS */;
INSERT INTO `accounts_department` VALUES (1,'Manager','M',1,'2026-06-18 06:31:24.730012','2026-06-18 06:31:24.730032',1),(2,'Sales and marketing','SAM',1,'2026-06-18 06:42:14.411541','2026-06-18 07:21:28.206024',1),(3,'Accountant','ACC',1,'2026-06-18 06:45:16.148790','2026-06-18 06:45:16.148813',1);
/*!40000 ALTER TABLE `accounts_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_position`
--

DROP TABLE IF EXISTS `accounts_position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_position` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_position_company_id_eb37f7ae_fk_accounts_company_id` (`company_id`),
  CONSTRAINT `accounts_position_company_id_eb37f7ae_fk_accounts_company_id` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_position`
--

LOCK TABLES `accounts_position` WRITE;
/*!40000 ALTER TABLE `accounts_position` DISABLE KEYS */;
INSERT INTO `accounts_position` VALUES (1,'Manager','Manager',1,'2026-06-18 06:31:55.917210','2026-06-18 06:31:55.917238',1),(2,'Sales and marketing','Sales and Marketing',1,'2026-06-18 06:42:49.491478','2026-06-18 07:22:43.545484',1),(3,'Accountant','Accountant',1,'2026-06-18 06:45:56.933622','2026-06-18 06:45:56.933661',1),(4,'Inventory Manager','Inventory Manager',1,'2026-06-18 06:54:45.182922','2026-06-18 06:54:45.182992',1);
/*!40000 ALTER TABLE `accounts_position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `contact` varchar(13) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `branch_id` bigint DEFAULT NULL,
  `company_id` bigint DEFAULT NULL,
  `department_id` bigint DEFAULT NULL,
  `position_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `accounts_user_branch_id_38ec6caf_fk_accounts_branch_id` (`branch_id`),
  KEY `accounts_user_company_id_bc91fe74_fk_accounts_company_id` (`company_id`),
  KEY `accounts_user_department_id_8dc06840_fk_accounts_department_id` (`department_id`),
  KEY `accounts_user_position_id_75cb83eb_fk_accounts_position_id` (`position_id`),
  CONSTRAINT `accounts_user_branch_id_38ec6caf_fk_accounts_branch_id` FOREIGN KEY (`branch_id`) REFERENCES `accounts_branch` (`id`),
  CONSTRAINT `accounts_user_company_id_bc91fe74_fk_accounts_company_id` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`),
  CONSTRAINT `accounts_user_department_id_8dc06840_fk_accounts_department_id` FOREIGN KEY (`department_id`) REFERENCES `accounts_department` (`id`),
  CONSTRAINT `accounts_user_position_id_75cb83eb_fk_accounts_position_id` FOREIGN KEY (`position_id`) REFERENCES `accounts_position` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (1,'pbkdf2_sha256$1200000$dqPTeNrq7scpqilijvPEjI$M6OJ79qTNqNDNRjP4vi2nQ5iKi/D8ZkzKMRzAH0vCi0=','2026-07-04 09:38:39.133748',1,'oswardbiso@gmail.com',NULL,NULL,NULL,1,1,'2026-06-08 11:58:06.896649','2026-06-08 11:58:07.291491',NULL,NULL,NULL,NULL),(2,'pbkdf2_sha256$1200000$Pm01wL3aNOuWeZRY5eMY9l$EcNXFfUnKFRIEwSSN4JrhiVjVj1M39+nSOkYdtU/CAI=','2026-07-24 10:17:46.037130',1,'oswardmwambehile@gmail.com','osward','mwambehile','0657453423',1,0,'2026-06-18 06:28:11.647487','2026-06-30 18:55:00.508057',1,1,1,2),(3,'pbkdf2_sha256$1200000$T7llOQ5Pf6ndbf5XR2QROG$nNvgveXWZwdrqPA5+VDZou+Vc9Rtq+JPjdLcvTVyJic=','2026-06-30 08:11:02.477779',0,'philimonosward5@gmail.com','juma','aminu','+255745342322',1,0,'2026-06-18 07:17:35.236556','2026-06-18 07:17:35.679064',1,1,2,2),(4,'pbkdf2_sha256$1200000$5nLiOHW0tE0L06625J8Vav$/QJuIZmCKJSQrVklQQ+fl7kAdLjZf3vmOpM5imAzK9Q=','2026-07-03 11:35:37.397928',1,'oswardphilimon@gmail.com','osward','philimon','0768675609',1,1,'2026-06-27 09:43:13.883098','2026-06-27 09:49:24.767926',1,1,3,3),(5,'pbkdf2_sha256$1200000$uxbOwrDPB1uA6QWwWwizDs$H0HDwsocYCm6uUPAut2lxKdeh1BNdo9087QGrU0ZtpY=','2026-07-24 10:02:56.559855',1,'kije@gmail.com','kije','mwambe','0689859255',1,1,'2026-07-03 07:01:16.132311','2026-07-03 07:02:46.249581',NULL,NULL,NULL,1),(6,'pbkdf2_sha256$1200000$xJ9UIz8cPXKqlQxIqdhaOE$PcnMxadSUr9c7oFehneegAHXK8XVDD3qn6SjGRLSZ0Q=',NULL,1,'juma@gmail.com',NULL,NULL,NULL,1,1,'2026-07-24 10:02:08.199213','2026-07-24 10:02:08.587507',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_groups`
--

DROP TABLE IF EXISTS `accounts_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_groups`
--

LOCK TABLES `accounts_user_groups` WRITE;
/*!40000 ALTER TABLE `accounts_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_user_permissions`
--

DROP TABLE IF EXISTS `accounts_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_user_permissions`
--

LOCK TABLES `accounts_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add company',7,'add_company'),(22,'Can change company',7,'change_company'),(23,'Can delete company',7,'delete_company'),(24,'Can view company',7,'view_company'),(25,'Can add branch',6,'add_branch'),(26,'Can change branch',6,'change_branch'),(27,'Can delete branch',6,'delete_branch'),(28,'Can view branch',6,'view_branch'),(29,'Can add department',8,'add_department'),(30,'Can change department',8,'change_department'),(31,'Can delete department',8,'delete_department'),(32,'Can view department',8,'view_department'),(33,'Can add position',9,'add_position'),(34,'Can change position',9,'change_position'),(35,'Can delete position',9,'delete_position'),(36,'Can view position',9,'view_position'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add customer',11,'add_customer'),(42,'Can change customer',11,'change_customer'),(43,'Can delete customer',11,'delete_customer'),(44,'Can view customer',11,'view_customer'),(45,'Can add supplier',12,'add_supplier'),(46,'Can change supplier',12,'change_supplier'),(47,'Can delete supplier',12,'delete_supplier'),(48,'Can view supplier',12,'view_supplier'),(49,'Can add quotation',13,'add_quotation'),(50,'Can change quotation',13,'change_quotation'),(51,'Can delete quotation',13,'delete_quotation'),(52,'Can view quotation',13,'view_quotation'),(53,'Can add quotation item',14,'add_quotationitem'),(54,'Can change quotation item',14,'change_quotationitem'),(55,'Can delete quotation item',14,'delete_quotationitem'),(56,'Can view quotation item',14,'view_quotationitem'),(57,'Can add category',15,'add_category'),(58,'Can change category',15,'change_category'),(59,'Can delete category',15,'delete_category'),(60,'Can view category',15,'view_category'),(61,'Can add unit',19,'add_unit'),(62,'Can change unit',19,'change_unit'),(63,'Can delete unit',19,'delete_unit'),(64,'Can view unit',19,'view_unit'),(65,'Can add product',16,'add_product'),(66,'Can change product',16,'change_product'),(67,'Can delete product',16,'delete_product'),(68,'Can view product',16,'view_product'),(69,'Can add warehouse',20,'add_warehouse'),(70,'Can change warehouse',20,'change_warehouse'),(71,'Can delete warehouse',20,'delete_warehouse'),(72,'Can view warehouse',20,'view_warehouse'),(73,'Can add stock movement',18,'add_stockmovement'),(74,'Can change stock movement',18,'change_stockmovement'),(75,'Can delete stock movement',18,'delete_stockmovement'),(76,'Can view stock movement',18,'view_stockmovement'),(77,'Can add stock',17,'add_stock'),(78,'Can change stock',17,'change_stock'),(79,'Can delete stock',17,'delete_stock'),(80,'Can view stock',17,'view_stock'),(81,'Can add expense category',22,'add_expensecategory'),(82,'Can change expense category',22,'change_expensecategory'),(83,'Can delete expense category',22,'delete_expensecategory'),(84,'Can view expense category',22,'view_expensecategory'),(85,'Can add expense',21,'add_expense'),(86,'Can change expense',21,'change_expense'),(87,'Can delete expense',21,'delete_expense'),(88,'Can view expense',21,'view_expense'),(89,'Can add account type',23,'add_accounttype'),(90,'Can change account type',23,'change_accounttype'),(91,'Can delete account type',23,'delete_accounttype'),(92,'Can view account type',23,'view_accounttype'),(93,'Can add chart of account',24,'add_chartofaccount'),(94,'Can change chart of account',24,'change_chartofaccount'),(95,'Can delete chart of account',24,'delete_chartofaccount'),(96,'Can view chart of account',24,'view_chartofaccount'),(97,'Can add journal entry',25,'add_journalentry'),(98,'Can change journal entry',25,'change_journalentry'),(99,'Can delete journal entry',25,'delete_journalentry'),(100,'Can view journal entry',25,'view_journalentry'),(101,'Can add journal entry line',26,'add_journalentryline'),(102,'Can change journal entry line',26,'change_journalentryline'),(103,'Can delete journal entry line',26,'delete_journalentryline'),(104,'Can view journal entry line',26,'view_journalentryline'),(105,'Can add employee',27,'add_employee'),(106,'Can change employee',27,'change_employee'),(107,'Can delete employee',27,'delete_employee'),(108,'Can view employee',27,'view_employee'),(109,'Can add payroll',28,'add_payroll'),(110,'Can change payroll',28,'change_payroll'),(111,'Can delete payroll',28,'delete_payroll'),(112,'Can view payroll',28,'view_payroll'),(113,'Can add daily cash balance',29,'add_dailycashbalance'),(114,'Can change daily cash balance',29,'change_dailycashbalance'),(115,'Can delete daily cash balance',29,'delete_dailycashbalance'),(116,'Can view daily cash balance',29,'view_dailycashbalance'),(117,'Can add aluminium profile',30,'add_aluminiumprofile'),(118,'Can change aluminium profile',30,'change_aluminiumprofile'),(119,'Can delete aluminium profile',30,'delete_aluminiumprofile'),(120,'Can view aluminium profile',30,'view_aluminiumprofile'),(121,'Can add glass',31,'add_glass'),(122,'Can change glass',31,'change_glass'),(123,'Can delete glass',31,'delete_glass'),(124,'Can view glass',31,'view_glass'),(125,'Can add quotation normal',33,'add_quotationnormal'),(126,'Can change quotation normal',33,'change_quotationnormal'),(127,'Can delete quotation normal',33,'delete_quotationnormal'),(128,'Can view quotation normal',33,'view_quotationnormal'),(129,'Can add quotation item normal',32,'add_quotationitemnormal'),(130,'Can change quotation item normal',32,'change_quotationitemnormal'),(131,'Can delete quotation item normal',32,'delete_quotationitemnormal'),(132,'Can view quotation item normal',32,'view_quotationitemnormal');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_customer`
--

DROP TABLE IF EXISTS `customers_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_type` varchar(20) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `alternative_phone` varchar(20) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `address` longtext,
  `country` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_customer`
--

LOCK TABLES `customers_customer` WRITE;
/*!40000 ALTER TABLE `customers_customer` DISABLE KEYS */;
INSERT INTO `customers_customer` VALUES (1,'individual','osward mwambehile',NULL,'0689859255','0689859255','oswardmwambehile@gmail.com','mbeya mjin\r\nkyela','Tanzania','Dar es Salaam',1,'2026-06-18 07:24:10.260561','2026-06-18 07:24:10.260606'),(2,'individual','HELMAN',NULL,'0704777640',NULL,NULL,'','Tanzania','Dar es Salaam',1,'2026-06-18 11:00:15.760538','2026-06-18 11:00:15.760593'),(3,'individual','MLELWA',NULL,'0689859255','0689859255','oswardmwambehile@gmail.com','mbeya mjin\r\nkyela','Tanzania','Dar es Salaam',1,'2026-06-18 12:53:39.727869','2026-06-18 12:53:39.727904'),(4,'individual','DEOGRATIAS SITE',NULL,'+255767918464',NULL,NULL,'','Tanzania',NULL,1,'2026-07-03 07:12:31.222256','2026-07-03 07:12:31.222281'),(5,'individual','MS Kappa Senses Zanzibar Ltd',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-03 11:33:27.612279','2026-07-03 11:33:27.612315'),(6,'individual','Rafa Company LTD',NULL,'0684824770',NULL,NULL,'','Tanzania',NULL,1,'2026-07-04 09:36:29.049027','2026-07-04 09:36:29.049056'),(7,'individual','Ethics Commissioner',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-04 10:43:50.615027','2026-07-04 10:43:50.615057'),(8,'individual','ZSSF',NULL,NULL,NULL,'oswardmwambehile@gmail.com','mbeya mjin\r\nkyela','Tanzania',NULL,1,'2026-07-04 11:50:43.180175','2026-07-04 11:50:43.180214'),(9,'individual','KIONGOZI KANISA',NULL,'0713500385',NULL,NULL,'','Tanzania',NULL,1,'2026-07-06 06:26:57.190935','2026-07-06 06:26:57.190973'),(10,'individual','Mr. BENJAMINI',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-06 07:34:15.561825','2026-07-06 07:34:15.561851'),(11,'individual','Shanxi Construction Investment Group Company Limited',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-06 09:10:12.688054','2026-07-06 09:10:12.688080'),(12,'individual','Dolfing Engineering',NULL,NULL,NULL,'oswardmwambehile@gmail.com','mbeya mjin\r\nkyela','Tanzania',NULL,1,'2026-07-07 14:10:42.706088','2026-07-07 14:10:42.706110'),(13,'individual','ENG. KASANGA',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-08 08:12:51.216285','2026-07-08 08:12:51.216331'),(14,'individual','mussa',NULL,'07133413699',NULL,NULL,'','Tanzania',NULL,1,'2026-07-09 06:36:40.787084','2026-07-09 06:36:40.787105'),(15,'individual','KIGAMBONI SITE',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-09 09:47:53.740867','2026-07-09 09:47:53.740898'),(16,'individual','Advent Construction Ltd',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-11 08:45:26.877483','2026-07-11 08:45:26.877507'),(17,'individual',':MR JAMES',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-14 07:16:01.653798','2026-07-14 07:16:01.653832'),(18,'individual','Mr Peter',NULL,'0754211999',NULL,NULL,'','Tanzania',NULL,1,'2026-07-14 11:39:48.032593','2026-07-14 11:39:48.032619'),(19,'individual','JCG',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-15 13:19:06.523280','2026-07-15 13:19:06.523307'),(20,'individual','Fundi Wille Site Songea',NULL,'0750009667',NULL,NULL,'','Tanzania',NULL,1,'2026-07-16 07:00:31.747583','2026-07-16 07:58:08.663829'),(21,'individual','FOUNTAIN GATE LTD',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-16 09:19:14.385962','2026-07-16 09:19:14.385993'),(22,'individual','MR IMATOLA',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-16 09:44:17.438355','2026-07-16 09:44:17.438381'),(23,'individual','MR. ABDUL',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-17 11:32:04.400157','2026-07-17 11:32:04.400208'),(24,'individual','KELVIN',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-21 08:56:06.478837','2026-07-21 08:56:06.478881'),(25,'individual','MR. DICKSON',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-21 15:29:14.336689','2026-07-21 15:29:14.336723'),(26,'individual','ROMAN CATHOLIC KIBADA',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-22 06:13:46.979366','2026-07-22 06:13:46.979446'),(27,'individual','Shanxi Cig Company',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-22 11:41:40.615575','2026-07-22 11:41:40.615611'),(28,'individual','Boss Marcello',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-23 07:29:30.097220','2026-07-23 07:29:30.097245'),(29,'individual','Jens Builders',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-24 12:21:43.733076','2026-07-24 12:21:43.733099'),(30,'individual','Mr Jofrey',NULL,NULL,NULL,NULL,'','Tanzania',NULL,1,'2026-07-24 12:45:44.281701','2026-07-24 12:45:44.281737');
/*!40000 ALTER TABLE `customers_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers_supplier`
--

DROP TABLE IF EXISTS `customers_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers_supplier` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) NOT NULL,
  `contact_person` varchar(255) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `alternative_phone` varchar(20) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `tin_number` varchar(100) DEFAULT NULL,
  `vrn_number` varchar(100) DEFAULT NULL,
  `address` longtext,
  `country` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `bank_name` varchar(255) DEFAULT NULL,
  `bank_account_number` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `notes` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers_supplier`
--

LOCK TABLES `customers_supplier` WRITE;
/*!40000 ALTER TABLE `customers_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers_supplier` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-06-08 12:04:47.371723','1','Prince International',1,'[{\"added\": {}}]',7,1),(2,'2026-06-18 06:30:41.416565','1','Mbezi beach(Jogoo)',1,'[{\"added\": {}}]',6,2),(3,'2026-06-18 06:31:24.730569','1','Manager',1,'[{\"added\": {}}]',8,2),(4,'2026-06-18 06:31:55.918013','1','Manager',1,'[{\"added\": {}}]',9,2),(5,'2026-06-18 06:37:59.504780','2','oswardmwambehile@gmail.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Contact\", \"Company\", \"Branch\", \"Department\", \"Position\"]}}]',10,2),(6,'2026-06-27 09:49:24.771866','4','oswardphilimon@gmail.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Contact\", \"Company\", \"Branch\", \"Department\", \"Position\"]}}]',10,4),(7,'2026-07-03 07:02:46.253106','5','kije@gmail.com',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Contact\", \"Position\"]}}]',10,5);
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (23,'accounting','accounttype'),(24,'accounting','chartofaccount'),(25,'accounting','journalentry'),(26,'accounting','journalentryline'),(6,'accounts','branch'),(7,'accounts','company'),(8,'accounts','department'),(9,'accounts','position'),(10,'accounts','user'),(1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'contenttypes','contenttype'),(11,'customers','customer'),(12,'customers','supplier'),(29,'expenses','dailycashbalance'),(21,'expenses','expense'),(22,'expenses','expensecategory'),(15,'inventory','category'),(16,'inventory','product'),(17,'inventory','stock'),(18,'inventory','stockmovement'),(19,'inventory','unit'),(20,'inventory','warehouse'),(27,'payroll','employee'),(28,'payroll','payroll'),(30,'quotations','aluminiumprofile'),(31,'quotations','glass'),(13,'quotations','quotation'),(14,'quotations','quotationitem'),(32,'reports','quotationitemnormal'),(33,'reports','quotationnormal'),(5,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-04 11:40:06.682493'),(2,'contenttypes','0002_remove_content_type_name','2026-06-04 11:40:06.769347'),(3,'auth','0001_initial','2026-06-04 11:40:07.005514'),(4,'auth','0002_alter_permission_name_max_length','2026-06-04 11:40:07.071274'),(5,'auth','0003_alter_user_email_max_length','2026-06-04 11:40:07.078885'),(6,'auth','0004_alter_user_username_opts','2026-06-04 11:40:07.088163'),(7,'auth','0005_alter_user_last_login_null','2026-06-04 11:40:07.095821'),(8,'auth','0006_require_contenttypes_0002','2026-06-04 11:40:07.099087'),(9,'auth','0007_alter_validators_add_error_messages','2026-06-04 11:40:07.108261'),(10,'auth','0008_alter_user_username_max_length','2026-06-04 11:40:07.115614'),(11,'auth','0009_alter_user_last_name_max_length','2026-06-04 11:40:07.122801'),(12,'auth','0010_alter_group_name_max_length','2026-06-04 11:40:07.142061'),(13,'auth','0011_update_proxy_permissions','2026-06-04 11:40:07.150627'),(14,'auth','0012_alter_user_first_name_max_length','2026-06-04 11:40:07.156326'),(15,'accounts','0001_initial','2026-06-04 11:40:07.970098'),(16,'accounts','0002_alter_user_contact','2026-06-04 11:40:07.979185'),(17,'accounting','0001_initial','2026-06-04 11:40:08.415969'),(18,'admin','0001_initial','2026-06-04 11:40:08.553554'),(19,'admin','0002_logentry_remove_auto_add','2026-06-04 11:40:08.563186'),(20,'admin','0003_logentry_add_action_flag_choices','2026-06-04 11:40:08.574686'),(21,'customers','0001_initial','2026-06-04 11:40:08.621766'),(22,'customers','0002_remove_customer_city_remove_customer_district_and_more','2026-06-04 11:40:08.867973'),(23,'expenses','0001_initial','2026-06-04 11:40:09.251056'),(24,'inventory','0001_initial','2026-06-04 11:40:09.832730'),(25,'inventory','0002_alter_stockmovement_reference_id','2026-06-04 11:40:09.896758'),(26,'inventory','0003_stockmovement_note','2026-06-04 11:40:09.956743'),(27,'inventory','0004_category_created_at_unit_created_at','2026-06-04 11:40:10.048718'),(31,'sessions','0001_initial','2026-06-04 11:40:10.563695'),(32,'expenses','0002_expense_branch','2026-06-08 09:03:36.545431'),(33,'payroll','0001_initial','2026-06-09 06:04:37.064066'),(34,'payroll','0002_remove_employee_company_remove_employee_department_and_more','2026-06-09 06:04:37.472763'),(35,'expenses','0003_expense_employee_expense_paid_amount_and_more','2026-06-18 06:15:17.159217'),(36,'expenses','0004_dailycashbalance','2026-06-18 06:15:17.262017'),(37,'customers','0003_alter_customer_phone','2026-06-30 10:31:30.968687'),(45,'inventory','0005_remove_product_barcode_remove_product_buying_price_and_more','2026-07-07 10:38:55.011317'),(47,'inventory','0006_alter_product_name','2026-07-11 08:35:16.071965'),(48,'quotations','0012_alter_quotationitem_aluminium_profile_and_more','2026-07-11 08:35:16.225364'),(49,'inventory','0007_alter_product_name','2026-07-11 08:42:32.412192'),(50,'quotations','0001_initial','2026-07-13 08:45:35.822336'),(51,'quotations','0002_alter_quotationitem_cts','2026-07-13 08:45:35.873155'),(52,'quotations','0003_remove_quotationitem_methodology','2026-07-13 08:45:35.925050'),(53,'quotations','0004_rename_contact_person_quotation_glass_type_and_more','2026-07-13 08:45:36.007123'),(54,'quotations','0005_alter_quotationitem_aluminium_profile','2026-07-13 08:45:36.017978'),(55,'quotations','0006_alter_quotationitem_aluminium_profile','2026-07-13 08:45:36.027837'),(56,'quotations','0007_alter_quotation_customer','2026-07-13 08:45:36.198798'),(57,'quotations','0008_alter_quotationitem_aluminium_profile','2026-07-13 08:45:36.208871'),(58,'quotations','0009_quotation_currency','2026-07-13 08:45:36.299521'),(59,'quotations','0010_alter_quotationitem_quantity','2026-07-13 08:45:36.433387'),(60,'quotations','0011_alter_quotationitem_aluminium_profile_and_more','2026-07-13 08:45:36.452413'),(61,'quotations','0012_aluminiumprofile_glass_alter_quotationitem_product_and_more','2026-07-13 08:45:36.994141'),(62,'reports','0001_initial','2026-07-14 08:50:46.560511');
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
INSERT INTO `django_session` VALUES ('0f5o9pikup72cyscmqp7mynz3yvwiqlb','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1wnCyQ:Q7KzjzJI5XwwQT1IoWqNk7ANkfrdVytUSH4Fz38s-6U','2026-08-07 10:17:46.041559'),('6m0gh6fe6rk9a2z7yjoy0aqwhazqjetj','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1whiLu:fTJ5u4Tr65jl41zyrghwO7nxqCdFhd1sp_If6E7kAQc','2026-07-23 06:35:18.595033'),('71l84madln0qjqn4chqkal9jpqsqcxy6','e30:1wWYd3:5ex0jfSUwCjPT2h6kNztCbj7lgNCLdR6Aaum3_OM1rc','2026-06-22 11:58:53.686485'),('71lz9696mny0p1vqkb6uw4258mus8msx','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1wjAEm:9gUobVUeV6sCZRGjwbFkqM3GqD0CE6gGHT6ecz7_VY0','2026-07-27 06:33:56.017252'),('7qmd1dk7apwn6xq3xfim94wra9dtp3ss','.eJxVjEsOwjAMBe-SNYqcNHEUluw5Q-XYDimgVupnhbg7VOoCtm9m3sv0tK2t3xad-0HM2XTm9LsV4oeOO5A7jbfJ8jSu81DsrtiDLvY6iT4vh_t30Ghp3xp9FMfAqUaHWaEEUo-ARYgrg9fMkXwKoQAjVGaXUbvaAUoK1bF5fwDvgDhM:1waY6l:zVjHToKhIRmqWY2TOZkT8i8-70ZX1qj17Br3BWRcgt0','2026-07-03 12:14:03.443361'),('94i8a4p3qyymmalo7fjkvgtyna35sezn','.eJxVjEsOwjAMBe-SNYqcNHEUluw5Q-XYDimgVupnhbg7VOoCtm9m3sv0tK2t3xad-0HM2XTm9LsV4oeOO5A7jbfJ8jSu81DsrtiDLvY6iT4vh_t30Ghp3xp9FMfAqUaHWaEEUo-ARYgrg9fMkXwKoQAjVGaXUbvaAUoK1bF5fwDvgDhM:1wabg5:yhoCBYx1zcmDAz89BtRX6F6EC5y75n9IqDL4f1ry0_w','2026-07-03 16:02:45.329957'),('b83orwlut8bhiaxqllh4nyveq2d8l70r','e30:1wWYe9:pZb0CJ-GupBPN7PiYfEPrD7WJgLuyWs35tb4gyA_rHA','2026-06-22 12:00:01.717191'),('czarvkun9e77jqm7lkb2n7geep7pf71v','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1wjXKy:hEC2MfI6_NxjfUwtsLJVzNmEwMW-CiVR4FSqPDyMADo','2026-07-28 07:13:52.478648'),('dsf0zb4fa5gkjr1a9kc6amykap8iu7ec','e30:1wedZu:5sxHfcbkVBO0YwzrDh7-632RovnQ7SgyRXdou1K-GdU','2026-07-14 18:53:02.585964'),('jb6y8j93ubeqmmrhq1pwzb6kvd4smf5i','e30:1wWYdX:bvkIrYm1x5SCZZ8RyKyZqsAwsyr7Drm3hkJC_4TuWNQ','2026-06-22 11:59:23.516291'),('kob1x6mwthxnw505y2cumeju8ubbfhe0','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1wmVGA:Z8ZFyytpVZ3-JmPsnjlHsDL-pb7B7CqYw8uXbDIDtJY','2026-08-05 11:37:10.926212'),('m4s52rubnu2olxxce5pi3a5ehiblug5w','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1wmAGa:JvPgYnPcW-iYyGv2yOq28EvVKqAaFhi3GQTQHXiey9k','2026-08-04 13:12:12.159522'),('nq5rte51gyza5d2pmacosjeros6hr6af','e30:1wfwpb:rxWieUv7ijNG0atCW5e-vV_TFYP2aEiloEBWJrklINY','2026-07-18 09:38:39.116915'),('ph2n31iddebzjf1ix1hmifjh3d8syo07','.eJxVjEEOwiAQRe_C2hBohwFcuu8ZCMyMUjVtUtqV8e7apAvd_vfef6mUt7WmrcmSRlZnZdXpdyuZHjLtgO95us2a5mldxqJ3RR-06WFmeV4O9--g5la_tYnsxWWx6IgtBbS9sC_AYLMI9QR9CPHK0VvsAB0gFoRoGCga36F6fwDokzdX:1wWYhc:TEmN3mKSblFY3W30lT9ZeSUAi72pTWojMJK2E6g08D0','2026-06-22 12:03:36.691643'),('qs5hkdqrmoxf3n1xmrljxilkz20an99f','e30:1wfXrH:BGdxtTST9c_KKTRgBMasIIkP3x_mVwzLmQCneUgMuBc','2026-07-17 06:58:43.025030'),('r9avn1kd8tpi2uaqgjs7kc63hnd8cfvo','.eJxVjEEOwiAQRe_C2hBgwhBcuvcMZGAGqZqSlHZlvLs26UK3_733XyrRtra0DVnSxOqsnDr9bpnKQ-Yd8J3mW9elz-syZb0r-qBDXzvL83K4fweNRvvWyIYrGrGGBQzYLFioBhe9QAaI1cUgHsAHYSRrCwihKyiAMZSQ1fsD6t84Ag:1wjzUc:GYOoZQEOcwpAnETKKD_V8UesWhHZy8M6Ta44Ev88tw8','2026-07-29 13:17:42.567294'),('ulel8nw20zljlwroic96gai3xp754m20','e30:1wa718:m5-8_4cKKCkW1Mj4WwnnqFGJMiA49f1u6chYB_AweeY','2026-07-02 07:18:26.797002'),('xxpckaia0kp0cdjqibgemh9ylnvlbf7u','.eJxVjEsOwjAMBe-SNYqcNHEUluw5Q-XYDimgVupnhbg7VOoCtm9m3sv0tK2t3xad-0HM2XTm9LsV4oeOO5A7jbfJ8jSu81DsrtiDLvY6iT4vh_t30Ghp3xp9FMfAqUaHWaEEUo-ARYgrg9fMkXwKoQAjVGaXUbvaAUoK1bF5fwDvgDhM:1waSPW:86vmo0kWOXj4d2HmhI5OvE2NK9kEGKGIbgPBVhl1NlY','2026-07-03 06:09:02.068474'),('ygxjnxr2y80nnd0lpag15qng250kenzd','e30:1wa74S:FjXL8EgdvsHXqFCtEzp772rNX_cmrQAXdp4n7WtL9rQ','2026-07-02 07:21:52.848471');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses_dailycashbalance`
--

DROP TABLE IF EXISTS `expenses_dailycashbalance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses_dailycashbalance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `opening_balance` decimal(18,2) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `expenses_dailycashbalance_company_id_date_2d00e97c_uniq` (`company_id`,`date`),
  CONSTRAINT `expenses_dailycashba_company_id_156b6abf_fk_accounts_` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses_dailycashbalance`
--

LOCK TABLES `expenses_dailycashbalance` WRITE;
/*!40000 ALTER TABLE `expenses_dailycashbalance` DISABLE KEYS */;
/*!40000 ALTER TABLE `expenses_dailycashbalance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses_expense`
--

DROP TABLE IF EXISTS `expenses_expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses_expense` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `expense_number` varchar(100) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext,
  `amount` decimal(18,2) NOT NULL,
  `expense_date` date NOT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `approved_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `approved_by_id` bigint DEFAULT NULL,
  `company_id` bigint NOT NULL,
  `submitted_by_id` bigint DEFAULT NULL,
  `category_id` bigint NOT NULL,
  `branch_id` bigint DEFAULT NULL,
  `employee_id` bigint DEFAULT NULL,
  `paid_amount` decimal(18,2) NOT NULL,
  `remaining_balance` decimal(18,2) NOT NULL,
  `salary_amount` decimal(18,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `expense_number` (`expense_number`),
  KEY `expenses_expense_approved_by_id_8d0bf499_fk_accounts_user_id` (`approved_by_id`),
  KEY `expenses_expense_company_id_8a1baf75_fk_accounts_company_id` (`company_id`),
  KEY `expenses_expense_submitted_by_id_f7efca12_fk_accounts_user_id` (`submitted_by_id`),
  KEY `expenses_expense_category_id_aa33bbdd_fk_expenses_` (`category_id`),
  KEY `expenses_expense_branch_id_8a762cc5_fk_accounts_branch_id` (`branch_id`),
  KEY `expenses_expense_employee_id_ea30dbc0_fk_accounts_user_id` (`employee_id`),
  CONSTRAINT `expenses_expense_approved_by_id_8d0bf499_fk_accounts_user_id` FOREIGN KEY (`approved_by_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `expenses_expense_branch_id_8a762cc5_fk_accounts_branch_id` FOREIGN KEY (`branch_id`) REFERENCES `accounts_branch` (`id`),
  CONSTRAINT `expenses_expense_category_id_aa33bbdd_fk_expenses_` FOREIGN KEY (`category_id`) REFERENCES `expenses_expensecategory` (`id`),
  CONSTRAINT `expenses_expense_company_id_8a1baf75_fk_accounts_company_id` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`),
  CONSTRAINT `expenses_expense_employee_id_ea30dbc0_fk_accounts_user_id` FOREIGN KEY (`employee_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `expenses_expense_submitted_by_id_f7efca12_fk_accounts_user_id` FOREIGN KEY (`submitted_by_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses_expense`
--

LOCK TABLES `expenses_expense` WRITE;
/*!40000 ALTER TABLE `expenses_expense` DISABLE KEYS */;
/*!40000 ALTER TABLE `expenses_expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses_expensecategory`
--

DROP TABLE IF EXISTS `expenses_expensecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses_expensecategory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(50) NOT NULL,
  `description` longtext,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `expenses_expensecategory_company_id_code_f4cfc6ed_uniq` (`company_id`,`code`),
  CONSTRAINT `expenses_expensecate_company_id_dd19f548_fk_accounts_` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses_expensecategory`
--

LOCK TABLES `expenses_expensecategory` WRITE;
/*!40000 ALTER TABLE `expenses_expensecategory` DISABLE KEYS */;
INSERT INTO `expenses_expensecategory` VALUES (1,'Commissions','C','Commissions',1,'2026-06-18 07:11:57.581924','2026-06-18 07:11:57.581946',1);
/*!40000 ALTER TABLE `expenses_expensecategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_category`
--

DROP TABLE IF EXISTS `inventory_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_category`
--

LOCK TABLES `inventory_category` WRITE;
/*!40000 ALTER TABLE `inventory_category` DISABLE KEYS */;
INSERT INTO `inventory_category` VALUES (1,'Aluminium Sliding Window','2026-06-18 06:55:58.764155');
/*!40000 ALTER TABLE `inventory_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_product`
--

DROP TABLE IF EXISTS `inventory_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(1000) NOT NULL,
  `selling_price` decimal(12,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_product`
--

LOCK TABLES `inventory_product` WRITE;
/*!40000 ALTER TABLE `inventory_product` DISABLE KEYS */;
INSERT INTO `inventory_product` VALUES (1,'Aluminium Sliding Window Single Glazing',40000.00),(7,'Glass works at the entire project Kappa Senses Hotel',5000.00),(8,'Entrace Door(Glass Thickness 12mm)12mm Frameless security & Tempered glass',3000.00),(16,'Skylight Structure',300.00),(18,'Aluminium Sliding Window Single Glazing(Tinted Grey)',3000.00),(19,'Aluminium Toilet Door',390.00),(20,'Aluminium Works and Dry wall structure',39.00),(22,'Aluminium Sliding Window Single Glazing Clear 5mm',2000.00),(23,'Normal Aluminium Door.',2000.00),(24,'Frameless balustrades',2000.00),(25,'Chrome Balustrades.',3677.00),(26,'Aluminium Sliding Window H2 Ground Floor',4999.00),(30,'Commercial Building Aluminium window 100x50x1.5mm clear float glass',45.00),(31,'Residetial Building Aluminium window 100x50x1.5mm clear float glass',453.00),(32,'Aluminium Sliding window single grazing white H1',45.00),(33,'Aluminium Sliding window Single glazing white H2',5000.00),(35,'Toilet Window',34.00),(51,'Aluminium Sliding Window Single Glazing Clear 12mm',23.00),(52,'Aluminium Fixed window',24.00),(53,'Aluminium Top hung & fixed window',45.00),(54,'TYPE: W9 (Top hung & Fixed)-2500x11300mm',23.00),(56,'TYPE: W10 (Top Hung)-5770x1,000',23.00),(57,'Aluminium Sliding Window Single Glazing',34.00),(58,'Commercial Building Aluminium window 100x50x1.5mm clear float glass',34.00),(59,'Residetial Building Aluminium window 100x50x1.5mm clear float glass',34.00),(60,'Sensor Door',68.00),(61,'Chrome balustrades.',34.00),(62,'Frameless Tempered balustrades.',45.00),(63,'Frameless Tempered Glass',45.00),(64,'Frameless Tempered Glass Door First Floor.',45.00),(65,'Aluminium  Door.',23.00),(66,'Aluminium Sliding Window Ground Floor',34.00),(67,'Aluminium Sliding Window First Floor',22.00),(68,'Aluminium Sliding Window',45.00),(69,'UPVC Toilet Door.',34.00),(70,'Balcony with Glass',35.00),(71,'Balcony with Gas',45.00),(72,'SkyLight Structure',3.00),(73,'Framless Tempered Glass  (SEHUMU  YA KUABUDIA AND GROTTO)',34.00),(74,'Premium Grey Aluminium Arch Window Double Glazing Float Glass 24Gp 6mm + 6mm+12sp',45.00),(75,'Aluminium Partition Wall System Double MDF Board 6mm With Insullation Door Infill 15mm Eps Foam,Lock,Ironmongery',340.00),(76,'Advance payment request 25% for  Supply and Fix of Aluminium Works  (100*59*1.5mm) for the Proposed Construction of Satellite Village at Dungu Farm, Kigamboni, Temeke Municipality, Dar es Salaam, Lot 3. Contract No. NSSF/W/07/2013-2014.',34.00),(77,'Balcon Balustrades (Glass Balustrade)',34.00),(78,'Stair Case (Glass Balustrade)',24.00),(79,'Front Balcon Balustrades (Glass Balustrade)',45.00),(80,'Back Balcon Balustrades (Glass Balustrade)',67.00);
/*!40000 ALTER TABLE `inventory_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_stock`
--

DROP TABLE IF EXISTS `inventory_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_stock` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `warehouse_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_stock_product_id_b75f69ba_fk_inventory_product_id` (`product_id`),
  KEY `inventory_stock_warehouse_id_2fd6d240_fk_inventory_warehouse_id` (`warehouse_id`),
  CONSTRAINT `inventory_stock_product_id_b75f69ba_fk_inventory_product_id` FOREIGN KEY (`product_id`) REFERENCES `inventory_product` (`id`),
  CONSTRAINT `inventory_stock_warehouse_id_2fd6d240_fk_inventory_warehouse_id` FOREIGN KEY (`warehouse_id`) REFERENCES `inventory_warehouse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_stock`
--

LOCK TABLES `inventory_stock` WRITE;
/*!40000 ALTER TABLE `inventory_stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_stockmovement`
--

DROP TABLE IF EXISTS `inventory_stockmovement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_stockmovement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `movement_type` varchar(20) NOT NULL,
  `reference_type` varchar(100) NOT NULL,
  `reference_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  `balance_after` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `product_id` bigint NOT NULL,
  `warehouse_id` bigint NOT NULL,
  `note` longtext,
  PRIMARY KEY (`id`),
  KEY `inventory_stockmovem_created_by_id_9a39cb99_fk_accounts_` (`created_by_id`),
  KEY `inventory_stockmovem_product_id_4eccfd0a_fk_inventory` (`product_id`),
  KEY `inventory_stockmovem_warehouse_id_401c7fc4_fk_inventory` (`warehouse_id`),
  CONSTRAINT `inventory_stockmovem_created_by_id_9a39cb99_fk_accounts_` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `inventory_stockmovem_product_id_4eccfd0a_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_product` (`id`),
  CONSTRAINT `inventory_stockmovem_warehouse_id_401c7fc4_fk_inventory` FOREIGN KEY (`warehouse_id`) REFERENCES `inventory_warehouse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_stockmovement`
--

LOCK TABLES `inventory_stockmovement` WRITE;
/*!40000 ALTER TABLE `inventory_stockmovement` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_stockmovement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_unit`
--

DROP TABLE IF EXISTS `inventory_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_unit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_unit`
--

LOCK TABLES `inventory_unit` WRITE;
/*!40000 ALTER TABLE `inventory_unit` DISABLE KEYS */;
INSERT INTO `inventory_unit` VALUES (1,'Piece','Pc','2026-06-18 06:56:20.155151');
/*!40000 ALTER TABLE `inventory_unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_warehouse`
--

DROP TABLE IF EXISTS `inventory_warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_warehouse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `manager_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_warehouse_manager_id_6def176a_fk_accounts_user_id` (`manager_id`),
  CONSTRAINT `inventory_warehouse_manager_id_6def176a_fk_accounts_user_id` FOREIGN KEY (`manager_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_warehouse`
--

LOCK TABLES `inventory_warehouse` WRITE;
/*!40000 ALTER TABLE `inventory_warehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_warehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payroll_employee`
--

DROP TABLE IF EXISTS `payroll_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payroll_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employee_id` varchar(100) NOT NULL,
  `salary` decimal(18,2) NOT NULL,
  `hire_date` date NOT NULL,
  `employment_status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_id` (`employee_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `payroll_employee_user_id_ea80fd24_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payroll_employee`
--

LOCK TABLES `payroll_employee` WRITE;
/*!40000 ALTER TABLE `payroll_employee` DISABLE KEYS */;
INSERT INTO `payroll_employee` VALUES (1,'001',70000.00,'2026-06-27','active','2026-06-27 11:25:48.201307','2026-06-27 11:25:48.201380',1),(2,'002',600000.00,'2026-06-27','active','2026-06-27 11:26:13.589481','2026-06-27 11:26:13.589506',3),(3,'003',50000.00,'2026-06-27','active','2026-06-27 11:26:47.887210','2026-06-27 11:26:47.887235',4);
/*!40000 ALTER TABLE `payroll_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payroll_payroll`
--

DROP TABLE IF EXISTS `payroll_payroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payroll_payroll` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `payroll_number` varchar(100) NOT NULL,
  `basic_salary` decimal(18,2) NOT NULL,
  `allowance` decimal(18,2) NOT NULL,
  `deduction` decimal(18,2) NOT NULL,
  `tax` decimal(18,2) NOT NULL,
  `net_salary` decimal(18,2) NOT NULL,
  `payroll_month` int NOT NULL,
  `payroll_year` int NOT NULL,
  `status` varchar(20) NOT NULL,
  `processed_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `company_id` bigint NOT NULL,
  `employee_id` bigint NOT NULL,
  `processed_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `payroll_number` (`payroll_number`),
  KEY `payroll_payroll_company_id_54bc489f_fk_accounts_company_id` (`company_id`),
  KEY `payroll_payroll_employee_id_cd24ccf6_fk_payroll_employee_id` (`employee_id`),
  KEY `payroll_payroll_processed_by_id_7d2d497c_fk_accounts_user_id` (`processed_by_id`),
  CONSTRAINT `payroll_payroll_company_id_54bc489f_fk_accounts_company_id` FOREIGN KEY (`company_id`) REFERENCES `accounts_company` (`id`),
  CONSTRAINT `payroll_payroll_employee_id_cd24ccf6_fk_payroll_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `payroll_employee` (`id`),
  CONSTRAINT `payroll_payroll_processed_by_id_7d2d497c_fk_accounts_user_id` FOREIGN KEY (`processed_by_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payroll_payroll`
--

LOCK TABLES `payroll_payroll` WRITE;
/*!40000 ALTER TABLE `payroll_payroll` DISABLE KEYS */;
INSERT INTO `payroll_payroll` VALUES (1,'PAY00001',600000.00,0.00,0.00,0.00,600000.00,6,2026,'draft',NULL,'2026-06-27 11:28:22.380053','2026-06-27 11:28:22.380103',1,2,4),(2,'PAY00002',50000.00,0.00,0.00,0.00,50000.00,6,2026,'draft',NULL,'2026-06-27 11:29:52.846776','2026-06-27 11:29:52.846811',1,3,4),(3,'PAY00003',70000.00,0.00,0.00,0.00,70000.00,6,2026,'draft',NULL,'2026-06-27 11:30:31.322016','2026-06-27 11:30:31.322089',1,1,4);
/*!40000 ALTER TABLE `payroll_payroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotations_aluminiumprofile`
--

DROP TABLE IF EXISTS `quotations_aluminiumprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotations_aluminiumprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotations_aluminiumprofile`
--

LOCK TABLES `quotations_aluminiumprofile` WRITE;
/*!40000 ALTER TABLE `quotations_aluminiumprofile` DISABLE KEYS */;
INSERT INTO `quotations_aluminiumprofile` VALUES (2,'Al Pro 80mm'),(5,'Al Pro 80mm Black'),(13,'EPPP 100mm'),(4,'Metal Al Pro 100mm'),(1,'Metal Al Pro 100mm Grey'),(11,'Metal Al Pro 80mm Grey'),(6,'Metal Al Profile 100mm Grey'),(7,'Metal Al Profile 100mm Light Yellow'),(8,'Metal U Channel'),(9,'Metal: Grey alminium profile 100mm.'),(12,'Tempered Glass'),(10,'UPVC Pro');
/*!40000 ALTER TABLE `quotations_aluminiumprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotations_glass`
--

DROP TABLE IF EXISTS `quotations_glass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotations_glass` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotations_glass`
--

LOCK TABLES `quotations_glass` WRITE;
/*!40000 ALTER TABLE `quotations_glass` DISABLE KEYS */;
INSERT INTO `quotations_glass` VALUES (16,'12mm'),(4,'12mm Laminated glazing bronze'),(3,'5mm clear,5m one way grey'),(12,'5mm Grey'),(8,'6mm Clear Float Glass'),(2,'6mm Grey'),(6,'6mm Tinted grey'),(15,'6mm+6mm =12mm'),(9,'Ballistic glass  22mm GP'),(5,'Ballistic glass EN 1522;Rating S55 DFL; glass option 22mm GP'),(7,'Frosted 6mm'),(10,'Glass Clear 12mm'),(13,'Glass Single Glazing Tinted grey 5mm'),(14,'Single Glazing Tinted grey 5mm');
/*!40000 ALTER TABLE `quotations_glass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotations_quotation`
--

DROP TABLE IF EXISTS `quotations_quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotations_quotation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quotation_no` varchar(100) NOT NULL,
  `profile_type` varchar(255) NOT NULL,
  `project_location` varchar(255) NOT NULL,
  `glass_type` varchar(255) NOT NULL,
  `quotation_date` date NOT NULL,
  `vat_included` tinyint(1) NOT NULL,
  `vat_percentage` decimal(5,2) NOT NULL,
  `subtotal` decimal(15,2) NOT NULL,
  `discount_amount` decimal(15,2) NOT NULL,
  `tax_amount` decimal(15,2) NOT NULL,
  `grand_total` decimal(15,2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `customer_id` bigint DEFAULT NULL,
  `sales_person_id` bigint DEFAULT NULL,
  `currency` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quotation_no` (`quotation_no`),
  KEY `quotations_quotation_created_by_id_f86a7566_fk_accounts_user_id` (`created_by_id`),
  KEY `quotations_quotation_sales_person_id_2ae63ba7_fk_accounts_` (`sales_person_id`),
  KEY `quotations_quotation_customer_id_e30770ba_fk_customers` (`customer_id`),
  CONSTRAINT `quotations_quotation_created_by_id_f86a7566_fk_accounts_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `quotations_quotation_customer_id_e30770ba_fk_customers` FOREIGN KEY (`customer_id`) REFERENCES `customers_customer` (`id`),
  CONSTRAINT `quotations_quotation_sales_person_id_2ae63ba7_fk_accounts_` FOREIGN KEY (`sales_person_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotations_quotation`
--

LOCK TABLES `quotations_quotation` WRITE;
/*!40000 ALTER TABLE `quotations_quotation` DISABLE KEYS */;
INSERT INTO `quotations_quotation` VALUES (1,'QT-2026-0001','','Dar es Salaam','','2026-07-14',0,18.00,12242500.00,0.00,0.00,12242500.00,'Draft','2026-07-14 08:11:33.150019','2026-07-14 08:14:18.967648',2,17,NULL,'TZS'),(2,'QT-2026-0002','','Dar es Salaam','','2026-07-15',1,18.00,49518150.00,0.00,8913267.00,58431417.00,'Draft','2026-07-15 13:21:10.619730','2026-07-15 14:20:07.795677',2,19,NULL,'TZS'),(3,'QT-2026-0003','','Mwanza','','2026-07-16',0,18.00,15680000.00,0.00,0.00,15680000.00,'Draft','2026-07-16 07:33:18.789515','2026-07-16 07:42:23.570195',2,20,NULL,'TZS'),(4,'QT-2026-0004','','Dodoma','','2026-07-16',0,18.00,32500000.00,0.00,0.00,32500000.00,'Draft','2026-07-16 09:20:48.068666','2026-07-16 09:25:03.074765',2,21,NULL,'TZS'),(5,'QT-2026-0005','','','','2026-07-16',0,18.00,128310000.00,0.00,0.00,128310000.00,'Draft','2026-07-16 10:59:02.238313','2026-07-20 16:18:22.178495',2,22,NULL,'TZS'),(6,'QT-2026-0006','','Dar es Salaam','','2026-07-16',0,18.00,14232000.00,0.00,0.00,14232000.00,'Draft','2026-07-16 12:43:48.432638','2026-07-16 12:43:48.432653',2,14,NULL,'TZS'),(7,'QT-2026-0007','','','','2026-07-16',0,18.00,6750000.00,0.00,0.00,6750000.00,'Draft','2026-07-16 13:03:26.197939','2026-07-16 13:03:26.197969',2,14,NULL,'TZS'),(8,'QT-2026-0008','','Dar es Salaam','','2026-07-11',1,18.00,459840000.00,0.00,82771200.00,542611200.00,'Draft','2026-07-16 13:28:22.305486','2026-07-24 09:08:39.506482',2,16,NULL,'TZS'),(9,'QT-2026-0009','','P.O.BOX, DODOMA,','','2026-07-17',0,18.00,6325000.00,0.00,0.00,6325000.00,'Draft','2026-07-17 11:40:05.504794','2026-07-17 13:58:21.529598',2,23,NULL,'TZS'),(10,'QT-2026-0010','','Dodoma','','2026-07-17',0,18.00,11385000.00,0.00,0.00,11385000.00,'Draft','2026-07-17 11:51:45.537470','2026-07-17 11:53:33.464432',2,23,NULL,'TZS'),(11,'QT-2026-0011','','Dodoma','','2026-07-17',0,18.00,22230000.00,0.00,0.00,22230000.00,'Draft','2026-07-17 12:13:20.977852','2026-07-17 12:13:20.977869',2,23,NULL,'TZS'),(12,'QT-2026-0012','','Dodoma','','2026-07-17',1,18.00,2675000.00,0.00,481500.00,3156500.00,'Draft','2026-07-17 12:51:06.073354','2026-07-17 12:57:24.789488',2,23,NULL,'TZS'),(13,'QT-2026-0013','','Dodoma','','2026-07-17',0,18.00,2976000.00,0.00,0.00,2976000.00,'Draft','2026-07-17 13:22:40.759523','2026-07-18 15:18:45.765858',2,23,NULL,'TZS'),(14,'QT-2026-0014','','Dodoma','','2026-07-17',0,18.00,2625000.00,0.00,0.00,2625000.00,'Draft','2026-07-17 13:42:42.036003','2026-07-17 13:42:42.036019',2,23,NULL,'TZS'),(15,'QT-2026-0015','','Dodoma','','2026-07-18',0,18.00,8000000.00,0.00,0.00,8000000.00,'Draft','2026-07-18 14:19:15.737021','2026-07-18 14:19:41.185000',2,23,NULL,'TZS'),(16,'QT-2026-0016','','Dodoma','','2026-07-18',0,18.00,26010000.00,0.00,0.00,26010000.00,'Draft','2026-07-18 14:29:48.168597','2026-07-18 14:30:07.074795',2,23,NULL,'TZS'),(17,'QT-2026-0017','','Dodoma','','2026-07-18',0,18.00,12540000.00,0.00,0.00,12540000.00,'Draft','2026-07-18 14:49:37.024202','2026-07-21 13:13:47.850709',2,23,NULL,'TZS'),(18,'QT-2026-0018','','Dodoma','','2026-07-20',0,18.00,33750000.00,0.00,0.00,33750000.00,'Draft','2026-07-20 16:55:47.290322','2026-07-20 16:58:47.388432',2,22,NULL,'TZS'),(19,'QT-2026-0019','','Dodoma','','2026-07-21',0,18.00,3792000.00,0.00,0.00,3792000.00,'Draft','2026-07-21 09:07:58.677749','2026-07-21 09:52:50.759665',2,24,NULL,'TZS'),(20,'QT-2026-0020','','Dodoma','','2026-07-21',0,18.00,18072000.00,0.00,0.00,18072000.00,'Draft','2026-07-21 16:33:24.587452','2026-07-21 16:50:33.749124',2,25,NULL,'TZS'),(21,'QT-2026-0021','','Dar es Salaam','','2026-07-22',0,18.00,49075000.00,0.00,0.00,49075000.00,'Draft','2026-07-22 06:20:45.375697','2026-07-22 06:20:45.375762',2,26,NULL,'TZS'),(22,'QT-2026-0022','','Dar es Salaam','','2026-07-22',1,18.00,109200000.00,0.00,19656000.00,128856000.00,'Draft','2026-07-22 11:44:17.454836','2026-07-22 11:44:17.454851',2,27,NULL,'TZS'),(23,'QT-2026-0023','','Dar es Salaam','','2026-07-22',0,18.00,135652800.00,0.00,0.00,135652800.00,'Draft','2026-07-22 19:51:11.072043','2026-07-24 11:43:13.490185',2,16,NULL,'TZS'),(24,'QT-2026-0024','','Dodoma','','2026-07-23',0,18.00,73547000.00,0.00,0.00,73547000.00,'Draft','2026-07-23 12:50:29.862249','2026-07-23 12:50:29.862265',2,28,NULL,'TZS'),(25,'QT-2026-0025','','Dar es Salaam','','2026-07-24',0,18.00,24480000.00,0.00,0.00,24480000.00,'Draft','2026-07-24 12:26:51.069974','2026-07-24 13:06:25.143908',2,29,NULL,'TZS'),(26,'QT-2026-0026','','','','2026-07-24',0,18.00,11880000.00,0.00,0.00,11880000.00,'Draft','2026-07-24 12:49:34.802111','2026-07-24 13:03:15.643926',2,30,NULL,'TZS');
/*!40000 ALTER TABLE `quotations_quotation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotations_quotationitem`
--

DROP TABLE IF EXISTS `quotations_quotationitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotations_quotationitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_code` varchar(100) NOT NULL,
  `aluminium_profile_id` bigint DEFAULT NULL,
  `glass_id` bigint DEFAULT NULL,
  `width` decimal(10,2) NOT NULL,
  `height` decimal(10,2) NOT NULL,
  `quantity` decimal(10,2) NOT NULL,
  `sqm` decimal(10,2) NOT NULL,
  `total_sqm` decimal(10,2) NOT NULL,
  `unit_price` decimal(15,2) NOT NULL,
  `total_price` decimal(15,2) NOT NULL,
  `cts` decimal(10,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `product_id` bigint DEFAULT NULL,
  `quotation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quotations_quotation_quotation_id_9791bda3_fk_quotation` (`quotation_id`),
  KEY `quotations_quotation_product_id_3ac5d6a5_fk_inventory` (`product_id`),
  KEY `quotations_quotationitem_aluminium_profile_id_92cd842e` (`aluminium_profile_id`),
  KEY `quotations_quotationitem_glass_id_66fd7c3f` (`glass_id`),
  CONSTRAINT `quotations_quotation_aluminium_profile_id_92cd842e_fk_quotation` FOREIGN KEY (`aluminium_profile_id`) REFERENCES `quotations_aluminiumprofile` (`id`),
  CONSTRAINT `quotations_quotation_glass_id_66fd7c3f_fk_quotation` FOREIGN KEY (`glass_id`) REFERENCES `quotations_glass` (`id`),
  CONSTRAINT `quotations_quotation_product_id_3ac5d6a5_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_product` (`id`),
  CONSTRAINT `quotations_quotation_quotation_id_9791bda3_fk_quotation` FOREIGN KEY (`quotation_id`) REFERENCES `quotations_quotation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=457 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotations_quotationitem`
--

LOCK TABLES `quotations_quotationitem` WRITE;
/*!40000 ALTER TABLE `quotations_quotationitem` DISABLE KEYS */;
INSERT INTO `quotations_quotationitem` VALUES (1,'A01',2,3,1455.00,1980.00,1.00,2.90,3.00,125000.00,375000.00,0.00,'2026-07-14 08:11:33.165194',32,1),(2,'A02',2,3,1780.00,1985.00,1.00,3.50,4.00,125000.00,500000.00,0.00,'2026-07-14 08:11:33.173384',32,1),(3,'A03',2,3,1990.00,1680.00,1.00,3.30,3.30,125000.00,412500.00,0.00,'2026-07-14 08:11:33.180449',32,1),(4,'A04',2,3,1790.00,1720.00,1.00,3.10,3.10,125000.00,387500.00,0.00,'2026-07-14 08:11:33.187326',32,1),(5,'A05',2,3,795.00,720.00,1.00,0.60,1.00,125000.00,125000.00,0.00,'2026-07-14 08:11:33.193213',32,1),(6,'A06',2,3,1780.00,1695.00,1.00,3.00,3.00,125000.00,375000.00,0.00,'2026-07-14 08:11:33.199787',32,1),(7,'A07',2,3,1180.00,1450.00,1.00,1.70,2.00,125000.00,250000.00,0.00,'2026-07-14 08:11:33.206364',32,1),(8,'A08',2,3,1760.00,1695.00,1.00,3.00,3.00,125000.00,375000.00,0.00,'2026-07-14 08:11:33.213519',32,1),(9,'A09',2,3,1785.00,1740.00,1.00,3.10,3.10,125000.00,387500.00,0.00,'2026-07-14 08:11:33.219868',32,1),(10,'A10',2,3,770.00,740.00,1.00,0.60,1.00,125000.00,125000.00,0.00,'2026-07-14 08:11:33.226635',32,1),(11,'A11',2,3,1775.00,1740.00,1.00,3.10,3.10,125000.00,387500.00,0.00,'2026-07-14 08:11:33.233089',32,1),(12,'A12',2,3,1960.00,1985.00,1.00,3.90,4.00,125000.00,500000.00,0.00,'2026-07-14 08:11:33.239879',33,1),(13,'A13',2,3,1970.00,1990.00,1.00,3.90,4.00,125000.00,500000.00,0.00,'2026-07-14 08:11:33.246485',33,1),(14,'A14',2,3,1770.00,1470.00,1.00,2.60,3.00,125000.00,375000.00,0.00,'2026-07-14 08:11:33.262169',33,1),(15,'A15',2,3,2445.00,2825.00,1.00,6.90,7.00,125000.00,875000.00,0.00,'2026-07-14 08:11:33.270402',33,1),(16,'A16',2,3,735.00,730.00,1.00,0.50,1.00,125000.00,125000.00,0.00,'2026-07-14 08:11:33.277314',33,1),(17,'A17',2,3,1970.00,1720.00,1.00,3.40,3.40,125000.00,425000.00,0.00,'2026-07-14 08:11:33.284137',33,1),(18,'A18',2,3,730.00,720.00,1.00,0.50,1.00,125000.00,125000.00,0.00,'2026-07-14 08:11:33.290383',33,1),(19,'A19',2,3,1970.00,1710.00,1.00,3.40,3.40,125000.00,425000.00,0.00,'2026-07-14 08:11:33.296814',33,1),(20,'A20',2,3,980.00,715.00,1.00,0.70,1.00,125000.00,125000.00,0.00,'2026-07-14 08:11:33.303939',33,1),(21,'A21',2,3,1980.00,1715.00,1.00,3.40,3.40,125000.00,425000.00,0.00,'2026-07-14 08:11:33.310582',33,1),(22,'A22',2,3,1955.00,1710.00,1.00,3.30,3.30,125000.00,412500.00,0.00,'2026-07-14 08:11:33.317191',33,1),(23,'A23',2,3,1985.00,2575.00,1.00,5.10,5.10,900000.00,900000.00,0.00,'2026-07-14 08:11:33.324290',NULL,1),(24,'A24',2,3,2010.00,2600.00,1.00,5.20,5.20,900000.00,900000.00,0.00,'2026-07-14 08:11:33.330850',NULL,1),(25,'A25',2,3,2980.00,2600.00,1.00,7.70,7.70,900000.00,900000.00,0.00,'2026-07-14 08:11:33.337328',NULL,1),(26,'A26',2,3,885.00,2610.00,1.00,2.30,2.30,450000.00,450000.00,0.00,'2026-07-14 08:11:33.343403',19,1),(27,'A27',2,3,770.00,2505.00,1.00,1.90,1.90,450000.00,450000.00,0.00,'2026-07-14 08:11:33.349457',19,1),(28,'A28',2,3,780.00,2500.00,1.00,1.90,1.90,450000.00,450000.00,0.00,'2026-07-14 08:11:33.355858',19,1),(29,'A29',2,3,770.00,775.00,1.00,0.60,1.00,180000.00,180000.00,0.00,'2026-07-14 08:11:33.362315',35,1),(30,'A01',NULL,NULL,0.00,0.00,1.00,1.00,1.00,49518150.00,49518150.00,0.00,'2026-07-15 13:21:10.624634',NULL,2),(31,'A01',NULL,NULL,0.00,0.00,1.00,10.50,11.00,1200000.00,13200000.00,0.00,'2026-07-16 07:33:18.793067',NULL,3),(32,'A02',NULL,NULL,0.00,0.00,1.00,1.00,1.00,250000.00,250000.00,0.00,'2026-07-16 07:33:18.802187',NULL,3),(33,'A03',NULL,NULL,0.00,0.00,1.00,1.00,1.00,350000.00,350000.00,0.00,'2026-07-16 07:33:18.810652',NULL,3),(34,'A04',NULL,NULL,0.00,0.00,1.00,1.00,1.00,550000.00,550000.00,0.00,'2026-07-16 07:33:18.817576',NULL,3),(35,'A05',NULL,NULL,0.00,0.00,1.00,1.00,1.00,950000.00,950000.00,0.00,'2026-07-16 07:33:18.824548',NULL,3),(36,'A06',NULL,NULL,0.00,0.00,1.00,1.00,1.00,30000.00,30000.00,0.00,'2026-07-16 07:33:18.830926',NULL,3),(37,'A07',NULL,NULL,0.00,0.00,1.00,1.00,1.00,350000.00,350000.00,0.00,'2026-07-16 07:33:18.837333',NULL,3),(38,'A01',NULL,NULL,0.00,0.00,1.00,50.00,50.00,650000.00,32500000.00,0.00,'2026-07-16 09:20:48.072543',NULL,4),(39,'A01',4,4,4400.00,3625.00,1.00,16.00,16.00,250000.00,4000000.00,0.00,'2026-07-16 10:59:02.254279',53,5),(40,'A02',4,4,3000.00,3050.00,1.00,9.20,9.20,250000.00,2300000.00,0.00,'2026-07-16 10:59:02.261588',53,5),(41,'A03',4,4,2500.00,11300.00,1.00,28.30,28.30,250000.00,7075000.00,0.00,'2026-07-16 10:59:02.268511',53,5),(42,'A04',4,9,2500.00,11300.00,1.00,28.30,28.30,450000.00,12735000.00,0.00,'2026-07-16 10:59:02.276232',53,5),(43,'A05',4,4,14100.00,3175.00,1.00,44.80,45.00,250000.00,11250000.00,0.00,'2026-07-16 10:59:02.282279',53,5),(44,'A06',4,4,3200.00,7300.00,1.00,23.40,23.40,250000.00,5850000.00,0.00,'2026-07-16 10:59:02.288488',53,5),(45,'A07',4,4,5770.00,1000.00,1.00,5.80,6.00,250000.00,1500000.00,0.00,'2026-07-16 10:59:02.295451',53,5),(46,'A08',4,4,7800.00,3175.00,1.00,24.80,25.00,250000.00,6250000.00,0.00,'2026-07-16 10:59:02.302108',53,5),(47,'A09',4,4,12000.00,3175.00,1.00,38.10,38.10,250000.00,9525000.00,0.00,'2026-07-16 10:59:02.308838',53,5),(48,'A10',4,4,1750.00,11800.00,1.00,20.70,21.00,250000.00,5250000.00,0.00,'2026-07-16 10:59:02.315248',53,5),(49,'A11',4,4,1750.00,9300.00,1.00,16.30,16.30,250000.00,4075000.00,0.00,'2026-07-16 10:59:02.322182',53,5),(50,'A12',4,4,14100.00,3175.00,1.00,44.80,45.00,250000.00,11250000.00,0.00,'2026-07-16 10:59:02.328754',53,5),(51,'A13',4,4,14000.00,3050.00,1.00,42.70,43.00,250000.00,10750000.00,0.00,'2026-07-16 10:59:02.335042',53,5),(52,'A14',4,4,1500.00,7300.00,1.00,11.00,11.00,250000.00,2750000.00,0.00,'2026-07-16 10:59:02.341739',53,5),(53,'A15',4,4,2000.00,5276.00,1.00,10.60,11.00,250000.00,2750000.00,0.00,'2026-07-16 10:59:02.348089',53,5),(54,'A16',4,4,900.00,7300.00,1.00,6.60,7.00,250000.00,1750000.00,0.00,'2026-07-16 10:59:02.354736',53,5),(55,'A17',4,4,1500.00,1500.00,1.00,2.30,2.30,250000.00,575000.00,0.00,'2026-07-16 10:59:02.361488',53,5),(56,'A18',4,4,900.00,1500.00,1.00,1.40,1.40,250000.00,350000.00,0.00,'2026-07-16 10:59:02.368161',53,5),(57,'A19',4,4,1500.00,1925.00,1.00,2.90,3.00,250000.00,750000.00,0.00,'2026-07-16 10:59:02.374639',53,5),(58,'A20',4,3,800.00,2925.00,1.00,2.30,2.30,250000.00,575000.00,0.00,'2026-07-16 10:59:02.381070',53,5),(59,'A01',5,6,1710.00,1900.00,1.00,3.20,3.20,120000.00,384000.00,0.00,'2026-07-16 12:43:48.451269',1,6),(60,'A02',5,6,1070.00,1900.00,1.00,2.00,2.00,120000.00,240000.00,0.00,'2026-07-16 12:43:48.458516',1,6),(61,'A03',5,6,920.00,1200.00,1.00,1.10,1.10,120000.00,132000.00,0.00,'2026-07-16 12:43:48.471379',1,6),(62,'A04',5,6,900.00,980.00,1.00,0.90,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.477828',1,6),(63,'A05',5,6,820.00,980.00,1.00,0.80,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.484546',1,6),(64,'A06',5,6,1480.00,1900.00,1.00,2.80,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.491004',1,6),(65,'A07',5,6,2000.00,1880.00,1.00,3.80,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.496819',1,6),(66,'A08',5,6,1500.00,1970.00,1.00,3.00,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.503450',1,6),(67,'A09',5,6,760.00,1900.00,1.00,1.40,1.40,120000.00,168000.00,0.00,'2026-07-16 12:43:48.510050',1,6),(68,'A10',5,6,1960.00,1920.00,1.00,3.80,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.516027',1,6),(69,'A11',5,6,980.00,1200.00,1.00,1.20,1.20,120000.00,144000.00,0.00,'2026-07-16 12:43:48.522040',1,6),(70,'A12',5,6,950.00,1060.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.528082',1,6),(71,'A13',5,6,600.00,680.00,1.00,0.40,0.40,120000.00,48000.00,0.00,'2026-07-16 12:43:48.533990',1,6),(72,'A14',5,6,2000.00,1940.00,1.00,3.90,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.539675',1,6),(73,'A15',4,6,1970.00,1910.00,1.00,3.80,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.546417',1,6),(74,'A16',5,6,1520.00,1950.00,1.00,3.00,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.552512',1,6),(75,'A17',5,6,960.00,1070.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.558736',1,6),(76,'A18',5,6,1920.00,1800.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.565550',1,6),(77,'A19',5,6,790.00,1820.00,1.00,1.40,1.40,120000.00,168000.00,0.00,'2026-07-16 12:43:48.572807',1,6),(78,'A20',5,6,900.00,1300.00,1.00,1.20,1.20,120000.00,144000.00,0.00,'2026-07-16 12:43:48.579001',1,6),(79,'A21',5,6,900.00,940.00,1.00,0.80,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.585960',1,6),(80,'A22',5,6,950.00,970.00,1.00,0.90,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.591828',1,6),(81,'A23',5,6,1700.00,1830.00,1.00,3.10,3.10,120000.00,372000.00,0.00,'2026-07-16 12:43:48.598013',1,6),(82,'A24',5,6,2030.00,1830.00,1.00,3.70,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.603998',1,6),(83,'A25',5,6,2030.00,1860.00,1.00,3.80,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.609928',1,6),(84,'A26',5,6,600.00,610.00,1.00,0.40,0.40,120000.00,48000.00,0.00,'2026-07-16 12:43:48.616911',1,6),(85,'A27',5,6,1620.00,1810.00,1.00,2.90,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.623024',1,6),(86,'A28',5,6,1020.00,1800.00,1.00,1.80,2.00,120000.00,240000.00,0.00,'2026-07-16 12:43:48.631095',1,6),(87,'A29',5,6,970.00,1290.00,1.00,1.30,1.30,120000.00,156000.00,0.00,'2026-07-16 12:43:48.638497',1,6),(88,'A30',5,6,940.00,1010.00,1.00,0.90,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.644766',1,6),(89,'A31',5,6,950.00,1030.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.651067',1,6),(90,'A32',5,6,1520.00,1840.00,1.00,2.80,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.657010',1,6),(91,'A33',5,6,2040.00,1850.00,1.00,3.80,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.670056',1,6),(92,'A34',5,6,1540.00,1840.00,1.00,2.80,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.676415',1,6),(93,'A35',5,6,1950.00,1730.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-16 12:43:48.684543',1,6),(94,'A36',5,6,810.00,1700.00,1.00,1.40,1.40,120000.00,168000.00,0.00,'2026-07-16 12:43:48.691685',1,6),(95,'A37',5,6,1200.00,1520.00,1.00,1.80,2.00,120000.00,240000.00,0.00,'2026-07-16 12:43:48.698725',1,6),(96,'A38',5,6,980.00,1200.00,1.00,1.20,1.20,120000.00,144000.00,0.00,'2026-07-16 12:43:48.705258',1,6),(97,'A39',5,6,880.00,1210.00,1.00,1.10,1.10,120000.00,132000.00,0.00,'2026-07-16 12:43:48.711935',1,6),(98,'A40',5,6,830.00,1740.00,1.00,1.40,1.40,120000.00,168000.00,0.00,'2026-07-16 12:43:48.718031',1,6),(99,'A41',5,6,2080.00,1740.00,1.00,3.60,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.724444',1,6),(100,'A42',5,6,2030.00,1730.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.733039',1,6),(101,'A43',5,6,600.00,600.00,1.00,0.40,0.40,120000.00,48000.00,0.00,'2026-07-16 12:43:48.741393',1,6),(102,'A44',5,6,2030.00,1740.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.750315',1,6),(103,'A45',5,6,1100.00,1730.00,1.00,1.90,2.00,120000.00,240000.00,0.00,'2026-07-16 12:43:48.758769',1,6),(104,'A46',5,6,1730.00,1730.00,1.00,3.00,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.767413',1,6),(105,'A47',5,6,1170.00,1530.00,1.00,1.80,2.00,120000.00,240000.00,0.00,'2026-07-16 12:43:48.775482',1,6),(106,'A48',5,6,900.00,1020.00,1.00,0.90,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.782362',1,6),(107,'A49',5,6,950.00,1010.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-16 12:43:48.789526',1,6),(108,'A50',5,6,1540.00,1750.00,1.00,2.70,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.797042',1,6),(109,'A51',5,6,2030.00,1740.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-16 12:43:48.804410',1,6),(110,'A52',5,6,1550.00,1750.00,1.00,2.70,3.00,120000.00,360000.00,0.00,'2026-07-16 12:43:48.811859',1,6),(111,'A01',5,7,770.00,2760.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-16 13:03:26.214722',19,7),(112,'A02',5,7,770.00,2800.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-16 13:03:26.222094',19,7),(113,'A03',5,7,710.00,2740.00,1.00,1.90,1.90,450000.00,450000.00,0.00,'2026-07-16 13:03:26.228554',19,7),(114,'A04',5,7,870.00,2920.00,1.00,2.50,2.50,450000.00,450000.00,0.00,'2026-07-16 13:03:26.237485',19,7),(115,'A05',5,7,800.00,2800.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-16 13:03:26.245411',19,7),(116,'A06',5,7,740.00,2680.00,1.00,2.00,2.00,450000.00,450000.00,0.00,'2026-07-16 13:03:26.253521',19,7),(117,'A07',5,7,760.00,2870.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-16 13:03:26.260918',19,7),(118,'A08',5,7,930.00,2940.00,1.00,2.70,2.70,450000.00,450000.00,0.00,'2026-07-16 13:03:26.267718',19,7),(119,'A09',5,7,780.00,2670.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-16 13:03:26.274493',19,7),(120,'A10',5,7,770.00,2700.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-16 13:03:26.280829',19,7),(121,'A11',5,7,830.00,2700.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-16 13:03:26.287936',19,7),(122,'A12',5,7,810.00,2700.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-16 13:03:26.294478',19,7),(123,'A13',5,7,940.00,3560.00,1.00,3.30,3.30,450000.00,450000.00,0.00,'2026-07-16 13:03:26.301766',19,7),(124,'A14',5,7,810.00,2660.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-16 13:03:26.308109',19,7),(125,'A15',5,7,760.00,2700.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-16 13:03:26.315449',19,7),(126,'A01',1,8,0.00,0.00,1.00,320.00,320.00,240000.00,76800000.00,0.00,'2026-07-16 13:28:22.310236',58,8),(127,'A02',7,8,0.00,0.00,1.00,1596.00,1596.00,240000.00,383040000.00,0.00,'2026-07-16 13:28:22.326504',59,8),(128,'A21',NULL,NULL,1800.00,2400.00,1.00,4.30,4.30,9000000.00,9000000.00,0.00,'2026-07-16 14:32:19.992339',60,5),(129,'A22',NULL,NULL,1800.00,2400.00,1.00,4.30,4.30,9000000.00,9000000.00,0.00,'2026-07-16 14:32:20.000738',60,5),(130,'A23',NULL,NULL,1500.00,2500.00,1.00,3.80,3.80,9000000.00,9000000.00,0.00,'2026-07-16 14:32:20.008109',60,5),(131,'A01',NULL,NULL,1490.00,1100.00,1.00,1.60,2.00,250000.00,500000.00,0.00,'2026-07-17 11:40:05.507954',25,9),(132,'A02',NULL,NULL,4065.00,1100.00,1.00,4.50,5.00,250000.00,1250000.00,0.00,'2026-07-17 11:40:05.514736',25,9),(133,'A03',NULL,NULL,3820.00,1100.00,1.00,4.20,4.20,250000.00,1050000.00,0.00,'2026-07-17 11:40:05.521662',25,9),(134,'A04',NULL,NULL,2415.00,1100.00,1.00,2.70,3.00,250000.00,750000.00,0.00,'2026-07-17 11:40:05.528184',25,9),(135,'A05',NULL,NULL,730.00,1100.00,1.00,0.80,1.00,250000.00,250000.00,0.00,'2026-07-17 11:40:05.534822',25,9),(136,'A06',NULL,NULL,2400.00,1100.00,1.00,2.60,3.00,250000.00,750000.00,0.00,'2026-07-17 11:40:05.541359',25,9),(137,'A07',NULL,NULL,2800.00,1100.00,1.00,3.10,3.10,250000.00,775000.00,0.00,'2026-07-17 11:40:05.551778',25,9),(138,'A08',NULL,NULL,3300.00,1100.00,1.00,3.60,4.00,250000.00,1000000.00,0.00,'2026-07-17 11:40:05.559537',25,9),(139,'A01',8,10,1490.00,1100.00,1.00,1.60,2.00,450000.00,900000.00,0.00,'2026-07-17 11:51:45.553379',62,10),(140,'A02',8,10,4065.00,1100.00,1.00,4.50,5.00,450000.00,2250000.00,0.00,'2026-07-17 11:51:45.559712',62,10),(141,'A03',8,10,3820.00,1100.00,1.00,4.20,4.20,450000.00,1890000.00,0.00,'2026-07-17 11:51:45.568055',62,10),(142,'A04',8,10,2415.00,1100.00,1.00,2.70,3.00,450000.00,1350000.00,0.00,'2026-07-17 11:51:45.574246',62,10),(143,'A05',8,10,730.00,1100.00,1.00,0.80,1.00,450000.00,450000.00,0.00,'2026-07-17 11:51:45.580780',62,10),(144,'A06',8,10,2400.00,1100.00,1.00,2.60,3.00,450000.00,1350000.00,0.00,'2026-07-17 11:51:45.587910',62,10),(145,'A07',8,10,2800.00,1100.00,1.00,3.10,3.10,450000.00,1395000.00,0.00,'2026-07-17 11:51:45.594361',62,10),(146,'A08',8,10,3300.00,1100.00,1.00,3.60,4.00,450000.00,1800000.00,0.00,'2026-07-17 11:51:45.601040',62,10),(147,'A01',8,10,4230.00,3070.00,1.00,13.00,13.00,450000.00,5850000.00,0.00,'2026-07-17 12:13:20.993677',63,11),(148,'A02',8,10,4020.00,3080.00,1.00,12.40,12.40,450000.00,5580000.00,0.00,'2026-07-17 12:13:21.000471',63,11),(149,'A03',8,10,2615.00,3370.00,1.00,8.80,9.00,450000.00,4050000.00,0.00,'2026-07-17 12:13:21.007468',63,11),(150,'A04',8,10,2714.00,2530.00,1.00,6.90,7.00,450000.00,3150000.00,0.00,'2026-07-17 12:13:21.014702',64,11),(151,'A05',8,10,3010.00,2530.00,1.00,7.60,8.00,450000.00,3600000.00,0.00,'2026-07-17 12:13:21.021409',64,11),(152,'A01',2,12,750.00,2520.00,1.00,1.90,1.90,450000.00,450000.00,0.00,'2026-07-17 12:51:06.075971',19,12),(153,'A02',2,12,855.00,2520.00,1.00,2.20,2.20,450000.00,450000.00,0.00,'2026-07-17 12:51:06.083148',19,12),(154,'A03',2,12,1675.00,3050.00,1.00,5.10,5.10,250000.00,1275000.00,0.00,'2026-07-17 12:51:06.089731',65,12),(155,'A04',2,12,630.00,3080.00,1.00,1.90,2.00,250000.00,500000.00,0.00,'2026-07-17 12:51:06.096516',65,12),(156,'A01',11,14,1005.00,1225.00,1.00,1.20,1.20,120000.00,144000.00,0.00,'2026-07-17 13:22:40.762485',68,13),(157,'A02',11,14,1005.00,1225.00,1.00,1.20,1.20,120000.00,144000.00,0.00,'2026-07-17 13:22:40.769156',68,13),(158,'A03',11,14,1125.00,1625.00,1.00,1.80,2.00,120000.00,240000.00,0.00,'2026-07-17 13:22:40.777007',68,13),(159,'A04',11,14,1350.00,1365.00,1.00,1.80,2.00,120000.00,240000.00,0.00,'2026-07-17 13:22:40.783663',68,13),(160,'A05',1,13,850.00,600.00,1.00,0.50,1.00,120000.00,120000.00,0.00,'2026-07-17 13:22:40.790597',68,13),(161,'A06',11,14,1010.00,1255.00,1.00,1.30,1.30,120000.00,156000.00,0.00,'2026-07-17 13:22:40.797078',68,13),(162,'A07',11,14,1740.00,1705.00,1.00,3.00,3.00,120000.00,360000.00,0.00,'2026-07-17 13:22:40.803574',68,13),(163,'A08',11,14,785.00,1715.00,1.00,1.30,1.30,120000.00,156000.00,0.00,'2026-07-17 13:22:40.810228',68,13),(164,'A09',11,14,1005.00,1270.00,1.00,1.30,1.30,120000.00,156000.00,0.00,'2026-07-17 13:22:40.816732',68,13),(165,'A10',11,14,940.00,690.00,1.00,0.60,1.00,120000.00,120000.00,0.00,'2026-07-17 13:22:40.823969',68,13),(166,'A11',11,14,950.00,1150.00,1.00,1.10,1.10,120000.00,132000.00,0.00,'2026-07-17 13:22:40.831322',68,13),(167,'A12',11,14,970.00,1170.00,1.00,1.10,1.10,120000.00,132000.00,0.00,'2026-07-17 13:22:40.837811',68,13),(168,'A13',11,14,1610.00,2045.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-17 13:22:40.845850',68,13),(169,'A14',11,14,800.00,2030.00,1.00,1.60,2.00,120000.00,240000.00,0.00,'2026-07-17 13:22:40.852971',68,13),(170,'A15',11,14,755.00,630.00,1.00,0.50,1.00,120000.00,120000.00,0.00,'2026-07-17 13:22:40.860845',68,13),(171,'A16',11,14,1620.00,630.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-17 13:22:40.868026',68,13),(173,'A01',10,13,685.00,3110.00,1.00,2.10,2.10,250000.00,525000.00,0.00,'2026-07-17 13:42:42.039980',69,14),(174,'A02',10,13,650.00,3125.00,1.00,2.00,2.00,250000.00,500000.00,0.00,'2026-07-17 13:42:42.047357',69,14),(175,'A03',10,13,675.00,2450.00,1.00,1.70,2.00,250000.00,500000.00,0.00,'2026-07-17 13:42:42.054794',69,14),(176,'A04',10,13,870.00,2560.00,1.00,2.20,2.20,250000.00,550000.00,0.00,'2026-07-17 13:42:42.062499',69,14),(177,'A05',10,13,850.00,2540.00,1.00,2.20,2.20,250000.00,550000.00,0.00,'2026-07-17 13:42:42.069786',69,14),(216,'A01',1,14,850.00,2690.00,1.00,2.30,2.30,450000.00,450000.00,0.00,'2026-07-18 14:19:15.753422',19,15),(217,'A02',1,14,910.00,2600.00,1.00,2.40,2.40,450000.00,450000.00,0.00,'2026-07-18 14:19:15.760783',19,15),(218,'A03',1,14,685.00,3110.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-18 14:19:15.768018',19,15),(219,'A04',1,14,650.00,3125.00,1.00,2.00,2.00,450000.00,450000.00,0.00,'2026-07-18 14:19:15.774776',19,15),(220,'A05',1,14,675.00,2450.00,1.00,1.70,1.70,450000.00,450000.00,0.00,'2026-07-18 14:19:15.781981',19,15),(221,'A06',1,14,725.00,2540.00,1.00,1.80,1.80,450000.00,450000.00,0.00,'2026-07-18 14:19:15.789183',19,15),(222,'A07',1,14,760.00,3135.00,1.00,2.40,2.40,450000.00,450000.00,0.00,'2026-07-18 14:19:15.795932',19,15),(223,'A08',1,14,775.00,3140.00,1.00,2.40,2.40,450000.00,450000.00,0.00,'2026-07-18 14:19:15.804054',19,15),(224,'A09',10,14,850.00,2690.00,1.00,2.30,2.30,250000.00,575000.00,0.00,'2026-07-18 14:19:15.813055',69,15),(225,'A10',10,14,910.00,2600.00,1.00,2.40,2.40,250000.00,600000.00,0.00,'2026-07-18 14:19:15.820842',69,15),(226,'A11',10,14,650.00,3125.00,1.00,2.00,2.00,250000.00,500000.00,0.00,'2026-07-18 14:19:15.828443',69,15),(227,'A12',10,14,675.00,2450.00,1.00,1.70,2.00,250000.00,500000.00,0.00,'2026-07-18 14:19:15.835506',69,15),(228,'A13',10,14,725.00,2540.00,1.00,1.80,2.00,250000.00,500000.00,0.00,'2026-07-18 14:19:15.844068',69,15),(229,'A14',10,14,760.00,3135.00,1.00,2.40,2.40,250000.00,600000.00,0.00,'2026-07-18 14:19:15.850629',69,15),(230,'A15',10,14,775.00,3140.00,1.00,2.40,2.40,250000.00,600000.00,0.00,'2026-07-18 14:19:15.858731',69,15),(231,'A16',10,14,685.00,3110.00,1.00,2.10,2.10,250000.00,525000.00,0.00,'2026-07-18 14:19:15.864157',69,15),(232,'A01',10,14,2620.00,3470.00,1.00,9.10,9.10,450000.00,4095000.00,0.00,'2026-07-18 14:29:48.172202',63,16),(233,'A02',8,14,2040.00,3100.00,1.00,6.30,6.30,450000.00,2835000.00,0.00,'2026-07-18 14:29:48.181342',63,16),(234,'A03',8,14,4320.00,3100.00,1.00,13.40,13.40,450000.00,6030000.00,0.00,'2026-07-18 14:29:48.188731',63,16),(235,'A04',8,14,3010.00,2550.00,1.00,7.70,8.00,450000.00,3600000.00,0.00,'2026-07-18 14:29:48.195775',63,16),(236,'A05',8,14,2710.00,2550.00,1.00,6.90,7.00,450000.00,3150000.00,0.00,'2026-07-18 14:29:48.202934',63,16),(237,'A06',8,14,2340.00,2770.00,1.00,6.50,7.00,450000.00,3150000.00,0.00,'2026-07-18 14:29:48.210830',63,16),(238,'A07',8,14,2340.00,2770.00,1.00,6.50,7.00,450000.00,3150000.00,0.00,'2026-07-18 14:29:48.218037',63,16),(239,'A01',4,12,2500.00,1100.00,1.00,2.80,3.00,350000.00,1050000.00,0.00,'2026-07-18 14:49:37.027893',70,17),(240,'A02',4,12,2600.00,1100.00,1.00,2.90,3.00,350000.00,1050000.00,0.00,'2026-07-18 14:49:37.034765',70,17),(241,'A03',4,12,2100.00,1100.00,1.00,2.30,2.30,350000.00,805000.00,0.00,'2026-07-18 14:49:37.041036',70,17),(242,'A04',4,12,1200.00,1100.00,1.00,1.30,1.30,350000.00,455000.00,0.00,'2026-07-18 14:49:37.048736',70,17),(243,'A05',4,12,4070.00,1100.00,1.00,4.50,5.00,350000.00,1750000.00,0.00,'2026-07-18 14:49:37.055979',70,17),(244,'A06',10,12,3810.00,1100.00,1.00,4.20,4.20,350000.00,1470000.00,0.00,'2026-07-18 14:49:37.063541',70,17),(245,'A07',1,12,2400.00,1100.00,1.00,2.60,3.00,350000.00,1050000.00,0.00,'2026-07-18 14:49:37.070423',70,17),(246,'A08',4,12,680.00,1100.00,1.00,0.70,1.00,350000.00,350000.00,0.00,'2026-07-18 14:49:37.078218',70,17),(247,'A09',NULL,NULL,2500.00,1100.00,1.00,2.80,3.00,200000.00,600000.00,0.00,'2026-07-18 14:49:37.085090',71,17),(248,'A10',NULL,NULL,2600.00,1100.00,1.00,2.90,3.00,200000.00,600000.00,0.00,'2026-07-18 14:49:37.092696',71,17),(249,'A11',NULL,NULL,2100.00,1100.00,1.00,2.30,2.30,200000.00,460000.00,0.00,'2026-07-18 14:49:37.102834',71,17),(250,'A12',NULL,NULL,1200.00,1100.00,1.00,1.30,1.30,200000.00,260000.00,0.00,'2026-07-18 14:49:37.111562',71,17),(251,'A13',NULL,NULL,4070.00,1100.00,1.00,4.50,5.00,200000.00,1000000.00,0.00,'2026-07-18 14:49:37.118712',71,17),(252,'A14',NULL,NULL,3810.00,1100.00,1.00,4.20,4.20,200000.00,840000.00,0.00,'2026-07-18 14:49:37.126115',71,17),(253,'A15',NULL,NULL,2400.00,1100.00,1.00,2.60,3.00,200000.00,600000.00,0.00,'2026-07-18 14:49:37.133426',71,17),(254,'A16',NULL,NULL,680.00,1100.00,1.00,0.70,1.00,200000.00,200000.00,0.00,'2026-07-18 14:49:37.140643',71,17),(255,'A01',1,2,0.00,0.00,1.00,135.00,135.00,250000.00,33750000.00,0.00,'2026-07-20 16:55:47.295576',72,18),(256,'A01',11,2,1490.00,2025.00,1.00,3.00,3.00,120000.00,360000.00,0.00,'2026-07-21 09:07:58.694381',1,19),(257,'A02',11,2,1785.00,2035.00,1.00,3.60,4.00,120000.00,480000.00,0.00,'2026-07-21 09:07:58.702203',1,19),(258,'A03',11,2,1745.00,2025.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-21 09:07:58.710691',1,19),(259,'A04',11,2,1785.00,2025.00,1.00,3.60,4.00,120000.00,480000.00,0.00,'2026-07-21 09:07:58.717910',1,19),(260,'A05',11,2,1600.00,2045.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-21 09:07:58.726036',1,19),(261,'A06',11,2,1475.00,1800.00,1.00,2.70,3.00,120000.00,360000.00,0.00,'2026-07-21 09:07:58.733849',1,19),(262,'A07',11,2,1955.00,1800.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-21 09:07:58.744099',1,19),(263,'A08',11,2,990.00,2050.00,1.00,2.00,2.00,120000.00,240000.00,0.00,'2026-07-21 09:07:58.752114',1,19),(264,'A09',11,2,973.00,1270.00,1.00,1.20,1.20,120000.00,144000.00,0.00,'2026-07-21 09:07:58.761203',1,19),(265,'A10',11,2,970.00,1000.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-21 09:07:58.769375',1,19),(266,'A11',11,2,1080.00,995.00,1.00,1.10,1.10,120000.00,132000.00,0.00,'2026-07-21 09:07:58.778745',1,19),(267,'A12',11,2,1005.00,980.00,1.00,1.00,1.00,120000.00,120000.00,0.00,'2026-07-21 09:07:58.789810',1,19),(268,'A01',11,14,1890.00,1805.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.603685',1,20),(269,'A02',11,14,1497.00,1755.00,1.00,2.60,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.610249',1,20),(270,'A03',11,14,955.00,1185.00,1.00,1.10,1.10,120000.00,132000.00,0.00,'2026-07-21 16:33:24.617286',1,20),(271,'A04',11,14,1940.00,1750.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.623601',1,20),(272,'A05',11,14,1940.00,1715.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-21 16:33:24.631000',1,20),(273,'A06',11,14,757.00,1014.00,1.00,0.80,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.637313',1,20),(274,'A07',11,14,957.00,2250.00,1.00,2.20,2.20,120000.00,264000.00,0.00,'2026-07-21 16:33:24.643428',1,20),(275,'A08',11,14,1953.00,2000.00,1.00,3.90,4.00,120000.00,480000.00,0.00,'2026-07-21 16:33:24.650352',1,20),(276,'A09',11,14,1930.00,1975.00,1.00,3.80,4.00,120000.00,480000.00,0.00,'2026-07-21 16:33:24.656971',1,20),(277,'A10',11,14,725.00,940.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.663953',1,20),(278,'A11',11,14,1935.00,1990.00,1.00,3.90,4.00,120000.00,480000.00,0.00,'2026-07-21 16:33:24.669842',1,20),(279,'A12',11,14,915.00,1765.00,1.00,1.60,2.00,120000.00,240000.00,0.00,'2026-07-21 16:33:24.676244',1,20),(280,'A13',11,14,1785.00,1755.00,1.00,3.10,3.10,120000.00,372000.00,0.00,'2026-07-21 16:33:24.682559',1,20),(281,'A14',11,14,1935.00,2235.00,1.00,4.30,4.30,120000.00,516000.00,0.00,'2026-07-21 16:33:24.691085',1,20),(282,'A15',11,14,1125.00,1515.00,1.00,1.70,2.00,120000.00,240000.00,0.00,'2026-07-21 16:33:24.697503',1,20),(283,'A16',11,14,1900.00,1745.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-21 16:33:24.704261',1,20),(284,'A17',11,14,1440.00,1745.00,1.00,2.50,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.710044',1,20),(285,'A18',11,14,720.00,955.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.716853',1,20),(286,'A19',11,14,1455.00,1775.00,1.00,2.60,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.724172',1,20),(287,'A20',11,14,1960.00,1750.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.730234',1,20),(288,'A21',11,14,760.00,970.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.737450',1,20),(289,'A22',11,14,1415.00,1760.00,1.00,2.50,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.752005',1,20),(290,'A23',11,14,1740.00,1740.00,1.00,3.00,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.758271',1,20),(291,'A24',11,14,925.00,2165.00,1.00,2.00,2.00,120000.00,240000.00,0.00,'2026-07-21 16:33:24.764467',1,20),(292,'A25',11,14,1450.00,1675.00,1.00,2.40,2.40,120000.00,288000.00,0.00,'2026-07-21 16:33:24.771097',1,20),(293,'A26',11,14,1725.00,1680.00,1.00,2.90,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.777781',1,20),(294,'A27',11,14,1985.00,1700.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.785037',1,20),(295,'A28',11,14,760.00,920.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.791101',1,20),(296,'A29',11,14,1945.00,1710.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-21 16:33:24.797499',1,20),(297,'A30',11,14,1940.00,1685.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-21 16:33:24.804666',1,20),(298,'A31',11,14,958.00,2240.00,1.00,2.10,2.10,120000.00,252000.00,0.00,'2026-07-21 16:33:24.811385',1,20),(299,'A32',11,14,1365.00,1825.00,1.00,2.50,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.817942',1,20),(300,'A33',1,14,1965.00,1770.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-21 16:33:24.823922',1,20),(301,'A34',1,14,1965.00,1755.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.830430',1,20),(302,'A35',1,14,725.00,1000.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.837621',1,20),(303,'A36',11,14,1940.00,2090.00,1.00,4.10,4.10,120000.00,492000.00,0.00,'2026-07-21 16:33:24.844441',1,20),(304,'A37',11,14,1975.00,1785.00,1.00,3.50,4.00,120000.00,480000.00,0.00,'2026-07-21 16:33:24.851692',1,20),(305,'A38',11,14,1928.00,2235.00,1.00,4.30,4.30,120000.00,516000.00,0.00,'2026-07-21 16:33:24.858164',1,20),(306,'A39',11,14,1955.00,1725.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.864644',1,20),(307,'A40',1,14,1755.00,1775.00,1.00,3.10,3.10,120000.00,372000.00,0.00,'2026-07-21 16:33:24.871825',1,20),(308,'A41',11,14,1895.00,1745.00,1.00,3.30,3.30,120000.00,396000.00,0.00,'2026-07-21 16:33:24.878503',1,20),(309,'A42',11,14,723.00,970.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.885204',1,20),(310,'A43',11,14,1940.00,1765.00,1.00,3.40,3.40,120000.00,408000.00,0.00,'2026-07-21 16:33:24.891687',1,20),(311,'A44',11,14,730.00,985.00,1.00,0.70,1.00,120000.00,120000.00,0.00,'2026-07-21 16:33:24.898026',1,20),(312,'A45',11,14,1455.00,1755.00,1.00,2.60,3.00,120000.00,360000.00,0.00,'2026-07-21 16:33:24.904743',1,20),(313,'A46',11,14,1744.00,1755.00,1.00,3.10,3.10,120000.00,372000.00,0.00,'2026-07-21 16:33:24.911499',1,20),(314,'A47',11,14,760.00,2750.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-21 16:33:24.918975',19,20),(315,'A48',11,14,760.00,2720.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-21 16:33:24.925802',19,20),(316,'A49',11,14,765.00,2690.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-21 16:33:24.932597',19,20),(317,'A50',11,14,760.00,2740.00,1.00,2.10,2.10,450000.00,450000.00,0.00,'2026-07-21 16:33:24.940109',19,20),(318,'A51',11,14,740.00,2700.00,1.00,2.00,2.00,450000.00,450000.00,0.00,'2026-07-21 16:33:24.947453',19,20),(319,'A52',11,14,740.00,2770.00,1.00,2.00,2.00,450000.00,450000.00,0.00,'2026-07-21 16:33:24.954455',19,20),(320,'A01',12,16,0.00,0.00,1.00,12.00,12.00,650000.00,7800000.00,0.00,'2026-07-22 06:20:45.382029',73,21),(321,'A02',13,15,0.00,0.00,1.00,54.00,54.00,550000.00,29700000.00,0.00,'2026-07-22 06:20:45.398299',74,21),(322,'A03',NULL,NULL,0.00,0.00,1.00,46.30,46.30,250000.00,11575000.00,0.00,'2026-07-22 06:20:45.408525',61,21),(323,'A01',2,2,0.00,0.00,1.00,312.00,312.00,350000.00,109200000.00,0.00,'2026-07-22 11:44:17.459672',75,22),(324,'A01',NULL,NULL,0.00,0.00,1.00,1.00,1.00,135652800.00,135652800.00,0.00,'2026-07-22 19:51:11.076996',76,23),(325,'A01',11,2,5210.00,2440.00,1.00,12.70,13.00,130000.00,1690000.00,0.00,'2026-07-23 12:50:29.882101',1,24),(326,'A02',11,2,1760.00,1910.00,1.00,3.40,3.40,130000.00,442000.00,0.00,'2026-07-23 12:50:29.895038',1,24),(327,'A03',11,2,1610.00,1910.00,1.00,3.10,3.10,130000.00,403000.00,0.00,'2026-07-23 12:50:29.901178',1,24),(328,'A04',11,2,1400.00,1660.00,1.00,2.30,2.30,130000.00,299000.00,0.00,'2026-07-23 12:50:29.908357',1,24),(329,'A05',11,2,1550.00,1950.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:29.915892',1,24),(330,'A06',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:29.922684',1,24),(331,'A07',11,2,950.00,730.00,1.00,0.70,1.00,130000.00,130000.00,0.00,'2026-07-23 12:50:29.929229',1,24),(332,'A08',11,2,1515.00,1955.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:29.936136',1,24),(333,'A09',11,2,1515.00,1955.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:29.950405',1,24),(334,'A10',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:29.957839',1,24),(335,'A11',11,2,950.00,730.00,1.00,0.70,1.00,130000.00,130000.00,0.00,'2026-07-23 12:50:29.965265',1,24),(336,'A12',11,2,1635.00,1950.00,1.00,3.20,3.20,130000.00,416000.00,0.00,'2026-07-23 12:50:29.972051',1,24),(337,'A13',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:29.979381',1,24),(338,'A14',11,2,1500.00,2000.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:29.986210',1,24),(339,'A15',11,2,1500.00,2000.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:29.992141',1,24),(340,'A16',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:29.998240',1,24),(341,'A17',11,2,1500.00,2000.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.005474',1,24),(342,'A18',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.011588',1,24),(343,'A19',11,2,150.00,2000.00,1.00,0.30,0.30,130000.00,39000.00,0.00,'2026-07-23 12:50:30.018500',1,24),(344,'A20',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.025071',1,24),(345,'A21',11,2,1610.00,1950.00,1.00,3.10,3.10,130000.00,403000.00,0.00,'2026-07-23 12:50:30.032014',1,24),(346,'A22',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.038615',1,24),(347,'A23',11,2,950.00,730.00,1.00,0.70,1.00,130000.00,130000.00,0.00,'2026-07-23 12:50:30.045038',1,24),(348,'A24',11,2,1500.00,1955.00,1.00,2.90,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.051898',1,24),(349,'A25',11,2,1530.00,1955.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.058861',1,24),(350,'A26',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.065085',1,24),(351,'A27',11,2,1500.00,1950.00,1.00,2.90,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.072424',1,24),(352,'A28',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.079418',1,24),(353,'A29',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.087373',1,24),(354,'A30',11,2,1550.00,1960.00,1.00,3.00,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.094561',1,24),(355,'A31',11,2,1460.00,1955.00,1.00,2.90,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.101913',1,24),(356,'A32',11,2,890.00,2445.00,1.00,2.20,2.20,130000.00,286000.00,0.00,'2026-07-23 12:50:30.108266',1,24),(357,'A33',11,2,3470.00,2425.00,1.00,8.40,8.40,130000.00,1092000.00,0.00,'2026-07-23 12:50:30.114533',1,24),(358,'A34',11,2,2360.00,1010.00,1.00,2.40,2.40,250000.00,600000.00,0.00,'2026-07-23 12:50:30.125523',52,24),(359,'A35',11,2,2360.00,1230.00,1.00,2.90,3.00,250000.00,750000.00,0.00,'2026-07-23 12:50:30.132079',52,24),(360,'A36',11,2,1600.00,2300.00,1.00,3.70,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.139045',1,24),(361,'A37',11,2,750.00,2180.00,1.00,1.60,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.145903',1,24),(362,'A38',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.153289',1,24),(363,'A39',11,2,1490.00,232.00,1.00,0.30,0.30,130000.00,39000.00,0.00,'2026-07-23 12:50:30.160003',1,24),(364,'A40',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.165993',1,24),(365,'A41',11,2,1580.00,2990.00,1.00,4.70,5.00,130000.00,650000.00,0.00,'2026-07-23 12:50:30.174974',1,24),(366,'A42',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.181459',1,24),(367,'A43',11,2,730.00,2140.00,1.00,1.60,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.189411',1,24),(368,'A44',11,2,750.00,2130.00,1.00,1.60,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.196510',1,24),(369,'A45',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.204313',1,24),(370,'A46',11,2,735.00,2135.00,1.00,1.60,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.210956',1,24),(371,'A47',11,2,2440.00,1775.00,1.00,4.30,4.30,130000.00,559000.00,0.00,'2026-07-23 12:50:30.218063',1,24),(372,'A48',11,2,2440.00,1775.00,1.00,4.30,4.30,130000.00,559000.00,0.00,'2026-07-23 12:50:30.225892',1,24),(373,'A49',11,2,1620.00,2300.00,1.00,3.70,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.232571',1,24),(374,'A50',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.243518',1,24),(375,'A51',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.250742',1,24),(376,'A52',11,2,755.00,2130.00,1.00,1.60,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.257765',1,24),(377,'A53',11,2,1470.00,2130.00,1.00,3.10,3.10,130000.00,403000.00,0.00,'2026-07-23 12:50:30.264555',1,24),(378,'A54',11,2,1490.00,2300.00,1.00,3.40,3.40,130000.00,442000.00,0.00,'2026-07-23 12:50:30.272538',1,24),(379,'A55',11,2,1760.00,1130.00,1.00,2.00,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.279434',1,24),(380,'A56',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.287362',1,24),(381,'A57',11,2,1500.00,2310.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.294482',1,24),(382,'A58',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.301581',1,24),(383,'A59',11,NULL,1500.00,2310.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.308759',1,24),(384,'A60',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.316081',1,24),(385,'A61',11,2,1500.00,2310.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.323765',1,24),(386,'A62',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.330635',1,24),(387,'A63',11,2,1520.00,2310.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.338802',1,24),(388,'A64',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.346532',1,24),(389,'A65',11,2,1550.00,2320.00,1.00,3.60,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.354228',1,24),(390,'A66',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.361187',1,24),(391,'A67',11,2,1330.00,2300.00,1.00,3.10,3.10,130000.00,403000.00,0.00,'2026-07-23 12:50:30.369294',1,24),(392,'A68',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.377207',1,24),(393,'A69',11,2,920.00,2300.00,1.00,2.10,2.10,130000.00,273000.00,0.00,'2026-07-23 12:50:30.389502',1,24),(394,'A70',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.396879',1,24),(395,'A71',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.405345',1,24),(396,'A72',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.413386',1,24),(397,'A73',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.422497',1,24),(398,'A74',11,2,1540.00,2500.00,1.00,3.90,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.429605',1,24),(399,'A75',11,2,2360.00,1040.00,1.00,2.50,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.437574',1,24),(400,'A76',11,2,2360.00,1235.00,1.00,2.90,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.445190',1,24),(401,'A77',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.452843',1,24),(402,'A78',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.468020',1,24),(403,'A79',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.494651',1,24),(404,'A80',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.507079',1,24),(405,'A81',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.518314',1,24),(406,'A82',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.527648',1,24),(407,'A83',11,2,1150.00,1775.00,1.00,2.00,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.540158',1,24),(408,'A84',11,2,1150.00,1775.00,1.00,2.00,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.552188',1,24),(409,'A85',11,2,1475.00,1775.00,1.00,2.60,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.565268',1,24),(410,'A86',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.576690',1,24),(411,'A87',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.588867',1,24),(412,'A88',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.597186',1,24),(413,'A89',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.605518',1,24),(414,'A90',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.613189',1,24),(415,'A91',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.621476',1,24),(416,'A92',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.629052',1,24),(417,'A93',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.636882',1,24),(418,'A94',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.644408',1,24),(419,'A95',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.652596',1,24),(420,'A96',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.660559',1,24),(421,'A97',11,2,940.00,9350.00,1.00,8.80,9.00,130000.00,1170000.00,0.00,'2026-07-23 12:50:30.669467',1,24),(422,'A98',11,2,1570.00,2300.00,1.00,3.60,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.677167',1,24),(423,'A99',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.685581',1,24),(424,'A100',11,2,940.00,3750.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.693388',1,24),(425,'A101',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.701311',1,24),(426,'A102',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.709550',1,24),(427,'A103',11,2,1560.00,2300.00,1.00,3.60,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.717488',1,24),(428,'A104',11,2,930.00,2300.00,1.00,2.10,2.10,130000.00,273000.00,0.00,'2026-07-23 12:50:30.725542',1,24),(429,'A105',11,12,940.00,2300.00,1.00,2.20,2.20,130000.00,286000.00,0.00,'2026-07-23 12:50:30.733873',1,24),(430,'A106',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.741859',1,24),(431,'A107',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.750412',1,24),(432,'A108',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.758780',1,24),(433,'A109',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.766504',1,24),(434,'A110',11,2,1540.00,2300.00,1.00,3.50,4.00,130000.00,520000.00,0.00,'2026-07-23 12:50:30.774475',1,24),(435,'A111',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.785917',1,24),(436,'A112',11,2,2310.00,1000.00,1.00,2.30,2.30,250000.00,575000.00,0.00,'2026-07-23 12:50:30.795037',52,24),(437,'A113',11,2,2310.00,2500.00,1.00,5.80,6.00,250000.00,1500000.00,0.00,'2026-07-23 12:50:30.803099',52,24),(438,'A114',11,2,425.00,545.00,1.00,0.20,0.20,130000.00,26000.00,0.00,'2026-07-23 12:50:30.811495',1,24),(439,'A115',11,2,1460.00,1500.00,1.00,2.20,2.20,130000.00,286000.00,0.00,'2026-07-23 12:50:30.820246',1,24),(440,'A116',11,2,1210.00,1500.00,1.00,1.80,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.827751',1,24),(441,'A117',11,2,600.00,440.00,1.00,0.30,0.30,130000.00,39000.00,0.00,'2026-07-23 12:50:30.836079',1,24),(442,'A118',11,2,1720.00,1710.00,1.00,2.90,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.843704',1,24),(443,'A119',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.852232',1,24),(444,'A120',11,2,1800.00,1700.00,1.00,3.10,3.10,130000.00,403000.00,0.00,'2026-07-23 12:50:30.861838',1,24),(445,'A121',11,2,940.00,7350.00,1.00,6.90,7.00,130000.00,910000.00,0.00,'2026-07-23 12:50:30.870065',1,24),(446,'A122',11,2,550.00,470.00,1.00,0.30,0.30,130000.00,39000.00,0.00,'2026-07-23 12:50:30.878553',1,24),(447,'A123',11,2,550.00,470.00,1.00,0.30,0.30,130000.00,39000.00,0.00,'2026-07-23 12:50:30.888062',1,24),(448,'A124',11,2,1740.00,1230.00,1.00,2.10,2.10,130000.00,273000.00,0.00,'2026-07-23 12:50:30.896004',1,24),(449,'A125',11,2,2300.00,1190.00,1.00,2.70,3.00,130000.00,390000.00,0.00,'2026-07-23 12:50:30.904291',1,24),(450,'A126',11,2,740.00,2010.00,1.00,1.50,2.00,130000.00,260000.00,0.00,'2026-07-23 12:50:30.912004',1,24),(451,'A127',11,2,1240.00,480.00,1.00,0.60,1.00,130000.00,130000.00,0.00,'2026-07-23 12:50:30.919727',1,24),(452,'A01',12,16,40340.00,1100.00,1.00,44.40,44.40,450000.00,19980000.00,0.00,'2026-07-24 12:26:51.074192',77,25),(453,'A02',12,16,8840.00,1100.00,1.00,9.70,10.00,450000.00,4500000.00,0.00,'2026-07-24 12:26:51.080619',78,25),(454,'A01',12,16,9150.00,1100.00,1.00,10.10,10.10,450000.00,4545000.00,0.00,'2026-07-24 12:49:34.805920',79,26),(455,'A02',12,16,5740.00,1100.00,1.00,6.30,6.30,450000.00,2835000.00,0.00,'2026-07-24 12:49:34.812262',80,26),(456,'A03',12,16,8640.00,1100.00,1.00,9.50,10.00,450000.00,4500000.00,0.00,'2026-07-24 12:49:34.819135',78,26);
/*!40000 ALTER TABLE `quotations_quotationitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_quotationitemnormal`
--

DROP TABLE IF EXISTS `reports_quotationitemnormal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_quotationitemnormal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` decimal(10,2) NOT NULL,
  `unit_price` decimal(12,2) NOT NULL,
  `total_price` decimal(12,2) NOT NULL,
  `product_id` bigint NOT NULL,
  `quotation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reports_quotationite_product_id_9b84b835_fk_inventory` (`product_id`),
  KEY `reports_quotationite_quotation_id_bf01a95a_fk_reports_q` (`quotation_id`),
  CONSTRAINT `reports_quotationite_product_id_9b84b835_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_product` (`id`),
  CONSTRAINT `reports_quotationite_quotation_id_bf01a95a_fk_reports_q` FOREIGN KEY (`quotation_id`) REFERENCES `reports_quotationnormal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_quotationitemnormal`
--

LOCK TABLES `reports_quotationitemnormal` WRITE;
/*!40000 ALTER TABLE `reports_quotationitemnormal` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports_quotationitemnormal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_quotationnormal`
--

DROP TABLE IF EXISTS `reports_quotationnormal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_quotationnormal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quotation_no` varchar(30) NOT NULL,
  `quotation_date` date NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quotation_no` (`quotation_no`),
  KEY `reports_quotationnor_customer_id_7dc25abd_fk_customers` (`customer_id`),
  CONSTRAINT `reports_quotationnor_customer_id_7dc25abd_fk_customers` FOREIGN KEY (`customer_id`) REFERENCES `customers_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_quotationnormal`
--

LOCK TABLES `reports_quotationnormal` WRITE;
/*!40000 ALTER TABLE `reports_quotationnormal` DISABLE KEYS */;
INSERT INTO `reports_quotationnormal` VALUES (1,'QT-2026-00056','2026-07-14',2),(2,'QT-2026-00058','2026-07-14',18);
/*!40000 ALTER TABLE `reports_quotationnormal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-24 17:53:42
