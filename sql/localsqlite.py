import os
import sqlite3
from datetime import datetime

os.chdir("c:/users/erik/tmp/sqlite3_dbs")

def generate_filename():
    return f"localsqlite_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.sq3"


def test_using():
    conn = sqlite3.connect(generate_filename())
    conn.execute("create table user (user_id int primary key, name char(30));")
    conn.execute("create table post (user_id int, post char(30));")
    conn.execute("insert into user (user_id, name) values (1, 'joe');")
    conn.execute("insert into post (user_id, post) values (1, 'i am joe');")
    cur = conn.execute("select p.post, u.name from post p join user u using(user_id)")
    for row in cur:
        print(row)
