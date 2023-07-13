-- This script creates a trigger to reduce stock after every order
DELIMITER ~
CREATE TRIGGER decrease_qtty
AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END~
DELIMITER ;
