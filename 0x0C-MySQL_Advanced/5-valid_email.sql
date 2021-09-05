-- Create a trigger that resets the attribute valid_email when the email has been changed.
DELIMITER $$
CREATE TRIGGER email_correct BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
	   SET NEW.valid_email = 0;
	END IF;
END;$$
DELIMITER ;
