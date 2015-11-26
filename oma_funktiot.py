#Eetu Kaivola

# -*- coding: utf-8 -*-
import mysql.connector

#opens connection to database
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
    )

#where you are

def location(db):
    #db.cursor()
    db.cursor.execute("select location from roomID where id=1");
    return (db.cursor.fetchone())[0]