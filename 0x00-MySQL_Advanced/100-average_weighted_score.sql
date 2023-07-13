-- This script creates a procedure that calculates the weighted average
-- score of students and feeds the data into the database
DELIMITER ~
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	SELECT (SUM(corrections.score * projects.weight) / SUM(projects.weight)) INTO
	@score FROM corrections JOIN projects WHERE corrections.user_id = user_id
	AND projects.id = corrections.project_id;

	UPDATE users SET average_score = @score WHERE id = user_id;
END~
DELIMITER ;
