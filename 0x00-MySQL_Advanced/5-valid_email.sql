-- SQL script that creates a trigger that resets
-- the attribute valid_email only when the email
-- has been changed

CREATE OR REPLACE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
WHEN (NEW.email <> OLD.email)
BEGIN
    NEW.valid_email = false;
END;
