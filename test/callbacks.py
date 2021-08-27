##callback functions for GUI
from Database import *

def open_db_callback(sender, app_data, user_data):
    #user_data.open_db()

    Database.create_table
    Database.csv_reader


def open_connection_callback(sender, app_data, user_data):
    #user_data.loop_connection()
    user_data.loop_conn()


def close_connection_callback(sender, app_data, user_data):
    user_data.b_connected = False


def checkme(sender, data):
    input_value = data
    print("This is what you typed " + input_value)


def checkme2(sender, data):
    dpg.get_value(uni)
    input_value = 'SELECT * FROM test_table WHERE size = ? '
    c.execute(input_value, (data,))
    item = list()
    for items in c.fetchall():
        item.append(data[0])
    print(item)

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
        Database.add_one(a,b,h,d,e,f,g)
        print('New data entered successfully')
    else:
        for item in items:
            print (item)