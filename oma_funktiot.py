#Eetu Kaivola

# -*- coding: utf-8 -*-
import mysql.connector
#opens connection to database
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
    )
known_commands =['go', 'move', 'exit', 'walk', 'travel', 'climb', 'crawl', 'run',
                 'open', 'close',
                 'look', 'inspect', 'examine', 'search', 'investigate',
                 'take', 'lift', 'pick', 'get', 'grab',
                 'talk', 'ask', 'interrogate', 'interview', 'speak', 'tell',
                 'inventory', 'help', 'map']
known_rooms =['guestroom', 'Garage', 'Corridor', 'Maidroom', 'Office', 'Kitchen', 'Stairs', 'Ballroom',
              'Bathroom', 'bedroom', 'Study', 'Attic']

#where you are

def room_desc(db):
    cursor=db.cursor()
    cursor.execute("select description from room "
                   "where roomID "
                   "in (select location from player)")
    return (cursor.fetchone())[0]

def move(db, noun):
    roomID = known_rooms.index(noun)
    roomID = roomID +1
    cursor=db.cursor()
    cursor.execute("update player set location = "+ roomID )

def people(db):
    cursor=db.cursor()
    cursor.execute("select description from npc where npc.location in (select location from player)")
    return (cursor.fetchone())[0]





