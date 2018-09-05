get_totals = "SELECT arbiter_id, sc1 + sc2 + sc3 AS total_extremes FROM"

print_simple_query(cnx, """
SELECT s.arbiter_id, s.first_criterion, s.second_criterion, s.third_criterion FROM
scores AS s INNER JOIN
(
SELECT arbiter_id, first_criterion IN
(SELECT MAX(first_criterion) AS ext1 FROM scores
UNION ALL
SELECT MIN(first_criterion) AS ext1 FROM scores
) AS sc1,
second_criterion IN
(SELECT MAX(second_criterion) AS ext2 FROM scores
UNION ALL
SELECT MIN(second_criterion) AS ext2 FROM scores
) AS sc2,
third_criterion IN
(SELECT MAX(third_criterion) AS ext3 FROM scores
UNION ALL
SELECT MIN(third_criterion) AS ext3 FROM scores
) AS sc3
FROM scores) AS t
ON t.arbiter_id = s.arbiter_id
WHERE t.sc1 + t.sc2 + t.sc3 < 2
""")


print_simple_query(cnx, """
SELECT ext1 FROM
(SELECT MAX(first_criterion) AS ext1 FROM scores
UNION ALL
SELECT MIN(first_criterion) AS ext1 FROM scores
) AS SC1""") 

def nothing(x):
    pass


nothing("""
CREATE PROCEDURE dancingCompetition()
BEGIN
	CREATE TEMPORARY TABLE IF NOT EXISTS extreme1
SELECT MAX(first_criterion) AS EXT1 FROM scores
UNION ALL
SELECT MIN(first_criterion) AS EXT1 FROM scores;

SELECT * FROM extreme1;

DROP TEMPORARY TABLE extreme1;

END;""")

nothing("""
CALL dancingCompetition();
""")

def test():
    pass
