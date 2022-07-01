-- 3.1 stacking rowsets

select ename as ename_and_dname, deptno
from emp
where deptno = 10
union all
select '----------', null
from t1
union all
select dname, deptno
from dept;

-- UNION most likely sorts to remove duplicates, so it may come with
-- a performance cost


-- 3.2 combining related rows

select e.ename, d.loc
from emp e
join dept d
on e.deptno = d.deptno
where e.deptno = 10;


-- 3.3 finding rows in common between two tables

create view V3_3
as
select ename, job, sal
from emp
where job = 'CLERK';

select empno, ename, job, sal, deptno
from emp
where (ename, job, sal) in (
  select ename, job, sal from emp
  intersect
  select ename, job, sal from V3_3
);


-- 3.4 retrieving values from one table that do not exist in another

select deptno from dept
except
select deptno from emp;

-- correlated subquery: rows from the outer query are referenced in the subquery.

select d.deptno
from dept d
where not exists (
  select 1
  from emp e
  where d.deptno = e.deptno
);
