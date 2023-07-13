-- This script calculates average and updates appropriate table with resulting value
DELIMITER ~
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	SELECT SUM(score) INTO @sum FROM corrections
	WHERE corrections.user_id = user_id;

	SELECT COUNT(*) INTO @count FROM corrections
	WHERE corrections.user_id = user_id;

	UPDATE users SET average_score = ((SELECT @sum) / (SELECT @count))
	WHERE users.id = user_id;
END~
DELIMITER ;
