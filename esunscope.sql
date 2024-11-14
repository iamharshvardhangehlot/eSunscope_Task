-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 14, 2024 at 01:51 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `esunscope`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `EmployeeID` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Position` varchar(50) DEFAULT NULL,
  `DateOfJoining` date DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`EmployeeID`, `Name`, `Department`, `Position`, `DateOfJoining`, `Location`) VALUES
(1, 'Alice', 'Sales', 'Manager', '2021-01-05', 'Berlin'),
(2, 'Mark', 'IT', 'Developer', '2020-02-12', 'Berlin'),
(3, 'Julia', 'HR', 'Executive', '2019-03-18', 'Berlin'),
(4, 'Oscar', 'Finance', 'Analyst', '2018-04-25', 'Berlin'),
(5, 'Sophie', 'Marketing', 'Specialist', '2021-05-10', 'Berlin'),
(6, 'Liam', 'Operations', 'Coordinator', '2022-06-11', 'Berlin'),
(7, 'Emma', 'Sales', 'Executive', '2019-07-15', 'London'),
(8, 'James', 'IT', 'Engineer', '2020-08-20', 'London'),
(9, 'Olivia', 'HR', 'Manager', '2021-09-10', 'London'),
(10, 'Henry', 'Finance', 'Executive', '2019-10-14', 'London'),
(11, 'Isabella', 'Marketing', 'Coordinator', '2018-11-19', 'London'),
(12, 'Amelia', 'Operations', 'Executive', '2022-12-23', 'London'),
(13, 'Benjamin', 'Sales', 'Representative', '2021-01-05', 'New York'),
(14, 'Elijah', 'IT', 'Developer', '2020-03-14', 'New York'),
(15, 'Emily', 'HR', 'Coordinator', '2021-04-20', 'New York'),
(16, 'David', 'Finance', 'Analyst', '2019-06-11', 'New York'),
(17, 'Mia', 'Marketing', 'Executive', '2022-07-25', 'New York'),
(18, 'Lucas', 'Operations', 'Manager', '2018-08-30', 'New York'),
(19, 'Sophia', 'Sales', 'Executive', '2021-09-04', 'Paris'),
(20, 'William', 'IT', 'Engineer', '2019-11-15', 'Paris'),
(21, 'Charlotte', 'HR', 'Executive', '2018-12-20', 'Paris'),
(22, 'Ava', 'Finance', 'Coordinator', '2020-01-18', 'Paris'),
(23, 'Isla', 'Marketing', 'Specialist', '2022-02-05', 'Paris'),
(24, 'Mason', 'Operations', 'Analyst', '2021-03-30', 'Paris'),
(25, 'Oliver', 'Sales', 'Manager', '2022-04-15', 'Tokyo'),
(26, 'Ethan', 'IT', 'Developer', '2019-05-22', 'Tokyo'),
(27, 'Ella', 'HR', 'Coordinator', '2020-06-27', 'Tokyo'),
(28, 'Jack', 'Finance', 'Executive', '2021-07-10', 'Tokyo'),
(29, 'Aiden', 'Marketing', 'Specialist', '2018-08-05', 'Tokyo'),
(30, 'Aria', 'Operations', 'Manager', '2019-09-18', 'Tokyo'),
(31, 'Grace', 'Sales', 'Representative', '2020-10-25', 'Berlin'),
(32, 'Finn', 'IT', 'Developer', '2021-11-30', 'Berlin'),
(33, 'Hannah', 'HR', 'Manager', '2018-01-14', 'Berlin'),
(34, 'Leo', 'Finance', 'Analyst', '2019-02-28', 'Berlin'),
(35, 'Zoe', 'Marketing', 'Coordinator', '2020-03-15', 'Berlin'),
(36, 'Noah', 'Operations', 'Executive', '2021-04-20', 'London'),
(37, 'Lily', 'Sales', 'Manager', '2022-05-25', 'London'),
(38, 'Sam', 'IT', 'Engineer', '2019-06-12', 'London'),
(39, 'Emma', 'HR', 'Coordinator', '2020-07-18', 'London'),
(40, 'Adam', 'Finance', 'Executive', '2021-08-23', 'London'),
(41, 'Chloe', 'Marketing', 'Specialist', '2018-09-10', 'London'),
(42, 'Eva', 'Operations', 'Manager', '2019-10-15', 'New York'),
(43, 'Ian', 'Sales', 'Executive', '2020-11-22', 'New York'),
(44, 'Sophia', 'IT', 'Developer', '2021-12-29', 'New York'),
(45, 'Owen', 'HR', 'Manager', '2018-01-10', 'New York');

-- --------------------------------------------------------

--
-- Table structure for table `workreports_year1`
--

CREATE TABLE `workreports_year1` (
  `EmployeeID` int(11) DEFAULT NULL,
  `Month` varchar(3) DEFAULT NULL,
  `ProjectsCompleted` int(11) DEFAULT NULL,
  `HoursWorked` int(11) DEFAULT NULL,
  `PerformanceScore` int(11) DEFAULT NULL,
  `FeedbackScore` decimal(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `workreports_year1`
--

INSERT INTO `workreports_year1` (`EmployeeID`, `Month`, `ProjectsCompleted`, `HoursWorked`, `PerformanceScore`, `FeedbackScore`) VALUES
(1, 'Jun', 9, 175, 90, 4.9),
(2, 'Jul', 6, 160, 84, 4.4),
(3, 'Aug', 5, 155, 82, 4.3),
(4, 'Sep', 7, 180, 88, 4.6),
(5, 'Oct', 6, 170, 85, 4.4),
(6, 'Nov', 5, 165, 83, 4.5),
(7, 'Dec', 8, 175, 91, 4.7),
(8, 'Jan', 7, 160, 86, 4.5),
(9, 'Feb', 6, 170, 88, 4.6),
(10, 'Mar', 9, 180, 90, 4.9),
(11, 'Apr', 8, 175, 89, 4.7),
(12, 'May', 5, 165, 82, 4.3),
(13, 'Jun', 6, 155, 80, 4.2),
(14, 'Jul', 7, 160, 84, 4.4),
(15, 'Aug', 9, 175, 92, 4.8),
(16, 'Sep', 8, 170, 89, 4.7),
(17, 'Oct', 7, 165, 86, 4.5),
(18, 'Nov', 6, 160, 83, 4.4),
(19, 'Dec', 5, 155, 80, 4.2),
(20, 'Jan', 8, 175, 91, 4.7),
(21, 'Feb', 9, 180, 94, 4.9),
(22, 'Mar', 7, 170, 88, 4.6),
(23, 'Apr', 6, 165, 85, 4.5),
(24, 'May', 5, 160, 82, 4.3),
(25, 'Jun', 8, 170, 90, 4.8),
(26, 'Jul', 7, 165, 87, 4.6),
(27, 'Aug', 9, 180, 93, 4.9),
(28, 'Sep', 6, 175, 88, 4.5),
(29, 'Oct', 5, 160, 84, 4.3),
(30, 'Nov', 8, 185, 92, 4.8),
(31, 'Dec', 7, 170, 85, 4.4),
(32, 'Jan', 6, 160, 82, 4.3),
(33, 'Feb', 5, 155, 80, 4.2),
(34, 'Mar', 9, 180, 91, 4.7),
(35, 'Apr', 8, 175, 90, 4.8),
(36, 'May', 7, 170, 87, 4.6),
(37, 'Jun', 6, 165, 85, 4.5),
(38, 'Jul', 5, 160, 83, 4.4),
(39, 'Aug', 9, 185, 94, 4.9),
(40, 'Sep', 8, 175, 92, 4.7),
(41, 'Oct', 7, 170, 89, 4.6),
(42, 'Nov', 6, 160, 84, 4.4),
(43, 'Dec', 5, 155, 81, 4.3),
(44, 'Jan', 8, 180, 93, 4.8),
(45, 'Feb', 9, 185, 95, 5.0);

-- --------------------------------------------------------

--
-- Table structure for table `workreports_year2`
--

CREATE TABLE `workreports_year2` (
  `EmployeeID` int(11) DEFAULT NULL,
  `Month` varchar(3) DEFAULT NULL,
  `ProjectsCompleted` int(11) DEFAULT NULL,
  `HoursWorked` int(11) DEFAULT NULL,
  `PerformanceScore` int(11) DEFAULT NULL,
  `FeedbackScore` decimal(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `workreports_year2`
--

INSERT INTO `workreports_year2` (`EmployeeID`, `Month`, `ProjectsCompleted`, `HoursWorked`, `PerformanceScore`, `FeedbackScore`) VALUES
(1, 'Jun', 5, 155, 80, 4.2),
(2, 'Jul', 7, 160, 85, 4.5),
(3, 'Aug', 6, 175, 88, 4.6),
(4, 'Sep', 8, 185, 92, 4.8),
(5, 'Oct', 9, 190, 95, 5.0),
(6, 'Nov', 5, 160, 83, 4.4),
(7, 'Dec', 7, 170, 89, 4.6),
(8, 'Jan', 6, 165, 86, 4.5),
(9, 'Feb', 9, 180, 92, 4.9),
(10, 'Mar', 8, 175, 90, 4.7),
(11, 'Apr', 7, 160, 84, 4.3),
(12, 'May', 5, 155, 81, 4.2),
(13, 'Jun', 8, 180, 91, 4.7),
(14, 'Jul', 9, 185, 94, 4.9),
(15, 'Aug', 6, 170, 87, 4.5),
(16, 'Sep', 7, 165, 85, 4.4),
(17, 'Oct', 5, 155, 80, 4.2),
(18, 'Nov', 8, 175, 90, 4.7),
(19, 'Dec', 6, 160, 83, 4.4),
(20, 'Jan', 9, 185, 95, 5.0),
(21, 'Feb', 7, 170, 89, 4.6),
(22, 'Mar', 5, 150, 78, 4.1),
(23, 'Apr', 8, 165, 88, 4.5),
(24, 'May', 6, 160, 84, 4.3),
(25, 'Jun', 9, 175, 93, 4.9),
(26, 'Jul', 7, 180, 90, 4.6),
(27, 'Aug', 8, 170, 88, 4.5),
(28, 'Sep', 5, 155, 81, 4.3),
(29, 'Oct', 6, 165, 85, 4.4),
(30, 'Nov', 7, 160, 83, 4.3),
(31, 'Dec', 9, 180, 94, 4.9),
(32, 'Jan', 8, 175, 92, 4.8),
(33, 'Feb', 6, 165, 87, 4.5),
(34, 'Mar', 7, 160, 85, 4.4),
(35, 'Apr', 5, 150, 80, 4.2),
(36, 'May', 9, 190, 95, 5.0),
(37, 'Jun', 8, 180, 93, 4.8),
(38, 'Jul', 7, 170, 89, 4.6),
(39, 'Aug', 6, 160, 86, 4.5),
(40, 'Sep', 9, 185, 91, 4.8),
(41, 'Oct', 8, 175, 90, 4.7),
(42, 'Nov', 5, 155, 82, 4.3),
(43, 'Dec', 7, 165, 87, 4.5),
(44, 'Jan', 6, 160, 84, 4.4),
(45, 'Feb', 9, 180, 93, 4.9);

-- --------------------------------------------------------

--
-- Table structure for table `workreports_year3`
--

CREATE TABLE `workreports_year3` (
  `EmployeeID` int(11) DEFAULT NULL,
  `Month` varchar(3) DEFAULT NULL,
  `ProjectsCompleted` int(11) DEFAULT NULL,
  `HoursWorked` int(11) DEFAULT NULL,
  `PerformanceScore` int(11) DEFAULT NULL,
  `FeedbackScore` decimal(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `workreports_year3`
--

INSERT INTO `workreports_year3` (`EmployeeID`, `Month`, `ProjectsCompleted`, `HoursWorked`, `PerformanceScore`, `FeedbackScore`) VALUES
(1, 'Jun', 7, 180, 90, 4.7),
(2, 'Jul', 6, 175, 86, 4.5),
(3, 'Aug', 9, 185, 92, 4.9),
(4, 'Sep', 8, 190, 91, 4.8),
(5, 'Oct', 5, 160, 82, 4.3),
(6, 'Nov', 7, 170, 87, 4.5),
(7, 'Dec', 6, 165, 85, 4.4),
(8, 'Jan', 8, 180, 89, 4.6),
(9, 'Feb', 9, 195, 95, 5.0),
(10, 'Mar', 7, 175, 88, 4.6),
(11, 'Apr', 5, 155, 80, 4.2),
(12, 'May', 8, 185, 91, 4.8),
(13, 'Jun', 9, 190, 94, 4.9),
(14, 'Jul', 6, 165, 83, 4.4),
(15, 'Aug', 7, 175, 87, 4.5),
(16, 'Sep', 5, 160, 82, 4.3),
(17, 'Oct', 9, 185, 93, 4.9),
(18, 'Nov', 8, 175, 90, 4.7),
(19, 'Dec', 6, 160, 84, 4.5),
(20, 'Jan', 7, 170, 86, 4.4),
(21, 'Feb', 8, 180, 89, 4.7),
(22, 'Mar', 9, 190, 92, 4.9),
(23, 'Apr', 5, 155, 81, 4.3),
(24, 'May', 6, 160, 83, 4.4),
(25, 'Jun', 7, 175, 88, 4.6),
(26, 'Jul', 8, 185, 91, 4.8),
(27, 'Aug', 9, 195, 95, 5.0),
(28, 'Sep', 6, 170, 85, 4.5),
(29, 'Oct', 5, 155, 80, 4.2),
(30, 'Nov', 8, 180, 90, 4.6),
(31, 'Dec', 7, 165, 87, 4.5),
(32, 'Jan', 9, 195, 94, 5.0),
(33, 'Feb', 6, 160, 84, 4.4),
(34, 'Mar', 5, 150, 78, 4.1),
(35, 'Apr', 8, 175, 89, 4.7),
(36, 'May', 7, 170, 86, 4.5),
(37, 'Jun', 6, 165, 83, 4.3),
(38, 'Jul', 9, 190, 91, 4.8),
(39, 'Aug', 8, 180, 89, 4.7),
(40, 'Sep', 5, 155, 82, 4.3),
(41, 'Oct', 7, 170, 85, 4.5),
(42, 'Nov', 6, 165, 84, 4.4),
(43, 'Dec', 9, 185, 93, 4.9),
(44, 'Jan', 8, 175, 90, 4.7),
(45, 'Feb', 7, 160, 85, 4.4);

-- --------------------------------------------------------

--
-- Table structure for table `workreports_year4`
--

CREATE TABLE `workreports_year4` (
  `EmployeeID` int(11) DEFAULT NULL,
  `Month` varchar(3) DEFAULT NULL,
  `ProjectsCompleted` int(11) DEFAULT NULL,
  `HoursWorked` int(11) DEFAULT NULL,
  `PerformanceScore` int(11) DEFAULT NULL,
  `FeedbackScore` decimal(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `workreports_year4`
--

INSERT INTO `workreports_year4` (`EmployeeID`, `Month`, `ProjectsCompleted`, `HoursWorked`, `PerformanceScore`, `FeedbackScore`) VALUES
(1, 'Jun', 5, 170, 84, 4.3),
(2, 'Jul', 7, 160, 85, 4.4),
(3, 'Aug', 9, 190, 93, 4.9),
(4, 'Sep', 6, 175, 89, 4.5),
(5, 'Oct', 8, 180, 91, 4.6),
(6, 'Nov', 7, 170, 88, 4.5),
(7, 'Dec', 6, 160, 83, 4.4),
(8, 'Jan', 9, 185, 93, 4.9),
(9, 'Feb', 8, 175, 90, 4.7),
(10, 'Mar', 7, 165, 85, 4.5),
(11, 'Apr', 5, 150, 79, 4.2),
(12, 'May', 6, 160, 82, 4.3),
(13, 'Jun', 8, 185, 91, 4.7),
(14, 'Jul', 9, 190, 94, 4.9),
(15, 'Aug', 7, 170, 87, 4.5),
(16, 'Sep', 6, 165, 84, 4.3),
(17, 'Oct', 8, 180, 90, 4.6),
(18, 'Nov', 5, 155, 81, 4.2),
(19, 'Dec', 9, 185, 93, 4.9),
(20, 'Jan', 8, 175, 89, 4.6),
(21, 'Feb', 7, 160, 85, 4.4),
(22, 'Mar', 6, 170, 83, 4.3),
(23, 'Apr', 9, 190, 94, 5.0),
(24, 'May', 8, 185, 92, 4.8),
(25, 'Jun', 5, 150, 80, 4.1),
(26, 'Jul', 6, 160, 82, 4.3),
(27, 'Aug', 7, 170, 86, 4.4),
(28, 'Sep', 9, 195, 95, 5.0),
(29, 'Oct', 8, 180, 90, 4.7),
(30, 'Nov', 6, 165, 84, 4.4),
(31, 'Dec', 7, 170, 87, 4.5),
(32, 'Jan', 8, 180, 91, 4.6),
(33, 'Feb', 5, 150, 78, 4.2),
(34, 'Mar', 9, 190, 94, 4.9),
(35, 'Apr', 7, 175, 89, 4.7),
(36, 'May', 6, 160, 83, 4.4),
(37, 'Jun', 9, 185, 92, 4.8),
(38, 'Jul', 8, 180, 90, 4.7),
(39, 'Aug', 5, 155, 81, 4.3),
(40, 'Sep', 7, 165, 85, 4.5),
(41, 'Oct', 6, 150, 80, 4.2),
(42, 'Nov', 8, 175, 88, 4.6),
(43, 'Dec', 9, 190, 93, 4.9),
(44, 'Jan', 7, 170, 86, 4.5),
(45, 'Feb', 6, 160, 82, 4.3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`EmployeeID`);

--
-- Indexes for table `workreports_year1`
--
ALTER TABLE `workreports_year1`
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Indexes for table `workreports_year2`
--
ALTER TABLE `workreports_year2`
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Indexes for table `workreports_year3`
--
ALTER TABLE `workreports_year3`
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Indexes for table `workreports_year4`
--
ALTER TABLE `workreports_year4`
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `workreports_year1`
--
ALTER TABLE `workreports_year1`
  ADD CONSTRAINT `workreports_year1_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`);

--
-- Constraints for table `workreports_year2`
--
ALTER TABLE `workreports_year2`
  ADD CONSTRAINT `workreports_year2_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`);

--
-- Constraints for table `workreports_year3`
--
ALTER TABLE `workreports_year3`
  ADD CONSTRAINT `workreports_year3_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`);

--
-- Constraints for table `workreports_year4`
--
ALTER TABLE `workreports_year4`
  ADD CONSTRAINT `workreports_year4_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
