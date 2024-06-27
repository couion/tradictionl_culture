-- MySQL dump 10.13  Distrib 8.0.35, for macos13 (arm64)
--
-- Host: 127.0.0.1    Database: traditional
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `personal_info` text,
  `photo_url` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `register_username` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'admin','admin','','','http://localhost:8000/media/uploads/admin%E5%A4%B4%E5%83%8F1_sfA4WxV.png','2024-04-09 16:07:22','2024-04-15 14:40:38','系统初始化创建');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `work_id` int NOT NULL,
  `user_id` int NOT NULL,
  `content` text NOT NULL COMMENT '评论内容',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `work_id` (`work_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comments_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comments_work_id_fk` FOREIGN KEY (`work_id`) REFERENCES `works` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='评论表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,1,1,'测试评论一下','2024-04-08 17:45:11','2024-04-08 17:45:11'),(2,1,1,'测试评论一下','2024-04-08 17:46:14','2024-04-08 17:46:14'),(3,1,1,'测试评论一下','2024-04-08 17:46:50','2024-04-08 17:46:50');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments_likes`
--

DROP TABLE IF EXISTS `comments_likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments_likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comment_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `comment_id` (`comment_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comments_likes_comment_id_fk` FOREIGN KEY (`comment_id`) REFERENCES `comments` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comments_likes_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='评论点赞表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments_likes`
--

LOCK TABLES `comments_likes` WRITE;
/*!40000 ALTER TABLE `comments_likes` DISABLE KEYS */;
INSERT INTO `comments_likes` VALUES (1,1,1,'2024-04-08 17:58:05','2024-04-08 17:58:05'),(5,3,1,'2024-04-15 14:02:07','2024-04-15 14:02:07');
/*!40000 ALTER TABLE `comments_likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments_marks`
--

DROP TABLE IF EXISTS `comments_marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments_marks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comment_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `comment_id_idx` (`comment_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `comments_marks_comment_id_fk` FOREIGN KEY (`comment_id`) REFERENCES `comments` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comments_marks_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='评论收藏表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments_marks`
--

LOCK TABLES `comments_marks` WRITE;
/*!40000 ALTER TABLE `comments_marks` DISABLE KEYS */;
INSERT INTO `comments_marks` VALUES (1,2,1,'2024-04-09 09:33:23','2024-04-09 09:33:23');
/*!40000 ALTER TABLE `comments_marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `work_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `work_id` (`work_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `likes_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `likes_work_id_fk` FOREIGN KEY (`work_id`) REFERENCES `works` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='点赞表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (6,1,1,'2024-04-15 13:43:16','2024-04-15 13:43:16');
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marks`
--

DROP TABLE IF EXISTS `marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `work_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `work_id` (`work_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `marks_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `marks_work_id_fk` FOREIGN KEY (`work_id`) REFERENCES `works` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='收藏表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks`
--

LOCK TABLES `marks` WRITE;
/*!40000 ALTER TABLE `marks` DISABLE KEYS */;
/*!40000 ALTER TABLE `marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `personal_info` text,
  `photo_url` text,
  `is_banned` char(1) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin0','admin1','13888888889','xxxxx我是后端，你是前端','http://localhost:8000/media/uploads/%E7%94%A8%E6%88%B7%E5%A4%B4%E5%83%8F1_WHVUSMo.png','0','2024-04-08 16:43:24','2024-04-15 14:06:47'),(2,'admin1','admin1','','','','0','2024-04-09 15:50:34','2024-04-15 09:14:15');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works`
--

DROP TABLE IF EXISTS `works`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works` (
  `id` int NOT NULL AUTO_INCREMENT,
  `work_type` varchar(20) DEFAULT '' COMMENT '作品类型',
  `title` varchar(255) DEFAULT '' COMMENT '作品标题',
  `worker` varchar(255) DEFAULT '' COMMENT '作者',
  `description` text COMMENT '作品简介',
  `image_url` text COMMENT '作品图片',
  `content` text COMMENT '正文文本',
  `video_url` text COMMENT '视频地址',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '数据创建时间',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间',
  `view_count` int DEFAULT NULL COMMENT '观看次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='作品总表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works`
--

LOCK TABLES `works` WRITE;
/*!40000 ALTER TABLE `works` DISABLE KEYS */;
INSERT INTO `works` VALUES (1,'文章','测试','测试','测试描述','测试地址','测试内容','测试地址','2024-04-08 16:10:13','2024-04-15 11:47:32',3),(2,'文章','中华传统文化是最优秀的!!!','中华人民!!','中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的','','中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的中华传统文化是最优秀的!!!','','2024-04-15 14:16:33','2024-04-15 14:18:39',0),(4,'文章','什么是传统文化？','百度百科','传统文化（Traditional culture）是文明演化而汇集成的一种反映民族特质和风貌的文化，是各民族历史上各种思想文化、观念形态的总体表现。','','传统文化（Traditional culture）是文明演化而汇集成的一种反映民族特质和风貌的文化，是各民族历史上各种思想文化、观念形态的总体表现。其内容当为历代存在过的种种物质的、制度的和精神的文化实体和文化意识。它是对应于当代文化和外来文化的一种统称。世界各国、各民族都有自己的传统文化。/n/n中国的传统文化，依据中国历史大系表顺序，经历了史前时期的有巢氏 、燧人氏、伏羲氏、神农氏（炎帝）、黄帝（轩辕氏）、尧、舜、禹等时代，到夏朝建立。之后绵延发展。中国的传统文化有儒家、佛家、杂家、纵横家、道家、墨家、法家、兵家、名家和阴阳家等文化意识形态，具体包括：古文、诗、词、曲、赋、民族音乐、民族戏剧、曲艺、国画、书法、对联、灯谜、射覆、酒令、歇后语，以及民族服饰、生活习俗、古典诗文。其中，儒家、佛家、道家思想，以及“三位一体”的合流思想对中国传统影响最为直接而深刻。1921年，在厉麟似的努力下，首个以中国传统文化为主要研究对象的国际学术组织——景星学社在德国诞生，标志着中国传统文化开始逐渐为西方主流知识界所接受。/n/n文化（culture）本身是一个比较大的概念。笼统地说，文化是一种社会现象，是人们长期创造形成的产物。同时又是一种历史现象，是社会历史的积淀物。广义的文化是人类创造出来的所有物质和精神财富的总和。其中既包括世界观，人生观，价值观等具有意识形态性质的部分，又包括自然科学和技术，语言和文字等非意识形态的部分。确切地说，文化是指一个国家或民族的历史、地理、风土人情、传统习俗、生活方式、文学艺术、行为规范、思维方式、价值观念等。根据英国人类学家爱德华·泰勒的定义，文化是“包括知识、信仰、艺术、法律、道德、风俗以及作为一个社会成员所获得的能力与习惯的复杂整体”。其核心是作为精神产品的各种知识，其本质是传播。文化是人类社会特有的现象。文化是由人所创造，为人所特有的。有了人类社会才有文化，文化是人类社会实践的产物。在中国人民长期的社会实践中， 形成以儒家、佛家、道家三家之学为支柱的中华传统文化。/n/n中华传统文化以儒家、佛家、道家三家之学为支柱, 包括思想、文字、语言，之后是六艺，也就是：礼、乐、射、御、书、数，再后是生活富足之后衍生出来的书法、音乐、武术、曲艺、棋类、节日、民俗等。传统文化是我们生活中息息相关的，融入我们生活的，我们享受它而不自知的东西。如，佛家的“烦恼”、“差别”、“平等”、“世界”等。/n/n中华传统文化的双重属性反映了传统文化之间（如：儒家/道家之间；儒家/法家之间、儒家/佛家之间）存在对立与统一的辩证关系。他们之间相渗透，形成古文、古诗、词语、乐曲、赋、民族音乐、民族戏剧、曲艺、国画、书法、对联、灯谜、射覆、酒令、歇后语文化形式等。','','2024-04-15 15:05:06','2024-04-15 15:05:06',0),(5,'文章','中国的传统文化有哪些？','AI文星模型','中国的传统文化极为丰富多样，涵盖了许多方面。','','中国的传统文化极为丰富多样，涵盖了许多方面。以下是一些主要的文化元素：/n/n思想与文化：中国传统文化深受儒家、道家、墨家等思想流派的影响。儒家思想强调仁爱、和谐与家庭伦理，道家主张返璞归真、天人合一，墨家则提倡兼爱和公平。这些思想塑造了中国人民的价值观和行为准则。/n/n艺术与文学：包括书法、绘画、音乐、戏曲、诗词、散文等多种艺术形式。例如，中国书法以其独特的字体风格和线条美感著称；中国画则通过墨色的浓淡和线条的灵动来表达意境；传统戏剧如京剧、昆曲等，则通过富有戏剧性的表演形式，表达人们对生活和社会的思考。/n/n节日与民俗：中国有许多传统节日，如春节、元宵节、清明节、端午节、中秋节等，每个节日都有独特的庆祝方式和文化内涵。此外，还有丰富的民俗活动，如舞龙舞狮、放鞭炮、挂灯笼等，这些都反映了中国人民的生活习俗和文化传统。/n/n物质文化：包括园林建筑、工艺美术、服饰文化、美食文化等。中国的园林建筑如苏州园林、颐和园等，富有东方哲学的韵味；传统工艺品如瓷器、丝绸等，展现了精湛的工艺技巧和审美趣味；传统服饰如汉服、唐装等，体现了中国文化的独特魅力；而美食文化则以其丰富的食材、独特的烹调方法和用餐礼仪，吸引了世界各地的食客。/n/n除此之外，还有封建社会的等级制度、科举制度、农耕制度、礼仪制度等社会制度文化，以及道教、佛教、儒教等宗教文化，这些都是中国传统文化的重要组成部分。/n/n总的来说，中国传统文化是一个博大精深、包容并蓄的体系，它包含了中国人民的智慧和创造力，也体现了中国人民的精神追求和审美情趣。','','2024-04-15 15:07:25','2024-04-15 15:07:25',0),(6,'文章','儒家传统文化介绍','AI文星模型','儒家传统文化是以儒家学说为指导思想的文化流派，为历代儒客信众所推崇。','','儒家传统文化是以儒家学说为指导思想的文化流派，为历代儒客信众所推崇。这一文化流派起源于春秋时期，由孔子所创立，历经数千年的传承与发展，对中国及东亚地区的文化、教育、政治、伦理等方面产生了深远的影响。儒家学说倡导血亲人伦、现世事功、修身存养、道德理性，其中心思想是恕、忠、孝、悌、勇、仁、义、礼、智、信。这些理念构成了儒家文化的核心价值体系，体现了儒家对于人性、社会、政治等方面的深刻洞察与独特见解。在教育方面，儒家强调教育的重要性，认为通过教育可以培养人的道德品质，提高人的素养。儒家教育注重德育，强调人与人之间的亲情、友情、爱情等情感纽带，以及个人对家庭、社会、国家的责任与义务。同时，儒家也提倡“圣”的理念，认为每个人都能通过努力成为道德高尚的人，为社会和谐作出贡献。在社会政治方面，儒家主张仁政，认为统治者应该实行仁爱的政策，关心民众疾苦，维护社会稳定。儒家提倡礼治，认为礼是维护社会秩序的重要手段，通过礼仪规范人们的行为，实现社会的和谐与稳定。在伦理道德方面，儒家强调个人的道德修养与自律，认为每个人都应该注重自我完善，追求道德境界的提升。儒家提倡“仁爱”之心，认为人应该具备同情心和关爱之心，尊重他人、关爱他人、帮助他人。总的来说，儒家传统文化是一个博大精深、内涵丰富的文化体系，它在中国历史长河中扮演着举足轻重的角色，对中华民族的精神文化产生了深远的影响。在当今社会，儒家传统文化的价值和意义依然不可忽视，它为我们提供了一种思考人生、社会、政治等问题的独特视角和方法。','','2024-04-15 15:08:46','2024-04-15 15:08:46',0),(7,'视频','热门视频1','抖音','热门视频，传统文化内容','','','http://localhost:8000/media/uploads/%E4%BC%A0%E7%BB%9F%E6%96%87%E5%8C%961.MP4','2024-04-15 15:15:01','2024-04-15 15:15:01',0),(8,'视频','热门视频2','抖音','热门视频2，传统文化内容','','','http://localhost:8000/media/uploads/%E4%BC%A0%E7%BB%9F%E6%96%87%E5%8C%962.MP4','2024-04-15 15:15:38','2024-04-15 15:15:38',0),(9,'视频','热门视频3','抖音','热门视频3，传统文化内容','','','http://localhost:8000/media/uploads/%E4%BC%A0%E7%BB%9F%E6%96%87%E5%8C%963.MP4','2024-04-15 15:16:03','2024-04-15 15:16:03',0),(10,'视频','热门视频4','抖音','热门视频4，传统文化内容','','','http://localhost:8000/media/uploads/%E4%BC%A0%E7%BB%9F%E6%96%87%E5%8C%964.MP4','2024-04-15 15:16:25','2024-04-15 15:16:25',0);
/*!40000 ALTER TABLE `works` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-15 15:20:04
