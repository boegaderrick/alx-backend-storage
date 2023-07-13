-- This script creates a view
CREATE VIEW need_meeting AS (
	SELECT * FROM students WHERE score < 80
	AND (last_meeting IS NULL OR
	TIMESTAMPDIFF(MONTH, last_meeting, CURDATE()) > 1)
);
