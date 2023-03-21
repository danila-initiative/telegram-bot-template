import os
import sqlite3 as sql


PATH_TO_DB = '/app/data/sqlite.db'
PATH_TO_MIGRATIONS = '/app/code/storage/migrations'


def migrate():
    if not os.path.exists(PATH_TO_DB):
        open(PATH_TO_DB, 'w').close()

    conn = sql.connect(PATH_TO_DB)
    cursor = conn.cursor()
    files = os.listdir(PATH_TO_MIGRATIONS)
    files.sort()
    for file in files:
        with open(PATH_TO_MIGRATIONS + '/' + file, 'r') as f:
            cursor.executescript(f.read())
    conn.commit()
    conn.close()


if __name__ == '__main__':
    migrate()
