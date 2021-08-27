##Sqlite wrapper from https://gist.github.com/goldsborough/c973d934f620e16678bf
import sqlite3
import pandas as pd
import dearpygui.dearpygui as dpg

conn = sqlite3.connect('../my_data.db')
c = conn.cursor()


class Database:

    def __init__(self, name=None):

        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self, name):

        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")

    def get_table_rows(self, table) -> list:
        self.cursor.execute(f"select * from {table}")
        table_rows = self.cursor.fetchall()
        return table_rows

    def open_db(self,name):
        srdata = pd.read_csv('C:/Users/ebrown/Desktop/Temp SR/test.csv')
        srdata.to_sql(name, conn, if_exists='replace')
        #c.execute('SELECT * FROM test_table')

        print("table created")

    def create_table(self):
        c.execute('''CREATE TABLE IF NOT EXISTS stressrelief 
        (id REAL, 
        Size TEXT, 
        weight TEXT,
        Connection TEXT,
        heat TEXT,
        temperature INTEGER, 
        time INTEGER, 
        material TEXT)
         ''')
        print('Table created')

    def csv_reader(self,file_name):
        srdata = pd.read_csv('C:/Users/ebrown/Desktop/Temp SR/test.csv')
        srdata.to_sql('test_table', conn, if_exists='replace')
        c.execute('SELECT * FROM test_table')

        print("table created")

        for row in c.fetchall():
            return row

    def add_one(self,size,weight,connection,heatnumber,material, temperature,time):
        conn=sqlite3.connect('../my_data.db')
        c=conn.cursor()
        c.execute('SELECT * FROM stressrelief2')
        length=len(c.fetchall())+1
        c.execute("INSERT INTO stressrelief VALUES(?,?,?,?,?,?,?,?)",(length,size,weight,connection,heatnumber,material,temperature,time))
        conn.commit()
        conn.close()

#Look up OD and return items with OD
    def size_callback(a):
        c.execute("SELECT * FROM stressrelief WHERE Size=(?)",(a,))
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
            print('New data entered successfully')
        else:
            for item in items:
                print (item)

##need to pass in table name
    def size_lookup(self) -> list[str]:
        query = 'SELECT Size FROM stressrelief'
        c.execute(query)
        size = list[str]
        for column in c.fetchall():
            size.append(str(column[0]))
        size = list(set(size))
        return size

    def display_db():
        c.execute("SELECT * FROM stressrelief")
        for row in c.fetchall():
            print(row)


##Data retrieval
    def get_ult(self, od, heat) -> list:
        c.execute('SELECT ult stressrelief WHERE Size=? AND heatnumber =?',(od,heat))
        ult = list()
        for column in c.fetchall():
            ult.append(column[0])
        return ult

    def get_yld(self,od,heat) -> list:
        c.execute('SELECT yld stressrelief WHERE Size=? AND heatnumber =?',(od,heat))
        yld = list()
        for column in c.fetchall():
            yld.append(column[0])
        return yld

    def get_ceq(self, heat) ->list:
        c.execute('SELECT ult stressrelief WHERE heatnumber =?', (heat,))
        ceq = list()
        for column in c.fetchall():
            ceq.append(column[0])
        return ceq


    def _load_demo_db(self):
        table   = "Employees"
        columns = ["EmpCode      INTEGER",
                   "EmpFName     TEXT",
                   "EmpLName     TEXT",
                   "Job          TEXT",
                   "Manager      TEXT",
                   "HireDate     TEXT",
                   "Salary       INTEGER",
                   "Commission   INTEGER",
                   "DEPTCODE     INTEGER"]
        data    = [[9369, 'TONY', 'STARK', 'SOFTWARE_ENGINEER', 7902, '1980-12-17', 2800,0,20],
                   [9499, 'TIM', 'ADOLF', 'SALESMAN', 7698, '1981-02-20', 1600, 300,30],
                   [9566, 'KIM', 'JARVIS', 'MANAGER', 7839, '1981-04-02', 3570,0,20],
                   [9654, 'SAM', 'MILES', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30],
                   [9782, 'KEVIN', 'HILL', 'MANAGER', 7839, '1981-06-09', 2940,0,10],
                   [9788, 'CONNIE', 'SMITH', 'ANALYST', 7566, '1982-12-09', 3000,0,20],
                   [9839, 'ALFRED', 'KINSLEY', 'PRESIDENT', 7566, '1981-11-17', 5000,0, 10],
                   [9844, 'PAUL', 'TIMOTHY', 'SALESMAN', 7698, '1981-09-08', 1500,0,30],
                   [9876, 'JOHN', 'ASGHAR', 'SOFTWARE_ENGINEER', 7788, '1983-01-12',3100,0,20],
                   [9900, 'ROSE', 'SUMMERS', 'TECHNICAL LEAD', 7698, '1981-12-03', 2950,0, 20],
                   [9902, 'ANDREW', 'FAULKNER', 'ANAYLYST', 7566, '1981-12-03', 3000,0, 10],
                   [9934, 'KAREN', 'MATTHEWS', 'SOFTWARE_ENGINEER', 7782, '1982-01-23', 3300,0,20],
                   [9591, 'WENDY', 'SHAWN', 'SALESMAN', 7698, '1981-02-22', 500,0,30],
                   [9698, 'BELLA', 'SWAN', 'MANAGER', 7839, '1981-05-01', 3420, 0,30],
                   [9777, 'MADII', 'HIMBURY', 'ANALYST', 7839, '1981-05-01', 2000, 200, "NULL"],
                   [9860, 'ATHENA', 'WILSON', 'ANALYST', 7839, '1992-06-21', 7000, 100, 50],
                   [9861, 'JENNIFER', 'HUETTE', 'ANALYST', 7839, '1996-07-01', 5000, 100, 50]]
        self.db.create_table(table, columns)
        self.db.add_rows(table, data)
        table   = "Books"
        columns = ["BookName    TEXT",
                   "Category    TEXT",
                   "Price       REAL",
                   "Price_Range TEXT",
                   ]
        data    = [['Computer Architecture', 'Computers', 125.6, '100-150'],
                   ['Advanced Composite Materials', 'Science', 172.56, '150-200'],
                   ['Asp.Net 4 Blue Book', 'Programming', 56.00, '50-100'],
                   ['Strategies Unplugged', 'Science', 99.99, '50-100'],
                   ['Teaching Science', 'Science', 164.10, '150-200'],
                   ['Challenging Times', 'Business', 150.70, '150-200'],
                   ['Circuit Bending', 'Science', 112.00, '100-150'],
                   ['Popular Science', 'Science', 210.40, '200-250'],
                   ['ADOBE Premiere', 'Computers', 62.20, '50-100']
                   ]
        self.db.create_table(table, columns)
        self.db.add_rows(table, data)

        table   = "Birds"
        columns = ["ID INTEGER",
                   "BirdName TEXT",
                   "TypeOfBird TEXT",
                   "ScientificName TEXT"
                   ]
        data    = [[1,	'Eurasian Collared-Dove', 'Dove', 'Streptopelia'],
                   [2,	'Bald Eagle	Hawk', 'Haliaeetus', 'Leucocephalus'],
                   [3,	'Coopers Hawk',	'Hawk',	'Accipiter Cooperii'],
                   [4,	'Bells Sparrow', 'Sparrow', 'Artemisiospiza Belli'],
                   [5,	'Mourning Dove', 'Dove', 'Zenaida Macroura'],
                   [6,	'Rock Pigeon', 'Dove', 'Columba Livia'],
                   [7,	'Aberts Towhee', 'Sparrow', 'Melozone Aberti'],
                   [8,	'Brewers Sparrow', 'Sparrow', 'Spizella Breweri'],
                   [9,	'Canyon Towhee', 'Sparrow', 'Melozone Fusca'],
                   [10, 'Black Vulture', 'Hawk', 'Coragyps Atratus'],
                   [11, 'Gila Woodpecker', 'Woodpecker', 'Melanerpes Uropygialis'],
                   [12, 'Gilded Flicker', 'Woodpecker', 'Colaptes Chrysoides'],
                   [13, 'Cassins Sparrow', 'Sparrow', 'Peucaea Cassinii'],
                   [14, 'American Kestrel', 'Hawk', 'Falco Sparverius'],
                   [15, 'Hairy Woodpecker', 'Woodpecker', 'Picoides villosus'],
                   [16, 'Lewis Woodpecker', 'Woodpecker', 'Melanerpes Lewis'],
                   [17, 'Snail Kite', 'Hawk', 'Rostrhamus Sociabilis'],
                   [18, 'White-tailed Hawk', 'Hawk', 'Geranoaetus Albicaudatus']
                   ]
        self.db.create_table(table, columns)
        self.db.add_rows(table, data)







