-- find winner

CREATE TEMPORARY TABLE winner_table AS
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
GROUP BY game_winner
END

-- combine away games goals

CREATE TEMPORARY TABLE away_goals_table AS
SELECT SUM(away_goals) AS away_goals, guest_team FROM
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
GROUP BY team
END



-- find away game goals

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
END AS guest_team

FROM scores


/*
id goal_diff, game_winner
1 	2 	1
2 	1 	1
3 	-2 	2
4 	1 	1
5 	-2 	2
6 	-2 	2
7 	2 	1
8 	-1 	2
9 	-1 	2
10 	2 	1
11 	1 	1
12 	-1 	2


*/
