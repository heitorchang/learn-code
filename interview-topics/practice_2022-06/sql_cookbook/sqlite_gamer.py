import os
import sqlite3
from datetime import datetime

DB_DIR = "c:/Users/heitor/code/tmp/sqlite3dbs/"

os.chdir(DB_DIR)

def gen_filename():
    return f"db_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.sq3"


def init_db():
    conn = sqlite3.connect(gen_filename())

    conn.execute("""
    create table gamer (
      gamer_id integer primary key,
      name text
    );
    """)

    conn.execute("""
    create table genre (
      genre_id integer primary key,
      name text
    );
    """)

    conn.execute("""
    create table game (
      game_id integer primary key,
      genre_id integer references genre,
      name text
    );
    """)

    conn.execute("""
    create table session (
      session_id integer primary key,
      player_one integer references gamer(gamer_id),
      player_two integer references gamer(gamer_id),
      game_id integer references game,
      hours_played integer
    );
    """)

    conn.execute("""
    insert into gamer (gamer_id, name) values
    (1, 'mike'),
    (2, 'heitor'),
    (3, 'tina'),
    (4, 'george');
    """)

    conn.execute("""
    insert into genre (genre_id, name) values
    (1, 'action'),
    (2, 'fighting'),
    (3, 'rpg');
    """)

    conn.execute("""
    insert into game (game_id, genre_id, name) values
    (1, 1, 'Contra'),
    (2, 1, 'Mario'),
    (3, 2, 'SFII'),
    (4, 2, 'SoulCalibur'),
    (5, 2, 'World Heroes'),
    (6, 3, 'FF6'),
    (7, 3, 'Lufia'),
    (8, 3, 'Pokemon');
    """)

    conn.execute("""
    insert into session (session_id, player_one, player_two, game_id, hours_played) values
    (1, 1, 2, 3, 3),
    (2, 1, 3, 1, 2),
    (3, 3, null, 6, 18),
    (4, 4, 2, 4, 9),
    (5, 1, 3, 3, 2),
    (6, 2, 3, 3, 5);

    """)

    return conn


def query_db(conn, query):
    cursor = conn.execute(query)
    for row in cursor:
        print(row)

    sample_queries = """
c = init_db()

query_db(c, "select sum(hours_played) from session s join gamer g on player_one = g.gamer_id or player_two = g.gamer_id where g.name = 'heitor'; ")

query_db(c, "select g.name, sum(hours_played) from game g left join session s using(game_id) group by g.name")

    """
