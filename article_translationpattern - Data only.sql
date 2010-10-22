-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 22, 2010 at 04:26 PM
-- Server version: 5.1.41
-- PHP Version: 5.3.2-1ubuntu4.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mongoose-django`
--

--
-- Dumping data for table `article_translationpattern`
--

INSERT INTO `article_translationpattern` (`id`, `needle`, `replace`) VALUES
(1, '\\[b\\]', '<strong>'),
(2, '\\[/b\\]', '</strong>'),
(3, '\\[i\\]', '<em>'),
(4, '\\[/i\\]', '</em>'),
(5, '===(.*)===', '<h2>\\1</h2>'),
(6, '==(.*)==', '<h3>\\1</h3>'),
(7, '\\n\\*[ ]([^\\n]+)', '\\n<li>\\1</li>'),
(8, '\\[section\\]', '<p>'),
(9, '\\[/section\\]', '</p>'),
(10, '\\[\\[(\\w+)\\]\\]', '<a href="/article/view/\\1">\\1</a>'),
(11, '\\[([^\\s\\]]+)[ ](.[^\\[]+)\\]', '<a href="\\1">\\2</a>');
