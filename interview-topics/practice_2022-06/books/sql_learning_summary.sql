create table employee (
  emp_id serial primary key,
  fname text,
  lname text
);


insert into employee (fname, lname) values
('tina', 'branford');


create table character (
  char_id serial primary key,
  name text,
  age text
);

alter table character add column sex text;

insert into character (name, age) values ('tina', 19);

update character set sex = 'f' where char_id = 1;

create table magic (
  magic_id serial primary key,
  color text,
  name text,
  cost integer
);

insert into magic (color, name, cost) values
('black', 'fire', 4),
('black', 'fira', 15),
('black', 'firaga', 32),
('white', 'cure', 5),
('white', 'cura', 18),
('white', 'curaga', 40),
('white', 'life2', 40),
('gray', 'stop', 8);


select case
         when color = 'black' then '*'
         when color = 'white' then 'o'
         else '#'
       end as symbol,
       name, cost
from magic
order by color, cost;


with cte as (
  select color, name, cost, dense_rank() over (partition by color order by cost desc) as rnk from magic
)
select * from cte
where rnk = 1
order by color, name;


select name, case
  when cost < 10 then 'cheap'
  when cost < 30 then 'medium'
  else 'expensive'
  end as cost
from magic;


select exists(select 1 from magic where name = 'life');
select exists(select 1 from magic where name = 'life2');

select m.name, case
  when exists(select 1 from magic msub where m.cost = 5) then 'is a 5 MP spell'
  else 'is not a 5 MP spell'
  end as has_5_mp
from magic m;

select length('ultima');

select position('a' in 'ultima');
select position('q' in 'ultima'); -- returns 0

-- concatenate
select name || ' is ' || case when sex = 'f' then 'a girl.'
                              when sex = 'm' then 'a guy.' end
from character;


select 'a' < 'b';

select substr('illumina', 1, 3);
select substr('illumina', 5, 3);
select substr('illumina', 5);

select replace('kid wants potion for kid please', 'kid', 'gau');

select '2022-01-15'::date;
select to_char('2022-01-15'::date, 'dd-mon-yyyy');

select '2022-01-15'::date + 1;
select '2022-01-15'::date + interval '1 month';
select extract(year from '2022-01-15'::date); -- day of week, sunday is 0
select extract(month from '2022-01-15'::date); -- day of week, sunday is 0
select extract(day from '2022-01-15'::date); -- day of week, sunday is 0
select extract(dow from '2022-01-15'::date); -- day of week, sunday is 0

select '2022-01-15'::date - '2022-01-19'::date;
