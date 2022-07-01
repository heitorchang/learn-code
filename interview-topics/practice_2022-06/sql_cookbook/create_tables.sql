create table dept (
deptno integer primary key,
dname text,
loc text
);

create table emp (
empno integer primary key,
ename text,
job text,
mgr integer,
hiredate date,
sal integer,
comm integer,
deptno integer references dept
);
