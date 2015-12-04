import mysql.connector
import oma_funktiot

hostname = 'localhost'
uname = 'player'
pswd = 'mm'
db = oma_funktiot.open_database(hostname, uname, pswd)

cursor=db.cursor()
cursor.execute("select * from plot")
plot=cursor.fetchone()
print(plot)

while plot == (0, 0, 0, 0, 0):
    step=input("what now then?")
    if step == 'go':
        cursor.execute("update plot set state1=1")
        cursor.execute("select * from plot")
        plot=cursor.fetchone()
        print (plot)