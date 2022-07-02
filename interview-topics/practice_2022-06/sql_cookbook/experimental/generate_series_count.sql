with cte as (
select t.i, count(*) as ct from generate_series('01-jan-2006'::date, '01-jan-2007'::date, '1 month') as t(i), emp e
where e.hiredate >= i and e.hiredate < i + interval '1 month'
group by i
order by i
)
select t.i, coalesce(ct, 0) from generate_series('01-jan-2006'::date, '01-jan-2007'::date, '1 month') as t(i)
left join cte on t.i = cte.i;
