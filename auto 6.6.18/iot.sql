-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 21, 2017 at 09:52 AM
-- Server version: 5.5.57-0+deb8u1
-- PHP Version: 5.6.30-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `iot`
--

-- --------------------------------------------------------

--
-- Table structure for table `main`
--

CREATE TABLE IF NOT EXISTS `main` (
  `id` int(5) NOT NULL,
  `fan` int(5) NOT NULL,
  `light` int(5) NOT NULL,
  `ac` int(5) NOT NULL,
  `projector` int(5) NOT NULL,
  `auto` int(5) NOT NULL,
  `net` int(5) NOT NULL,
  `door` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `main`
--

INSERT INTO `main` (`id`, `fan`, `light`, `ac`, `projector`, `auto`, `net`, `door`) VALUES
(1, 1, 0, 1, 1, 1, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `notify`
--

CREATE TABLE IF NOT EXISTS `notify` (
`id` int(5) NOT NULL,
  `msg` varchar(200) NOT NULL,
  `flag` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE IF NOT EXISTS `timetable` (
  `start` varchar(32) NOT NULL,
  `end` varchar(32) NOT NULL,
  `Monday` int(5) NOT NULL,
  `Tuesday` int(5) NOT NULL,
  `Wednesday` int(5) NOT NULL,
  `Thursday` int(5) NOT NULL,
  `Friday` int(5) NOT NULL,
  `Saturday` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`start`, `end`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`) VALUES
('08:45', '09:50', 1, 0, 1, 0, 0, 1),
('09:50', '10:45', 1, 1, 0, 1, 0, 0),
('11:30', '12:25', 0, 1, 1, 0, 1, 1),
('12:25', '13:20', 0, 1, 0, 1, 1, 0),
('13:30', '14:25', 0, 0, 1, 0, 1, 1),
('14:25', '15:30', 0, 1, 0, 1, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `notify`
--
ALTER TABLE `notify`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `notify`
--
ALTER TABLE `notify`
MODIFY `id` int(5) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
