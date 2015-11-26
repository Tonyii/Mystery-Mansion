#Eetu Kaivola

# -*- coding: utf-8 -*-
import mysql.connector

#opens connection to database
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
    )

#where you are

def room_desc(db):
    cursor=db.cursor()
    cursor.execute("select description from room "
                   "where roomID "
                   "in (select location from player)")
    return (cursor.fetchone())[0]

def move(db):
    cursor=db.cursor()
    cursor.execute("update player set location = 2")