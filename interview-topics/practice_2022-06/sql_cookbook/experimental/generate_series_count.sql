-- simple solution

select extract(year from hiredate) as yr, extract(month from hiredate) as mo, count(*) as ct
from emp
group by yr, mo;


with cte as (
select t.i, count(*) as ct from generate_series('01-jan-2006'::date, '01-jan-2007'::date, '1 month') as t(i), emp e
where e.hiredate >= i and e.hiredate < i + interval '1 month'
group by i
order by i
)
select t.i, coalesce(ct, 0) from generate_series('01-jan-2006'::date, '01-jan-2007'::date, '1 month') as t(i)
left join cte on t.i = cte.i;


-- alternative solution
with dates as (
select date, to_char(date, 'mm/dd/yy') as fmt_date from generate_series('2005-01-01'::date, '2008-01-01'::date, '1 month') as g(date)
)
select distinct date, dates.fmt_date, count(hiredate) over (partition by to_char(hiredate, 'yyyy-mm')) as ct
from dates left join emp on to_char(dates.date, 'yyyy-mm') = to_char(hiredate, 'yyyy-mm')
order by dates.date;
