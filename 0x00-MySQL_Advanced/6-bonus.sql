-- This script inserts rows into tables
DELIMITER ~
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END~
DELIMITER ;
