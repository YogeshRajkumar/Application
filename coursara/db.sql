-- Database: littlelemon

CREATE DATABASE IF NOT EXISTS littlelemon;
USE littlelemon;

-- Table: restaurant_menuitem
CREATE TABLE IF NOT EXISTS restaurant_menuitem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price DECIMAL(6,2) NOT NULL,
    inventory INT NOT NULL
);

-- Table: restaurant_booking
CREATE TABLE IF NOT EXISTS restaurant_booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    no_of_guests INT NOT NULL,
    booking_date DATE NOT NULL
);
