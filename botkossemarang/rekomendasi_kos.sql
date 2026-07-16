-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 16, 2026 at 03:12 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rekomendasi_kos`
--

-- --------------------------------------------------------

--
-- Table structure for table `indekos`
--

CREATE TABLE `indekos` (
  `id` int(11) NOT NULL,
  `nama_kos` varchar(100) NOT NULL,
  `gender` enum('Putra','Putri') NOT NULL,
  `kategori_kampus` enum('Negeri','Swasta') NOT NULL,
  `nama_kampus` varchar(50) NOT NULL,
  `harga` int(100) NOT NULL,
  `fasilitas` varchar(255) NOT NULL,
  `link_mamikos` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indekos`
--

INSERT INTO `indekos` (`id`, `nama_kos`, `gender`, `kategori_kampus`, `nama_kampus`, `harga`, `fasilitas`, `link_mamikos`) VALUES
(1, 'Kost Raya Tipe VVIP (UNNES)', 'Putra', 'Negeri', 'UNNES', 1500000, 'KM Dalam, AC, WiFi, TV, Kulkas, Springbed', 'https://mamikos.com/room/kost-semarang-kost-putra-eksklusif-kost-raya-tipe-vvip-gunung-pati-semarang?redirection_source=landing%20area'),
(2, 'Kost Bella (UNNES)', 'Putra', 'Negeri', 'UNNES', 500000, 'Kasur, Lemari, Kamar Mandi Luar', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-bella-gunung-pati-semarang?redirection_source=landing%20area'),
(3, 'Kost Smart 4 Kedawung (UNNES)', 'Putra', 'Negeri', 'UNNES', 700000, 'Kasur, Lemari, WiFi, Meja Belajar', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-smart-4-kedawung-standart-gunung-pati-semarang?redirection_source=landing%20area'),
(4, 'Kost Sinta Pink Tipe A (UNNES)', 'Putri', 'Negeri', 'UNNES', 600000, 'Kasur, Lemari, WiFi', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-sinta-pink-tipe-a-gunung-pati-semarang?redirection_source=landing%20area'),
(5, 'Kost Pink (UNNES)', 'Putri', 'Negeri', 'UNNES', 550000, 'Kasur, Lemari, Dapur Bersama', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-pink-gunung-pati-semarang?redirection_source=landing%20area'),
(6, 'Kost Griya Carmel (UNNES)', 'Putri', 'Negeri', 'UNNES', 650000, 'Kasur, Lemari, WiFi, Parkir Motor', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-griya-carmel-gunung-pati-semarang-2?redirection_source=landing%20area'),
(7, 'Kost Undip 19 (UNDIP)', 'Putra', 'Negeri', 'UNDIP', 750000, 'Kasur, Lemari, WiFi', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-undip-19-tembalang-semarang-2?redirection_source=landing%20area'),
(8, 'Kost Hijau Tipe D (UNDIP)', 'Putra', 'Negeri', 'UNDIP', 850000, 'Kasur, Lemari, WiFi, Meja Belajar', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-hijau-tipe-d-tembalang-semarang-2?redirection_source=landing%20area'),
(9, 'Kost Corvettee Executive (UNDIP)', 'Putra', 'Negeri', 'UNDIP', 1800000, 'KM Dalam, AC, WiFi, Water Heater, Springbed', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-corvettee-executive-tembalang-semarang-2?redirection_source=landing%20area'),
(10, 'Wisma Citra Exclusive (UNDIP)', 'Putri', 'Negeri', 'UNDIP', 1600000, 'KM Dalam, AC, WiFi, TV, Kulkas', 'https://mamikos.com/room/kost-semarang-kost-putri-eksklusif-kost-wisma-citra-tipe-exclusive-tembalang-semarang?redirection_source=landing%20area'),
(11, 'Kost Anindya (UNDIP)', 'Putri', 'Negeri', 'UNDIP', 800000, 'Kasur, Lemari, WiFi, KM Luar', 'https://mamikos.com/room/kost-semarang-kost-putri-murah-kost-anindya-tembalang-semarang?redirection_source=landing%20area'),
(12, 'Kost Hanisha Executive (UNDIP)', 'Putri', 'Negeri', 'UNDIP', 1700000, 'KM Dalam, AC, WiFi, Springbed, Akses Kartu', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-hanisha-tipe-executive-tembalang-semarang?redirection_source=landing%20area'),
(13, 'Kost Wisma Genius (POLINES)', 'Putra', 'Negeri', 'POLINES', 600000, 'Kasur, Lemari, WiFi', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-wisma-genius-banyumanik-semarang?redirection_source=landing%20area'),
(14, 'Kost JN VVIP (POLINES)', 'Putra', 'Negeri', 'POLINES', 1400000, 'KM Dalam, AC, WiFi, Kloset Duduk', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-jn-vvip-banyumanik-semarang?redirection_source=landing%20area'),
(15, 'Kost Putra Free Wifi (POLINES)', 'Putra', 'Negeri', 'POLINES', 550000, 'WiFi, Kasur, KM Luar', 'https://mamikos.com/room/kost-semarang-kost-putra-murah-kost-putra-free-wifi-km-luar-area-undip-tembalang-semarang?redirection_source=landing%20area'),
(16, 'Kost Marven (POLINES)', 'Putri', 'Negeri', 'POLINES', 1300000, 'KM Dalam, AC, WiFi, Springbed', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-marven-tembalang-semarang?redirection_source=landing%20area'),
(17, 'Kost Anindya Tembalang (POLINES)', 'Putri', 'Negeri', 'POLINES', 800000, 'Kasur, Lemari, WiFi', 'https://mamikos.com/room/kost-semarang-kost-putri-murah-kost-anindya-tembalang-semarang?redirection_source=landing%20area'),
(18, 'Kost Jasmine Tipe B (POLINES)', 'Putri', 'Negeri', 'POLINES', 1200000, 'KM Dalam, AC, WiFi, Kloset Duduk', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-jasmine-tipe-b-tembalang-semarang-2?redirection_source=landing%20area'),
(19, 'Kost Gede Arya Tipe A (UIN)', 'Putra', 'Negeri', 'UIN Walisongo', 500000, 'Kasur, Lemari, KM Luar', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-gede-arya-tipe-a-tugu-semarang-2?redirection_source=landing%20area'),
(20, 'Kost Salim (UIN)', 'Putra', 'Negeri', 'UIN Walisongo', 1100000, 'KM Dalam, AC, WiFi, Kloset Duduk', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-salim-tugu-semarang-barat?redirection_source=landing%20area'),
(21, 'Kost Tanti 1 Tipe A (UIN)', 'Putra', 'Negeri', 'UIN Walisongo', 1000000, 'KM Dalam, AC, WiFi', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-tanti-1-tipe-a-tugu-semarang?redirection_source=landing%20area'),
(22, 'Kost Takazi Tipe B (UIN)', 'Putri', 'Negeri', 'UIN Walisongo', 600000, 'Kasur, Lemari, WiFi, Akses 24 Jam', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-takazi-tipe-b-ngaliyan-semarang-1?redirection_source=landing%20area'),
(23, 'Kost Supriyono Tipe C (UIN)', 'Putri', 'Negeri', 'UIN Walisongo', 550000, 'Kasur, Lemari, WiFi', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-supriyono-tipe-c-ngaliyan-semarang?redirection_source=landing%20area'),
(24, 'Kost Ara Tipe B (UIN)', 'Putri', 'Negeri', 'UIN Walisongo', 650000, 'Kasur, Lemari, KM Luar, Parkir', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-ara-tipe-b-tugu-semarang-2?redirection_source=landing%20area'),
(25, 'Kost Nurul Khaqiqoh Pavilium (UDINUS)', 'Putra', 'Swasta', 'UDINUS', 1500000, 'KM Dalam, AC, WiFi, Springbed, Eksklusif', 'https://mamikos.com/room/kost-kota-semarang-kost-campur-eksklusif-kost-nurul-khaqiqoh-pavilium-semarang-tengah-semarang-1?redirection_source=landing%20area'),
(26, 'Kost Torisan 1 Executive (UDINUS)', 'Putra', 'Swasta', 'UDINUS', 1800000, 'KM Dalam, AC, WiFi, TV, Kulkas', 'https://mamikos.com/room/kost-kota-semarang-kost-campur-eksklusif-kost-torisan-1-executive-semarang-tengah-semarang?redirection_source=landing%20area'),
(27, 'Kost MK (UDINUS)', 'Putri', 'Swasta', 'UDINUS', 650000, 'Kasur, Lemari, WiFi, Murah', 'https://mamikos.com/room/kost-semarang-kost-putri-murah-kost-mk-semarang-tengah-1?redirection_source=landing%20area'),
(28, 'Kost Nara 12 Tipe A (UDINUS)', 'Putri', 'Swasta', 'UDINUS', 750000, 'Kasur, Lemari, WiFi, Strategis', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-nara-12-tipe-a-semarang-tengah-semarang?redirection_source=landing%20area'),
(29, 'Kost Ungu Udinus Tipe A (UDINUS)', 'Putri', 'Swasta', 'UDINUS', 800000, 'Kasur, Lemari, Akses 24 Jam, Dekat Kampus', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-ungu-udinus-tipe-a-semarang-tengah-semarang?redirection_source=landing%20area'),
(30, 'Kost Suhardi (UNISBANK)', 'Putra', 'Swasta', 'UNISBANK', 500000, 'Kasur, Lemari, KM Luar, Murah', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-suhardi-semarang-selatan-semarang?redirection_source=landing%20area'),
(31, 'Kost Alfahanin 05 Tipe B (UNISBANK)', 'Putra', 'Swasta', 'UNISBANK', 1200000, 'KM Dalam, AC, WiFi, Springbed', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-alfahanin-05-tipe-b-semarang-selatan-semarang-2?redirection_source=landing%20area'),
(32, 'Kost Alfahanin 05 Tipe C (UNISBANK)', 'Putra', 'Swasta', 'UNISBANK', 1300000, 'KM Dalam, AC, WiFi, Springbed, Luas', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-alfahanin-05-tipe-c-semarang-selatan-semarang?redirection_source=landing%20area'),
(33, 'Kost V2 AC (UNISBANK)', 'Putri', 'Swasta', 'UNISBANK', 1400000, 'KM Dalam, AC, WiFi, Kloset Duduk', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-v2-ac-semarang-tengah-semarang-2?redirection_source=landing%20area'),
(34, 'Kost V2 Non AC (UNISBANK)', 'Putri', 'Swasta', 'UNISBANK', 900000, 'KM Dalam, WiFi, Kipas Angin, Kloset Duduk', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-v2-non-ac-semarang-tengah-semarang?redirection_source=landing%20area'),
(35, 'Kost Tlogo Bayem (UNISBANK)', 'Putri', 'Swasta', 'UNISBANK', 550000, 'Kasur, Lemari, KM Luar, Murah', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-tlogo-bayem-semarang-selatan-semarang?redirection_source=landing%20area'),
(36, 'Kost Febby Genuk (UNISSULA)', 'Putra', 'Swasta', 'UNISSULA', 500000, 'Kasur, Lemari, KM Luar, Parkir', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-febby-genuk-semarang-2?redirection_source=landing%20area'),
(37, 'Kost Kahf Tipe A (UNISSULA)', 'Putra', 'Swasta', 'UNISSULA', 1100000, 'KM Dalam, AC, WiFi, Springbed', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-eksklusif-kost-kahf-tipe-a-genuk-semarang?redirection_source=landing%20area'),
(38, 'Kost Tasnim Tipe A (UNISSULA)', 'Putra', 'Swasta', 'UNISSULA', 600000, 'Kasur, Lemari, WiFi, Murah', 'https://mamikos.com/room/kost-kota-semarang-kost-putra-murah-kost-tasnim-tipe-a-genuk-semarang-3?redirection_source=landing%20area'),
(39, 'Kost VIP Genuk (UNISSULA)', 'Putri', 'Swasta', 'UNISSULA', 1500000, 'KM Dalam, AC, WiFi, Kulkas, VIP', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-eksklusif-kost-vip-genuk-semarang?redirection_source=landing%20area'),
(40, 'Kost Ninaaa Genuk (UNISSULA)', 'Putri', 'Swasta', 'UNISSULA', 600000, 'Kasur, Lemari, KM Luar', 'https://mamikos.com/room/kost-kost-putri-murah-kost-ninaaa-genuk-semarang-1?redirection_source=landing%20area'),
(41, 'Kost B113 Padi Raya Tipe A (UNISSULA)', 'Putri', 'Swasta', 'UNISSULA', 700000, 'Kasur, Lemari, WiFi, Bersih', 'https://mamikos.com/room/kost-kota-semarang-kost-putri-murah-kost-b113-padi-raya-tipe-a-genuk-semarang-2?redirection_source=landing%20area'),
(42, 'Kost Citarum Pandansari (USM)', 'Putri', 'Swasta', 'USM', 1300000, 'KM Dalam, AC, WiFi, Kloset Duduk', 'https://mamikos.com/kost/kost-dekat-usm-semarang-murah'),
(43, 'Kost Wisma Aruna (USM)', 'Putri', 'Swasta', 'USM', 1100000, 'KM Dalam, AC, WiFi, Kasur', 'https://mamikos.com/kost/kost-dekat-usm-semarang-murah'),
(44, 'Kost Kita Jaya (USM)', 'Putra', 'Swasta', 'USM', 1100000, 'KM Dalam, WiFi, AC, Kloset Duduk', 'https://mamikos.com/kost/kost-dekat-usm-semarang-murah');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `indekos`
--
ALTER TABLE `indekos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `indekos`
--
ALTER TABLE `indekos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
