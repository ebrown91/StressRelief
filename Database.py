import sqlite3
import pandas as pd

conn = sqlite3.connect('my_data.db')
c = conn.cursor()


def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS stressrelief (id REAL, Size INTEGER, weight INTEGER,Connection TEXT,wee TEXT,temperature INTEGER, time INTEGER, material TEXT)
     ''')


def csv_reader(file_name):
    srdata = pd.read_csv(file_name)
    srdata.to_sql('stressrelief', conn, if_exists='replace')
    c.execute('SELECT * FROM stressrelief')

    for row in c.fetchall():
        print(row)


def graph_data():

conn.commit()
conn.close()





