-- This script creates a trigger that updates a column when the email is changed
DELIMITER ~
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF NEW.email != OLD.email THEN 
			CASE 
				WHEN NEW.valid_email = 0 THEN
					SET NEW.valid_email = 1;
				ELSE 
					SET NEW.valid_email = 0;
			END CASE;
		END IF;
	END~
DELIMITER ;
