#Eetu Kaivola

# -*- coding: utf-8 -*-
import mysql.connector
#opens connection to database...
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
    )
known_moves =   ['go', 'move', 'exit', 'walk', 'travel', 'climb', 'crawl', 'run']
known_opens =   ['open', 'close']
known_looks =   ['look', 'inspect', 'examine', 'search', 'investigate']
known_takes =   ['take', 'lift', 'pick', 'get', 'grab']
known_talks =   ['talk', 'ask', 'interrogate', 'interview', 'speak', 'tell']
known_helps =   ['inventory', 'help', 'map']
known_rooms =   ['guestroom', 'garage', 'corridor', 'maidroom', 'office', 'kitchen', 'stairs', 'ballroom',
                'bathroom', 'bedroom', 'study', 'attic']
known_people =  ['butler']
known_objects = ['table']
known_items =   ['whiskey']

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

    sql = "update player set location = " + str(roomID)

    cursor.execute(sql)


def people(db):
    cursor=db.cursor()
    cursor.execute("select description from npc where npc.location in (select location from player)")

    #hakee kaikki arvot ja sitten tarkistaa onko ketään huoneessa
    rows = cursor.fetchone()
    if rows is not None:
        return_person = rows[0]
    else:
        return_person = "There's no one beside you in the room"

    return return_person




