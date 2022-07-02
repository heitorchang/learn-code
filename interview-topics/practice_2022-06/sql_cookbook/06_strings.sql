-- 6.1 walking a string

-- original
select substr(e.ename, iter.pos, 1) as c
  from (select ename from emp where ename = 'KING') e,
  (select id as pos from t10 order by id) iter
where iter.pos <= length(e.ename);

-- better (uses generate_series)
select substr(e.ename, iter.pos, 1) as c
  from (select ename from emp where ename = 'KING') e,
  (select generate_series(1, 10) as pos) iter -- large enough limit
where iter.pos <= length(e.ename);

-- cumulative substrings
select substr(e.ename, iter.pos) a,
  substr(e.ename, length(e.ename) - iter.pos + 1) b
  from (select ename from emp where ename = 'KING') e,
  (select generate_series(1, 10) as pos) iter -- large enough limit
where iter.pos <= length(e.ename);


-- CTE solution that does not depend on T10 pivot table or hardcoded
--   constants
with ename_cte as (
	select ename, max(length(ename)) as emax from emp where ename in ('KING', 'CLARK')
	group by ename
), iter as (
    select generate_series(1, max(length(ename))) as pos
	from ename_cte
)
select pos, substr(e.ename, iter.pos, 1) as c
from ename_cte e, iter
where iter.pos <= length(e.ename)
group by iter.pos, e.ename
order by e.ename, pos;


-- 6.2 embedding quotes in string literals

use '', for example: select 'g''day mate' qmarks from t1;
The string literal '' in NULL

-- 6.3
