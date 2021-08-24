import sqlite3
import pandas as pd

conn = sqlite3.connect('my_data.db')
c = conn.cursor()
class Database:

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS stressrelief (id REAL, Size INTEGER, weight INTEGER,Connection TEXT,wee TEXT,temperature INTEGER, time INTEGER, material TEXT)
     ''')


def csv_reader(file_name):
    srdata = pd.read_csv(file_name)
    srdata.to_sql('stressrelief', conn, if_exists='replace')
    c.execute('SELECT * FROM stressrelief')

    for row in c.fetchall():
        print(row)

def add_one(size,weight,connection,heatnumber,material, temperature,time):
    conn=sqlite3.connect('my_data.db')
    c=conn.cursor()
    c.execute('SELECT * FROM stressrelief2')
    length=len(c.fetchall())+1
    c.execute("INSERT INTO stressrelief2 VALUES(?,?,?,?,?,?,?,?)",(length,size,weight,connection,heatnumber,material,temperature,time))
    conn.commit()
    conn.close()

#Look up OD and return items with OD
def size_lookup(a):
    c.execute("SELECT * FROM stressrelief2 WHERE Size=(?)",(a,))
    #c.execute("SELECT * FROM stressrelief WHERE Size=(?) AND weight=(?)",(a,b))
    items = c.fetchall()
    if len(items)==0:
        print('There is no OD in that size')
        b=input('Weight: ')
        h=input('Connection: ')
        d= input('Heat Number: ')
        e = input('Material: ')
        f =input('Temperature F: ')
        g= input('Time in seconds: ')
        add_one(a,b,h,d,e,f,g)
        print('New data inputed sucessfully')
    else:
        for item in items:
            print (item)

def display_db():
    c.execute("SELECT * FROM stressrelief2")
    for row in c.fetchall():
        print(row)

def graph_data():

conn.commit()
conn.close()





