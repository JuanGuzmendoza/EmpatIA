-- Crear base de datos y tablas
CREATE DATABASE IF NOT EXISTS EmpatIA;
USE EmpatIA;

CREATE TABLE IF NOT EXISTS genres (
    id_genre INT AUTO_INCREMENT PRIMARY KEY,
    genre_type VARCHAR(50) NOT NULL,
    abbreviation VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
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
    CONSTRAINT fk_users_genres FOREIGN KEY (id_genre) REFERENCES genres(id_genre) ON UPDATE CASCADE
);

-- Insertar género de prueba
INSERT INTO genres (genre_type, abbreviation) VALUES ('Masculino', 'M');

-- Insertar usuario de prueba
INSERT INTO users (
    full_name,
    username,
    email,
    password_user,
    national_id,
    age,
    id_genre,
    country,
    city,
    phone,
    emergency_contact,
    address,
    user_profile
) VALUES (
    'Juan Pérez',
    'juanp',
    'juanp@example.com',
    '123456',
    '123456789',
    30,
    1, -- id_genre del género insertado arriba
    'Colombia',
    'Bogotá',
    '3001234567',
    '3109876543',
    'Calle 123 #45-67',
    'juanp_profile'
);