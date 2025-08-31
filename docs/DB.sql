CREATE DATABASE EmpatIA;

USE EmpatIA;

-- Tabla de géneros
CREATE TABLE genres (
    id_genre INT AUTO_INCREMENT PRIMARY KEY,
    genre_type VARCHAR(50) NOT NULL,
    abbreviation VARCHAR(10) NOT NULL
);

-- Tabla de usuarios
CREATE TABLE users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_user VARCHAR(255) NOT NULL,
    national_id VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL,
    id_genre INT NOT NULL,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    emergency_contact VARCHAR(20),
    address VARCHAR(255),
    user_profile VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Relación con genres
    CONSTRAINT fk_users_genres FOREIGN KEY (id_genre) REFERENCES genres(id_genre) ON UPDATE CASCADE
);