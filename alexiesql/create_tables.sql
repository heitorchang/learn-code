-- Assets Liabilities EXpenses Income Equity

create table acct_type (
  acct_type_id serial primary key,
  name text,
  sign integer
);

create table acct (
  acct_id serial primary key,
  acct_type_id integer references acct_type,
  name text,
  budget money
);

create table txn (
  txn_id serial primary key,
  dr integer references acct(acct_id),
  cr integer references acct(acct_id),
  txn_date date,
  txn_desc text,
  txn_amt money
);

-- insert common data

insert into acct_type (name, sign) values
('assets', 1),       -- 1
('expenses', 1),     -- 2
('liabilities', -1), -- 3
('income', -1),      -- 4
('equity', -1);      -- 5

insert into acct (acct_type_id, name) values
(1, 'savings'),         --  1
(1, 'checking'),        --  2
(1, 'wallet'),          --  3
(2, 'groceries'),       --  4
(2, 'transportation'),  --  5
(2, 'fees'),            --  6
(3, 'credit card'),     --  7
(4, 'salary'),          --  8
(4, 'interest'),        --  9
(5, 'opening balance'); -- 10

-- template 'open'
insert into txn (dr, cr, txn_date, txn_desc, txn_amt) values
((select acct_id from acct where name = 'wallet'),
 (select acct_id from acct where name = 'opening balance'),
 current_date,
 'open',
 120.50);


-- template 'expense'
insert into txn (dr, cr, txn_date, txn_desc, txn_amt) values
((select acct_id from acct where name = 'groceries'),
 (select acct_id from acct where name = 'wallet'),
 current_date,
 'burger',
 26.90);
