#Eetu Kaivola
#testataan gittiä
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
                   "I am feeling a bit thirsty, you don't happen to have any water of life?\"\n")

            return answer
        elif suspect == 'chef' or suspect == 'gordon' and trust == 1:
            answer = str("Chef angily stops what he is doing and turns to you. \"What do you want?\n"
                         "My job is to cook food and not to answer questions! Go away, I am trying to work!"
                         "Go talk to Willy, if there is something to know he knows.\"\n")
            return answer
        elif suspect == 'maid' or suspect == 'penelope' and trust == 1:
            answer = str("\"What a horrible thing to happen! I think I must find a new job... \nI guess this"
                         " wasn't a success for me.\" ")
            return answer
        elif suspect == 'butler' or suspect == 'jeeves' and trust == 1:
            answer = str("\"Oh how horrible act of violence this is! My dear master and friend is gone!\n"
                         "Terrible night, I slept like a log after catering your marvelous party. What a "
                         "shame.\nI hope that police arrives shortly and we can put the monster behind bars!\"\n")
            return answer
        elif suspect == 'lady' or suspect == 'sonya' and trust == 1:
            answer = str("\"Bohoo! My love is gone! Go away you idiot! Can't you see that I am in grief."
                         "I have nothing to say to you. Leave me alone! \"")
            return answer

    elif trust == 2 :
        if suspect == 'willy' or suspect == 'groundskeeper' and trust ==2:
            answer = str("\" I heard her, miss Penelope. In the attic. She did some weird things! *hiccup* I went to war\n "
                     "and I never heard anything as scary like that.  \"")
            return answer



def location(room):
    if room == 'guestroom':
        return str("\nYou are in the mansion's guest bedroom.\nThe walls are painted light yellow and there is a "
                   "painting of a man with a firm look on his face. \nThe bed you slept in is not made and "
                   "there is an empty champagne glass on the night table. \nYou get the chills from this room "
                   "now even though it did not seem to matter last night.\n")
    if room == 'garage':
        return str("You enter the groundskeepers garage.\n"
                   "The door barely opens enough for you to slip in. There's boxes behind the door that havent been "
                   "touched \n"
                   "in ages. Rakes, shovels and picks fill the walls and a moist air mixed with the scent of wood "
                   "fills \n"
                   "your lugns. At the end of the room theres a small lamp that glances yellowy light across the "
                   "room and a workdesk.\n")
    if room == 'corridor':
        return str("You look across a long corridor.\n"
                   "The patterns on wallpapers run through the corridor. Few seemingly old maple wood sideboards with \n"
                   "golden finishing and red silken veils on the walls resemble just how wealthy the residents living\n"
                   "here are. There's paintings of noble men lined up on the walls and you feel a quiet breeze coming\n"
                   "from the window.\n")
    if room == 'maidroom':
        return str("insert maids chamber description here:")
    if room == 'office':
        return str("\nYou enter the office.\nThere's a nice view from the windows, a large wooden desk and an executive sized "
                   "leather chair behind it and two not-so-comfortable\nlooking chairs in front of the desk. "
                   "Wouldn't want to work here, you think. The desk is neatly\norganized: pencil holder, phone, "
                   "calendar, phone book. Nothing out of the ordinary on your first glance.\n ")
    if room == 'kitchen':
        return str("\nYou walk into the kitchen.\nFirst thing that you notice is that the chef has to be a superior "
                   "being. The kitchen is straight from the 18th century.\nWell, at least there is enough room "
                   "for a fridge, liquor cabinet, baking oven and shelves for pans,\npots and other cutlery. The Chef "
                   "himself is leaning over the sink apparently working on lunch. He is not easily distracted "
                   "you think.\nNo sign of him noticing you are in the room.\n")
    if room == 'stairs':
        return str("\nYou arrive at the stairs.\nThank god they are wide you think remembering last nights fumbles "
                   "downstairs. Otherwise it is just a staircase. Nothing of interest in here.\nJust go up or down.\n")
    if room == 'ballroom':
        return str("You are in the ballroom.\nNot so stylish in bright daylight you think. Scarlet drapes are faded "
                   "from sunlight and the long table just looks sad and old.\nEspecially now when last nights dinner "
                   "is only partially cleaned up. Food and drinks are gone but there are still\nplates and glasses. "
                   "The large dancing area is empty. A few chairs are located next to the walls. In daylight this looks "
                   "like a not so welcoming place to spend time.\n")
    if room == 'bathroom':
        return str("You are in the bathroom. \n"
                   "Apart from the usual toilet seat, mirror cabinet, ceramic sink, and a couple of towels hanging on the wall,\n"
                   "you notice hardly anything worth your attention. \n"
                   "There is however, a surprisingly large amount of shaving scum splattered around the sink.\n"
                   "Well, maybe somebody was busy with something more important than cleaning last night.\n")
    if room == 'master bedroom':
        return str("You are in the Mansion's master bedroom.\n"
                   "The late Lord's corpse is still lying on the bed. Hair white, eyes wide open, and arms stiffly grasping the air.\n"
                   "What could've caused a man such and eerie ending? You feel a sense of duty that beckons you to get to the bottom of this!\n")
    if room == 'study':
        return str("You are in Lord Chadwick's personal study.\n"
                   "There's a desk neatly organized by the window, a comfortable chair positioned under a reading lamp on one corner,\n"
                   "and a giant bookshelf filled with volumes gracing the wall.\n"
                   "You smell the dank cigarette smoke of countless hours spent among the books here.\n")
    if room == 'attic':
        return str("You are in the attic of the Mansion.\n"
                   "The atmosphere is very musty, and you can see many cobwebs hanging from the beams supporting the roof.\n"
                   "The light is dim, but you can make out heeps of cardboard boxes along the walls.\n"
                   "A little light from a small window on the western end of the room reveals a small table with a chair.\n")


def check_command (db, cmd):
    cursor = db.cursor()
    send = "select nimi from Synocmd where Synonyymi = '" + str(cmd) + "'"
    cursor.execute(send)
    results = cursor.fetchone()
    if results is not None:
        result = results[0]
    else:
        result = "dance"
    return result


def look(db, object):
    cursor=db.cursor()
    cursor.execute("select location from player")
    room = cursor.fetchone()[0]
    if room == 6 and object == 'cabinet':
        return str("There is only a single bottle of whiskey left in the cabinet.\n")
    elif room == 12 and object == 'table':
        return str("There is a strange and very old looking book on the table.\n")
    elif room == 12 and object == 'book':
        return str("The book is open at a section written in a strange looking language unknown to you.\n"
                   "The words 'NULLI INCANTA DEMONOS' in big letters at the bottom of the page strike your attention.\n")
    elif room == 10 and object == 'corpse':
        return str("The corpse lies on the bed totally rigid. You notice no signs of violence.\n"
                  "The expression on his face gives the impression of one scared to death.\n")
    else:
        return str("You notice nothing of particular interest.")
#pitäisi toimia kunnolla

def take(db, object):
    cursor=db.cursor()
    cursor.execute("select location from player")
    room = cursor.fetchone()[0]
    if room == 6 and object == 'whiskey':
        cursor.execute("update item set location = 13 where itemid = 1")
        return str("You pick up the bottle of whiskey and think, \"That will loosen up my suspects a bit..\"")
    elif room == 4 and object == 'page':
        cursor.execute("update item set location = 13 where itemid = 2")
        return str("You pick up torn page from the floor. \"I wonder what this is?\"")
    elif room == 12 and object == 'spellbook':
        cursor.exevute("update item set location = 13 where itemid = 5")
        return str("You pick up the spellbook and notice that a page is missing. \" Hmmm there are pages missing..\n")

def inventory(db):
    cursor=db.cursor()
    cursor.execute("select item.description from item where item.location = 13")
    inv=cursor.fetchall()
    return inv

