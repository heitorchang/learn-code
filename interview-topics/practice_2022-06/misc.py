"""
topics off the top of my head that are important
"""

# FizzBuzz

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


# fibonacci

def fib_linrec(n):
    return fib_helper(n, 0, 1)


def fib_helper(rest, a, b):
    if rest == 0:
        return a
    return fib_helper(rest - 1, b, a + b)


def fib_for(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_treerec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_treerec(n - 1) + fib_treerec(n - 2)


# cached
from functools import lru_cache

@lru_cache
def fib_treerec_cached2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_treerec_cached2(n - 1) + fib_treerec_cached2(n - 2)


# calculate pi
# check code/learn-code/common-lisp/find-pi.lisp
# returns index 136120

# rationale for not using "while": avoid an infinite loop, be defensive
# if the range limit chosen was too small, increase it

def find_pi(desired_estimate):
    desired_estimate = str(desired_estimate)
    current_estimate = 0
    for i in range(300000):
        if i % 2 == 0:
            fraction = 4 / (2 * i + 1)
        else:
            fraction = -4 / (2 * i + 1)
        current_estimate += fraction

        # compare estimates
        if str(current_estimate)[:len(desired_estimate)] == desired_estimate:
            print(current_estimate, i)
            break
    else:
        # reached end, did not converge
        print(current_estimate, 'did not converge')


# Euclid's GCD algorithm

def euclid_gcd(lg, sm):
    if sm == 0:
        return lg
    return euclid_gcd(sm, lg % sm)


### SQL

# create: insert INTO
"""
insert into employees (id, name)
values (%s, %s);
"""

# read: select FROM
"""
select a.id, a.name, sum(t.amount) as credits
from account as a join txns as t
on t.credit = a.id
group by a.id;
"""

# update: update WHERE
"""
update person
set fname = 'John'
where person_id = 1;
"""

# delete: delete FROM ... WHERE
"""
delete from person
where person_id < 10;
"""

# case -> when CONDITION then VALUE else ALTERNATIVE

# cast: created::date
# cast('2022-06-20' as date)



### Table: create
"""
create table my_tbl (
  id integer primary key,
  name text
);
"""

# Common Table Expressions (CTE)
"""
with params as (
  select a, b, c from tbl
  cross join
), model_agg as (
  select a, b, c from params
)
select json_object_agg(b, val) as b_val
from model_agg;
"""

# Tricky queries (greatest n-per-group)
"""
select r.name, r.dept, r.salary
from (select e.*,
  dense_rank() over
  (partition by e.dept order by e.salary desc) as pos
  from employees e) as r
where r.pos <= 3
order by r.dept, r.salary desc;
"""


### PostgreSQL
# json_object_agg
