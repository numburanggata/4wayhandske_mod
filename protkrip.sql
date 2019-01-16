-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2016 at 06:53 PM
-- Server version: 5.6.26
-- PHP Version: 5.6.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `protkrip`
--

-- --------------------------------------------------------

--
-- Table structure for table `sequence_table`
--

CREATE TABLE IF NOT EXISTS `sequence_table` (
  `bssid` char(32) NOT NULL,
  `sequence` int(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sequence_table`
--

INSERT INTO `sequence_table` (`bssid`, `sequence`) VALUES
('11:11:11:11', 2147483647),
('11:29:EA:A2:11:34', 735386268),
('22:22:22:22:22:22', 201304643),
('99:99:99:99:99:99', 1289141311),
('AA:AA:AA:AA:AA:AA', 2147483647),
('BB:BB:BB:BB:BB:BB', 200415590),
('CC:CC:CC:CC:CC:CC', 1495148583),
('DD:DD:DD:DD:DD:DD', 1418788691);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sequence_table`
--
ALTER TABLE `sequence_table`
  ADD UNIQUE KEY `bssid` (`bssid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
