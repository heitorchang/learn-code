/*Please add ; after each select statement*/
CREATE PROCEDURE soccerGameSeries()
BEGIN
DECLARE wins1 INT;
DECLARE wins2 INT;
DECLARE goals1 INT;
DECLARE goals2 INT;
DECLARE goaldiff INT;
DECLARE away1 INT;
DECLARE away2 INT;

/*
DROP TEMPORARY TABLE winner_table;
DROP TEMPORARY TABLE away_goals_table;
*/

CREATE TEMPORARY TABLE IF NOT EXISTS winner_table
SELECT game_winner AS team, COUNT(game_winner) AS games_won, SUM(goal_difference) AS overall_goal_diff FROM
(
SELECT match_id, first_team_score - second_team_score AS goal_difference,
CASE
WHEN first_team_score - second_team_score > 0
THEN (SELECT 1)
WHEN first_team_score - second_team_score < 0
THEN (SELECT 2)
ELSE (SELECT 0)
END AS game_winner
FROM scores
) AS goal_diff
GROUP BY game_winner;


CREATE TEMPORARY TABLE IF NOT EXISTS away_goals_table
SELECT SUM(away_goals) AS away_goals, team FROM
(
SELECT match_id, first_team_score, second_team_score, match_host, first_team_score - second_team_score AS goal_difference,
CASE
WHEN first_team_score - second_team_score > 0
THEN (SELECT 1)
WHEN first_team_score - second_team_score < 0
THEN (SELECT 2)
ELSE (SELECT 0)
END AS game_winner,

CASE
WHEN match_host = 1
THEN (SELECT second_team_score)
ELSE (SELECT first_team_score)
END AS away_goals,

CASE
WHEN match_host = 2
THEN (SELECT 1)
ELSE (SELECT 2)
END AS team

FROM scores
) AS away_goals
GROUP BY team;

/*
SET wins1 = (SELECT games_won FROM winner_table WHERE team = 1);
*/
SET wins2 = (SELECT games_won FROM winner_table WHERE team = 2);

SET goals1 = (SELECT overall_goal_diff FROM winner_table WHERE team=1);
SET goals2 = (SELECT overall_goal_diff FROM winner_table WHERE team=2);
SET goaldiff = goals1+goals2;

SET away1 = (SELECT away_goals FROM away_goals_table WHERE team = 1);
SET away2 = (SELECT away_goals FROM away_goals_table WHERE team = 2);


SELECT games_won INTO wins1 FROM winner_table WHERE team = 1;

IF wins1 > wins2 THEN (SELECT 1 AS winner);
ELSEIF wins2 > wins1 THEN (SELECT 2 AS winner);
ELSE 
 IF goaldiff > 0 THEN (SELECT 1 AS winner);
 ELSEIF goaldiff < 0 THEN (SELECT 2 AS winner);
 ELSE
  IF away1 > away2 THEN (SELECT 1 AS winner);
  ELSEIF away2 > away1 THEN (SELECT 2 AS winner);
  ELSE
   (SELECT 0 AS winner);
  END IF;
 END IF;
END IF;

DROP TEMPORARY TABLE winner_table;
DROP TEMPORARY TABLE away_goals_table;
END
