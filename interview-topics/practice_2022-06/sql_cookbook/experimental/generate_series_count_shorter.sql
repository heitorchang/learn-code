with report_dates as (
select i from generate_series('01-jan-2006'::date, '01-jan-2007'::date, '1 month') as t(i)
), cte as (
select report_dates.i, count(*) as ct from report_dates, emp e
where e.hiredate >= i and e.hiredate < i + interval '1 month'
group by i
order by i
)
select r.i, coalesce(ct, 0) from report_dates r
left join cte on r.i = cte.i;
