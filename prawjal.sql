-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 24, 2021 at 02:43 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prawjal`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sr` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `dt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sr`, `name`, `phone_num`, `msg`, `dt`) VALUES
(1, 'asta', '6688442255', 'hiii i have a perfect mental health', '2021-10-24 03:01:49'),
(3, 'hinata naruto', '1155997766', 'hiii testing thismsh', '2021-10-24 10:54:13'),
(4, 'Itachi Uchiha', '5511337799', 'love you sasuke', '2021-10-24 10:56:52'),
(5, 'None', 'None', 'None', '2021-10-24 11:52:32'),
(6, 'None', 'None', 'None', '2021-10-24 11:52:43'),
(7, 'None', 'None', 'None', '2021-10-24 11:52:53'),
(8, 'gg', '1122335544', 'wake up to reality', '2021-10-24 11:53:25'),
(9, 'None', 'None', 'None', '2021-10-24 12:40:13'),
(10, 'None', 'None', 'None', '2021-10-24 12:40:15'),
(11, 'None', 'None', 'None', '2021-10-24 13:16:56'),
(12, 'deepika padukon', '9955113377', 'i love ranveer amd im stress free person', '2021-10-24 13:17:49'),
(13, 'None', 'None', 'None', '2021-10-24 13:18:36'),
(14, 'None', 'None', 'None', '2021-10-24 13:20:33'),
(15, 'None', 'None', 'None', '2021-10-24 14:41:21'),
(16, 'None', 'None', 'None', '2021-10-24 14:41:22'),
(17, 'deepika padukon', '9955113377', 'fysdgf', '2021-10-24 14:41:34');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sr` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sr`, `name`, `email`, `password`, `dt`) VALUES
(1, 'pravin', 'jaanu@gmail.com', '12345', '2021-10-23 18:03:01'),
(2, 'kimchi', 'kimchi@gmail.com', '54321', '2021-10-23 18:03:43'),
(3, 'prajwal', 'cristiano@gmail.com', '100707', '2021-10-23 18:04:38'),
(4, 'SwaGGyBoy', 'swaggy@gmail.com', '12345', '2021-10-24 00:15:57'),
(5, 'Captain America', 'catain@gmail.com', 'america123', '2021-10-24 01:01:17'),
(7, 'earth', 'darti@gmail.com', 'universe', '2021-10-24 01:36:47'),
(8, 'asus', 'asus@gmail.com', 'asus123', '2021-10-24 01:40:12'),
(9, 'Fl4sh', 'fl4sh@gmail.com', 'fl4sh', '2021-10-24 01:43:26'),
(10, 'naruto', 'hinata@gmail.com', 'hinata143', '2021-10-24 02:17:42'),
(11, 'Jungkook', 'jungkook@gmail.com', 'jung123', '2021-10-24 02:21:11'),
(12, 'luffy', 'pirateking@gmail.com', '12345', '2021-10-24 11:34:44'),
(13, 'Eren Yeager', 'mikasa@gmail.com', 'attackontitan', '2021-10-24 11:45:38'),
(14, 'Elon Musk', 'marsplanetary@gmail.com', 'tesla&spacex', '2021-10-24 13:06:45'),
(15, 'Prabhat Jaiswar', 'prabhat@gmail.com', '12345prabhat', '2021-10-24 13:15:58'),
(16, 'SAMMY', 'sammy@gmail.com', '2312312312', '2021-10-24 14:40:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sr`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sr`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sr` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sr` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
