# %%
import sqlite3
from .setting import DATABASE_PATH, TABLE_NAME

# %%
class Database:
    def __init__(self):
        # Create or read the database file
        self.conn = sqlite3.connect(DATABASE_PATH)
        # Init table if not exist in database
        self.create_table()

    def create_table(self):
        CREATE_STATEMENT = f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        year integer NOT NULL,
        times integer NOT NULL,
        N1 integer NOT NULL,
        N2 integer NOT NULL,
        N3 integer NOT NULL,
        N4 integer NOT NULL,
        N5 integer NOT NULL,
        N6 integer NOT NULL,
        S1 integer NOT NULL,
        PRIMARY KEY(year,times))
        '''
        c = self.conn.cursor()
        c.execute(CREATE_STATEMENT)
        self.conn.commit()

    def close(self):
        self.conn.close()

    
