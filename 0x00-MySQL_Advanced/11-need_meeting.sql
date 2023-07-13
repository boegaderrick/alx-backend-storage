-- This script creates a view
DELIMITER ~
CREATE VIEW need_meeting AS (
	SELECT * FROM students WHERE score < 80
	WHERE last_meeting = NULL OR
	TIMESTAMPDIFF(MONTH, last_meeting, CURDATE()) > 1;
)~
DELIMITER ;
