-- This script creates a procedure that calculates the weighted average
-- score of students and feeds the data into the database
DELIMITER ~
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_id INT;
	DECLARE done INT DEFAULT 0;
	DECLARE curs CURSOR FOR SELECT id FROM users;

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	
	OPEN curs;
	FETCH curs INTO user_id;

	WHILE (done = 0) DO
		SELECT (SUM(corrections.score * projects.weight) / SUM(projects.weight)) INTO
		@score FROM corrections JOIN projects WHERE corrections.user_id = user_id
		AND projects.id = corrections.project_id;

		UPDATE users SET average_score = @score WHERE id = user_id;

		FETCH curs INTO user_id;
	END WHILE;

	CLOSE curs;
END~

DELIMITER ;
