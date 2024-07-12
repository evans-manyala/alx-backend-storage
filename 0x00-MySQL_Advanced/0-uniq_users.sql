-- Task: Create a table 'users' with specified attributes if it does not already exist.
-- Creating the 'users' table with id, email, and name columns

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
