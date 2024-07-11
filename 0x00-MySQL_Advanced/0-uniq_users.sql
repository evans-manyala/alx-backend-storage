-- Task: Create a table 'users' with specified attributes if it does not already exist.
-- Creating the 'users' table with id, email, and name columns
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
)