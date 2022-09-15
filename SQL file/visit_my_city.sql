-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2022 at 06:36 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visit_my_city`
--

-- --------------------------------------------------------

--
-- Table structure for table `advert_offer`
--

CREATE TABLE `advert_offer` (
  `oano` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `title` varchar(50) COLLATE utf8_bin NOT NULL,
  `content` varchar(175) COLLATE utf8_bin NOT NULL,
  `image` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `olocation` varchar(50) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `advert_offer`
--

INSERT INTO `advert_offer` (`oano`, `username`, `title`, `content`, `image`, `olocation`) VALUES
(3, 'shubham@gmail.com', '', '', 'advt3.jpg', '18.465171,73.833144'),
(4, 'onkar@gmail.com', '', '', 'avert1.jpg', '18.465171,73.833144'),
(5, 'onkar@gmail.com', '', '', 'advt4.jpg', '18.465171,73.833144'),
(6, 'ritesh@gmail.com', 'Ritesh Super Market & Vegetable / Fruit', '20% off on fresh fruits,10 % off on vegetables,20% off on onion,5% off on mutter ,', 'defaultplace.jpg', '18.464118767934416,73.82816342184178'),
(7, 'abhiruchi@gmail.com', 'Abhiruchi Mall & Multiplex', '50% off on clothes ,10% off on kitchen material ,25% off on groceries ,5% off on any food ,', 'abhiruchi mall.jpg', '18.463318635692694,73.81678951451413'),
(8, 'ganesh@gmail.com', '', '', 'advt kothrude.jpg', '18.5196,73.8554'),
(9, 'adesh@gmail.com', '', '', 'onkar event decorators.jpg', '18.5196,73.8554'),
(10, 'adesh@gmail.com', 'Shri Ganesha Events, Katraj Pune', 'All types Events Decoration ,Birthday party,Baby shower,Naming ceremony, Engagement,', 'shri ganesha event.jpg', '18.452928026454465,73.86547697255246');

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

CREATE TABLE `article` (
  `ano` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `wname` varchar(30) COLLATE utf8_bin NOT NULL,
  `title` varchar(200) COLLATE utf8_bin NOT NULL,
  `article_content` varchar(1000) COLLATE utf8_bin NOT NULL,
  `photo` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `pdate` varchar(30) COLLATE utf8_bin NOT NULL,
  `alocation` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `article`
--

INSERT INTO `article` (`ano`, `username`, `wname`, `title`, `article_content`, `photo`, `pdate`, `alocation`) VALUES
(5, 'shubham@gmail.com', 'Onkar kulkarni', 'Sinhgad Institutes’ Stallion Motorsport team shines in Formula Student racing in Germany and Austria', 'Team Stallion Motorsport of Sinhgad Institutes, Pune, is one of the first teams from India to clear the endurance at Hockenheim, Germany as they competed with the best teams in the world, in the Formula Student Germany - FSG 2019. They received a standing ovation on successful completion of the endurance. Focusing on good design, reliability and performance, the group of enthusiastic students from Smt. Kashibai Navale College of Engineering, Vadgaon, Pune, designed and fabricated their open wheel Formula Student style racing car. Sunday 11 August 2019 was reserved entirely for Formula student Endurance of both classes — a grueling 22 KMs test of stamina for both driver and vehicle -with 6 cars racing on the track simultaneously.', 'article skc.jpg', '28 July, 2022', '18.465171,73.833144'),
(6, 'ganesh@gmail.com', 'ganesh', 'Chhatrapati Shivaji Maharaj Katha : शिवरायाचें आठवावें रूप, शिवरायाचा आठवावा प्रताप;', 'केवळ महाराष्ट्र किंवा भारतातच नव्हे, तर संपूर्ण जगभरात शिवाजी महाराजांचे नाव आदराने घेतले जाते. ज्यांच्या साहस कथा, विचार, तत्त्वज्ञान आजही सर्वांना प्रेरणा देतात, अशा छत्रपती शिवाजी महाराजांची १९ फेब्रुवारी रोजी जयंती झाली, आता येणाऱ्या सोमवारी २१ मार्च रोजी महाराजांची तिथीप्रमाणे जयंती आहे. हिंदू पंचांगात तिथीला देखील महत्व असते. शिवाजी महाराजांचे अनेक किस्से नेहमी शिकवण देत असतात आणि त्यांना रोजच आठवणीत ठेवले तर अनेक अडचणींवर मात करण्यासाठी एक मंत्र नक्की मिळेल.', 'article chhatrapati.jpg', '30 July, 2022', '18.5196,73.8554');

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `eno` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `ename` varchar(40) COLLATE utf8_bin NOT NULL,
  `venue` varchar(50) COLLATE utf8_bin NOT NULL,
  `edate` varchar(25) COLLATE utf8_bin NOT NULL,
  `etime` varchar(6) COLLATE utf8_bin NOT NULL,
  `poster` varchar(25) COLLATE utf8_bin DEFAULT NULL,
  `organizer` varchar(40) COLLATE utf8_bin NOT NULL,
  `elocation` varchar(50) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`eno`, `username`, `ename`, `venue`, `edate`, `etime`, `poster`, `organizer`, `elocation`) VALUES
(20, 'shubham@gmail.com', 'maharashtra din', 'SIOM,pune', '1 May, 2022', '09:10', 'maharshtra din.jpg', 'SIOM', '18.4647439,73.8326721'),
(22, 'onkar@gmail.com', 'shivjayanti', 'vadgaon', '6 July, 2022', '09:10', 'shivjayanti.jpg', 'ganesh tarun mandal', '18.465964527762253,73.824'),
(23, 'ganesh@gmail.com', 'ganesh Utsav ', 'kothrud, pune', '6 August, 2022', '09:00', 'ganesh chaturthi.jpg', 'kothrude group', '18.506227931013235,73.80768073269955'),
(24, 'adesh@gmail.com', 'ganesh chaturthi', 'Zeal college, Narhe', '31 August, 2022', '10:00', 'default event.jpg', 'zeal college students', '18.446699465606994,73.82666004368893');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `fno` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(30) COLLATE utf8_bin NOT NULL,
  `comment` text COLLATE utf8_bin NOT NULL,
  `flocation` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `guide`
--

CREATE TABLE `guide` (
  `gno` int(11) NOT NULL,
  `email` varchar(30) COLLATE utf8_bin NOT NULL,
  `password` varchar(16) COLLATE utf8_bin NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `gname` varchar(30) COLLATE utf8_bin NOT NULL,
  `glocation` varchar(50) COLLATE utf8_bin NOT NULL,
  `photo` varchar(30) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `guide`
--

INSERT INTO `guide` (`gno`, `email`, `password`, `mobile`, `gname`, `glocation`, `photo`) VALUES
(12, 'vadgaon@gmail.com', 'vadgaon@2000', 9874562555, 'Vadgaon Guide', '18.466056115603262,73.82498634526364', 'guide1.jpg'),
(13, 'ganesh@gmail.com', 'ganesh@2000', 9874524456, 'ganesh darekar', '18.51709345966072,73.85519874760739', 'guide2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `place`
--

CREATE TABLE `place` (
  `pno` int(11) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `pname` varchar(40) COLLATE utf8_bin NOT NULL,
  `type` varchar(100) COLLATE utf8_bin NOT NULL,
  `description` varchar(200) COLLATE utf8_bin NOT NULL,
  `mobileno` varchar(10) COLLATE utf8_bin NOT NULL,
  `photos` varchar(50) COLLATE utf8_bin NOT NULL,
  `plocation` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `place`
--

INSERT INTO `place` (`pno`, `username`, `pname`, `type`, `description`, `mobileno`, `photos`, `plocation`) VALUES
(17, 'shubham@gmail.com', 'Cricket Ground', 'sports', 'There are many games played here', '8956235478', 'cricket ground.jpeg', '18.468478,73.834377'),
(19, 'onkar@gmail.com', 'Ruhi Chicken And Egg', 'food', 'chicken and mutton available here', '8596562335', 'chicken and eggs.png', '18.464973,73.833068'),
(23, 'nanded@gmail.com', 'lalit garden', 'gardens', 'The best garden in Nanded city area', '9896546154', 'lalit garden.jpg', '18.459543080600923,73.7910483545982'),
(24, 'nanded@gmail.com', 'eco park', 'gardens', 'best garden for kids', '', 'eco park.jpg', '18.454551282570836,73.7849060959541'),
(25, 'ganesh@gmail.com', 'Sahyadri Hospital Kothrud', 'health', 'medical emergency ', '9566553232', 'hospital.jpg', '18.507862764086255,73.80449058035246'),
(26, 'ganesh@gmail.com', 'Pune-Okayama Friendship Garden', 'gardens', 'Japanese garden set on 10 acres with paths & wooden pergolas, plus fish ponds & a kids play area.', '6865464651', 'pu la garden.jpg', '18.4914749390221,73.83678806492917'),
(27, 'shubham@gmail.com', 'goodluck cafe', 'Cafe', 'best cafe near sinhgad college', '9874563214', 'goodluck cafe.JPG', '18.464417703506186,73.83690071770779'),
(28, 'shubham@gmail.com', 'datta mandir', 'temples', 'near stanza living and overhead water tank', '9846543513', 'datta mandir.jpg', '18.464666392063716,73.83242276975743'),
(29, 'abhiruchi@gmail.com', 'Abhiruchi Mall & Multiplex', 'mall', 'super market', '9874562215', 'abhiruchi mall.jpg', '18.463328812278796,73.8168217010223'),
(30, 'ritesh@gmail.com', 'Ritesh Super Market & Vegetable or Fruit', 'food', 'fresh vegetables and fruits are available here', '9874452565', 'defaultplace.jpg', '18.464120040001763,73.82815939852826'),
(31, 'onkar@gmail.com', 'stanza living', 'hostel', 'best hostel for students', '9874632545', 'stanza living.jpg', '18.46445840958629,73.83187425801388'),
(32, 'onkar@gmail.com', 'Berojgar Engineers', 'food', 'A good quality Pizza available here', '9845625478', 'berojgar.jpg', '18.464811725235474,73.82964735397927'),
(33, 'shri@gmail.com', 'lipton cafe', 'Cafe', '', '9885546256', 'lipton cafe.jpg', '18.46470264586425,73.3700264165036'),
(34, 'shri@gmail.com', 'swaminaray mandir', 'temples', 'BAPS swaminarayan mandir near narhe, pune', '6584156845', 'swaminaray temple.jpeg', '18.442073697056777,73.8364876575195'),
(35, 'shubham@gmail.com', 'oxygen zone', 'road', 'best oxygen zone near naded city', '6565615112', 'oxygen zone.jpg', '18.46136980832818,73.79931089946858'),
(36, 'adesh@gmail.com', 'jogeshwari misal', 'food', 'near narhe pune', '9874563255', 'jogeshwari misal.jpg', '18.447246509206803,73.80593327352635'),
(37, 'ss@gmail.com', 'Smt. Kashibai Navale Medical College and', 'college', 'medical college in narhe', '9889585489', 'skncm.jpg', '18.45630936866997,73.8208369679176'),
(38, 'abhishek@gmail.com', 'gfbfd', 'sports,gardens,grocery,', 'dfgdfh', '5325435532', 'Lagad Shubham sambhaji.jpg', '18.5204303,73.8567437');

-- --------------------------------------------------------

--
-- Table structure for table `resident`
--

CREATE TABLE `resident` (
  `rno` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(30) COLLATE utf8_bin NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `password` varchar(16) COLLATE utf8_bin NOT NULL,
  `rlocation` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `resident`
--

INSERT INTO `resident` (`rno`, `name`, `email`, `mobile`, `password`, `rlocation`) VALUES
(46, 'user nanded', 'nanded@gmail.com', 8959956256, 'nanded', '18.45917671503927,73.78640545079342'),
(47, 'abhishek', 'abhishek@gmail.com', 8596524526, 'abhishek@2000', '18.578072068179743,73.97877884575955'),
(48, 'ganesh ', 'ganesh@gmail.com', 8266265656, 'ganesh@2000', '18.506720353416455,73.80765712978409'),
(51, 'shri sharma', 'shri@gmail.com', 6585464864, 'shri@2000', '18.442038074593462,73.83511436650387'),
(52, 'onkar kulkarni', 'onkar@gmail.com', 9874563256, 'onkar@2000', '18.46477388137986,73.82968557545773'),
(53, 'ritesh', 'ritesh@gmail.com', 9878564665, 'ritesh@2000', '18.464163290286585,73.82816208073727'),
(54, 'abhi ruchi', 'abhiruchi@gmail.com', 9874563214, 'abhiruchi@2000', '18.463298282518632,73.81681097218625'),
(55, 'adesh lagad', 'adesh@gmail.com', 9874562456, 'adesh@2000', '18.580665337462893,73.97881639668576'),
(56, 'ss', 'ss@gmail.com', 5484845641, 'ssssssss', '18.515343627125503,73.85455501744381');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advert_offer`
--
ALTER TABLE `advert_offer`
  ADD PRIMARY KEY (`oano`);

--
-- Indexes for table `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`ano`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`eno`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`fno`);

--
-- Indexes for table `guide`
--
ALTER TABLE `guide`
  ADD PRIMARY KEY (`gno`);

--
-- Indexes for table `place`
--
ALTER TABLE `place`
  ADD PRIMARY KEY (`pno`);

--
-- Indexes for table `resident`
--
ALTER TABLE `resident`
  ADD PRIMARY KEY (`rno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `advert_offer`
--
ALTER TABLE `advert_offer`
  MODIFY `oano` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `article`
--
ALTER TABLE `article`
  MODIFY `ano` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `eno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `fno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `guide`
--
ALTER TABLE `guide`
  MODIFY `gno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `place`
--
ALTER TABLE `place`
  MODIFY `pno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `resident`
--
ALTER TABLE `resident`
  MODIFY `rno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
