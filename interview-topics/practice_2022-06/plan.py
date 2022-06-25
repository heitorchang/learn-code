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

### join

# left join

# right join

# outer join

# cross join

# json_object_agg

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

### DATA STRUCTURES
# linked list
# mention collections.deque
# keep that Lisp muscle on the down low

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next_node


### TODO reverse, add, remove methods


# binary search
# PythonDS 6.4

def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# merge sort


# quicksort


# adjacency list


# BFS


# DFS


# Priority Queue
