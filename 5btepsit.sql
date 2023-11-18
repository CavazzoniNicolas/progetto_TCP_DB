-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 16, 2023 alle 17:04
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5btepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_nicolas_cavazzoni`
--

CREATE TABLE `dipendenti_nicolas_cavazzoni` (
  `id` int(11) NOT NULL,
  `nome` char(30) NOT NULL,
  `cognome` char(30) NOT NULL,
  `posizione_lavoro` char(60) NOT NULL,
  `data_assunzione` date NOT NULL,
  `stipendio` float NOT NULL,
  `telefono` char(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `dipendenti_nicolas_cavazzoni`
--

INSERT INTO `dipendenti_nicolas_cavazzoni` (`id`, `nome`, `cognome`, `posizione_lavoro`, `data_assunzione`, `stipendio`, `telefono`) VALUES
(1, 'marco', 'rossi', 'operaio', '2017-08-30', 1500, '3892834419'),
(2, 'riccardo', 'bianchi', 'dirigente', '2013-03-10', 2500, '3992834423'),
(3, 'massimo', 'verdi', 'magazziniere', '2021-10-20', 1400, '3892554416'),
(4, 'mirco', 'morato', 'operaio', '2023-09-11', 1000, '399556697'),
(5, 'nicolas', 'pallini', 'commerciale', '2019-01-30', 2000, '3332834418');

-- --------------------------------------------------------

--
-- Struttura della tabella `zona_di_lavoro_nicolas_cavazzoni`
--

CREATE TABLE `zona_di_lavoro_nicolas_cavazzoni` (
  `id` int(11) NOT NULL,
  `nome` char(30) NOT NULL,
  `numero_clienti` int(30) NOT NULL,
  `metri_quadri` float NOT NULL,
  `dipendente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zona_di_lavoro_nicolas_cavazzoni`
--

INSERT INTO `zona_di_lavoro_nicolas_cavazzoni` (`id`, `nome`, `numero_clienti`, `metri_quadri`, `dipendente`) VALUES
(1, 'marco', 10, 50, 2),
(2, 'mattia', 5, 60, 1),
(3, 'giacomo', 5, 40, 3),
(4, 'paolo', 6, 80, 5),
(5, 'mauro', 7, 65, 4);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_nicolas_cavazzoni`
--
ALTER TABLE `dipendenti_nicolas_cavazzoni`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `zona_di_lavoro_nicolas_cavazzoni`
--
ALTER TABLE `zona_di_lavoro_nicolas_cavazzoni`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dipendente` (`dipendente`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_nicolas_cavazzoni`
--
ALTER TABLE `dipendenti_nicolas_cavazzoni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `zona_di_lavoro_nicolas_cavazzoni`
--
ALTER TABLE `zona_di_lavoro_nicolas_cavazzoni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zona_di_lavoro_nicolas_cavazzoni`
--
ALTER TABLE `zona_di_lavoro_nicolas_cavazzoni`
  ADD CONSTRAINT `zona_di_lavoro_nicolas_cavazzoni_ibfk_1` FOREIGN KEY (`dipendente`) REFERENCES `dipendenti_nicolas_cavazzoni` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
