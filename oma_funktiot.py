#Eetu Kaivola

# -*- coding: utf-8 -*-
import mysql.connector
#opens connection to database...
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
    )
known_moves=['go', 'move', 'exit', 'walk', 'travel', 'climb', 'crawl', 'run']
known_opens=['open', 'close']
known_looks=['look', 'inspect', 'examine', 'search', 'investigate']
known_takes=['take', 'lift', 'pick', 'get', 'grab']
known_talks=['talk', 'ask', 'interrogate', 'interview', 'speak', 'tell']
known_helps=['inventory', 'help', 'map']
known_commands= []
known_commands.extend(known_moves)
known_commands.extend(known_talks)
known_commands.extend(known_takes)
known_commands.extend(known_helps)
known_commands.extend(known_opens)
known_commands.extend(known_looks)
known_rooms=['guestroom', 'garage', 'corridor', 'maidroom', 'office', 'kitchen', 'stairs', 'ballroom',
                'bathroom', 'bedroom', 'study', 'attic']
known_people =['butler', 'jeeves', 'willy', 'groundskeeper', 'maid', 'penelope', 'chef', 'gordon', 'lady', 'sonya']
known_objects =['table']
known_items =['whiskey']

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
        rperson = rows[0]
        return_person = str(rperson + " is in the room.\n")

    else:
        return_person = "There's no one beside you in the room.\n"

    return return_person


def conversation(db, suspect):
    cursor=db.cursor()
    cursor.execute("select npc.trust from npc where npc.location in (select location from player)")
    trust = cursor.fetchone()[0]

    if trust == 1 :
        if suspect == 'willy' or suspect == 'groundskeeper' and trust == 1:
            answer = str("\"There are weird things going on in this mansion. If I hadn't been working here all my life\n"
                   "and my father before me and his father before him, I would have quit a long time ago. \n"
                   "I am feeling a bit thirsty, you don't happen to have any liquid of gods?\"\n")

            return answer
    elif trust == 2 :
        if suspect == 'willy' or suspect == 'groundskeeper' and trust ==2:
            answer = str("\" I saw her, miss Penelope. She did some weird things! *hiccup* I went to war\n "
                     "and I never saw anything like that.  \"")
            return answer


