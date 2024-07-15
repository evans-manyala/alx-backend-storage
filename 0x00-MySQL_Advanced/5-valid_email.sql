-- SQL script that creates a trigger that resets
-- the attribute valid_email only when the email
-- has been changed

DELIMITER //  -- Change the delimiter

CREATE TRIGGER reset_valid_email 
BEFORE UPDATE ON users
FOR EACH ROW
WHEN (NEW.email <> OLD.email)
BEGIN
    SET NEW.valid_email = 0;
END//

DELIMITER ;
