-- see also: insert_rows_pivot.py

insert into dept
(deptno, dname,    loc) values
(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH',   'DALLAS'),
(30, 'SALES',      'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON');


insert into emp
(empno, ename,   job,          mgr, hiredate,      sal, comm, deptno)
values
(7369, 'SMITH',  'CLERK',     7902, '17-DEC-2005', 800,  NULL, 20),
(7499, 'ALLEN',  'SALESMAN',  7698, '20-FEB-2006', 1600, 300,  30),
(7521, 'WARD',   'SALESMAN',  7698, '22-FEB-2006', 1250, 500,  30),
(7566, 'JONES',  'MANAGER',   7839, '02-APR-2006', 2975, NULL, 20),
(7654, 'MARTIN', 'SALESMAN',  7698, '28-SEP-2006', 1250, 1400, 30),
(7698, 'BLAKE',  'MANAGER',   7839, '01-MAY-2006', 2850, NULL, 30),
(7782, 'CLARK',  'MANAGER',   7839, '09-JUN-2006', 2450, NULL, 10),
(7788, 'SCOTT',  'ANALYST',   7566, '09-DEC-2007', 3000, NULL, 20),
(7839, 'KING',   'PRESIDENT', NULL, '17-NOV-2006', 5000, NULL, 10),
(7844, 'TURNER', 'SALESMAN',  7698, '08-SEP-2006', 1500, 0,    30),
(7876, 'ADAMS',  'CLERK',     7788, '12-JAN-2008', 1100, NULL, 20),
(7900, 'JAMES',  'CLERK',     7698, '03-DEC-2006', 950,  NULL, 30),
(7902, 'FORD',   'ANALYST',   7566, '03-DEC-2006', 3000, NULL, 20),
(7934, 'MILLER', 'CLERK',     7782, '23-JAN-2007', 1300, NULL, 10);


insert into emp_bonus (empno, received, type) values
(7369, '14-MAR-2005', 1),
(7900, '14-MAR-2005', 2),
(7788, '14-MAR-2005', 3);


insert into emp_bonus_3_9 (empno, received, type) values
(7934, '17-MAR-2005', 1),
(7934, '15-FEB-2005', 2),
(7839, '15-FEB-2005', 3),
(7782, '15-FEB-2005', 1);


insert into emp_bonus_3_10 (empno, received, type) values
(7934, '17-MAR-2005', 1),
(7934, '15-FEB-2005', 2);


insert into emp
(empno, ename,   job,          mgr, hiredate,      sal, comm, deptno)
select 1111, 'YODA',  'JEDI',     null, '01-JAN-2001', sal,  comm, null from emp where ename = 'KING';
