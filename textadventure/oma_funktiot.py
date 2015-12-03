#Eetu Kaivola
#testataan branchia
#testataan gittiä
# -*- coding: utf-8 -*-
import mysql.connector
#opens connection to database...
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
    )
#moves Sql:ssa
known_moves=['go', 'move', 'exit', 'walk', 'travel', 'climb', 'crawl', 'run']
#known looks sql:Ssa
known_looks=['look', 'inspect', 'examine', 'search', 'investigate']
#known takes sql:ssa
known_takes=['take', 'lift', 'pick', 'get', 'grab']
#talks sql:ssa
known_talks=['talk', 'ask', 'interrogate', 'interview', 'speak', 'tell']
known_opens=['open', 'close']
known_helps=['inventory', 'help', 'map', 'info']
known_commands= []
known_commands.extend(known_moves)
known_commands.extend(known_talks)
known_commands.extend(known_takes)
known_commands.extend(known_helps)
known_commands.extend(known_opens)
known_commands.extend(known_looks)

known_rooms=['guestroom', 'garage', 'corridor', 'maidroom', 'office', 'kitchen', 'stairs', 'ballroom',
                'bathroom', 'bedroom', 'study', 'attic']
#people sql:s
known_people =['butler', 'willy', 'maid', 'chef', 'lady']
known_objects =['table', 'cabinet', 'book', 'spellbook', 'corpse', 'lord', 'chadwick']
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

    #Tarkistaa nimen synonyymit ja vaihtaa oikean nimen
    send = "select npc.npcid, npc.trust from SynoPerson, npc where synoperson.Synonyymi = '" + suspect + "' and Synoperson.personID = npc.npcid"
    cursor.execute(send)
    person = cursor.fetchone()

    if person is not None:
        personid = person[0]
        trust = person[1]

    if trust == 1:
        #WILLY
        if personid == 1:
            answer = str("\"There are weird things going on in this mansion. If I hadn't been working here all my life\n"
                   "and my father before me and his father before him, I would have quit a long time ago. \n"
                   "I am feeling a bit thirsty, you don't happen to have any water of life?\"\n")

            return answer
        #CHEF
        elif personid == 3:
            answer = str("Chef angrily stops what he is doing and turns to you. \"What do you want?\n"
                         "My job is to cook food and not to answer questions! Go away, I am trying to work!"
                         "Go talk to Willy, if there is something to know he knows.\"\n")
            return answer
        #MAID
        elif personid == 2:
            answer = str("\"What a horrible thing to happen! I think I must find a new job... \nI guess this"
                         " wasn't a success for me.\" ")
            return answer
        #BUTLER
        elif personid == 4:
            answer = str("\"Oh how horrible act of violence this is! My dear master and friend is gone!\n"
                         "Terrible night, I slept like a log after catering your marvelous party. What a "
                         "shame.\nI hope that police arrives shortly and we can put the monster behind bars!\"\n")
            return answer
        #SONYA
        elif personid == 5:
            answer = str("\"Bohoo! My love is gone! Go away you idiot! Can't you see that I am in grief."
                         "I have nothing to say to you. Leave me alone! \"")
            return answer

    elif trust == 2 :
        if personid == 1:
            answer = str("\" I heard her, miss Penelope. In the attic. She did some weird things! *hiccup* I went to war\n "
                     "and I never heard anything as scary as that.  \"")
            return answer



def location(room):
    if room == 'guestroom':
        return str("\nYou are in the mansion's guest bedroom.\nThe walls are painted light yellow and there is a "
                   "painting of a man with a firm look on his face.\nThe bed you slept in is not made and "
                   "there is an empty champagne glass on the night table.\nYou get the chills from this room "
                   "now even though it did not seem to matter last night.\n"
                   "There is a single door leading to the corridor.\n")
    if room == 'garage':
        return str("You enter the groundskeeper's garage.\n"
                   "The door barely opens enough for you to slip in.\nThere are boxes behind the door that haven't been "
                   "touched in ages.\nRakes, shovels and picks fill the walls and a moist air mixed with the scent of wood "
                   "fills your lugns.\nAt the end of the room there's a small lamp that glances yellowy light across the "
                   "room and a workdesk.\nThe only door in the room leads back to the corridor.\n")
    if room == 'corridor':
        return str("You look across a long corridor.\n"
                   "The patterns on the wallpaper run through the corridor.\nFew seemingly old maple wood sideboards with "
                   "golden finishing and red silken veils on the walls resemble just how wealthy the residents are.\n"
                   "There are paintings of noble men lined up on the walls and you feel a quiet breeze coming from the window.\n"
                   "The corridor's five doors lead to the guestroom, maidroom, the kitchen, office, and the garage.\n"
                   "At the end of the corridor ascend the stairs leading to the second floor ballroom.\n")
    if room == 'maidroom':
        return str("You enter the Maid's Chamber.\n"
                   "The ascetic furnishing and lack of ornaments give an impression of efficiency.\n"
                   "The bed though seems to have been made in a hurry. The pillow for instance is halfway exposed.\n"
                   "The only door out of the room leads back to the corridor.\n")
    if room == 'office':
        return str("\nYou enter the office.\nThere's a nice view from the windows, a large wooden desk and an executive sized "
                   "leather chair behind it and two not-so-comfortable\nlooking chairs in front of the desk. "
                   "Wouldn't want to work here, you think. The desk is neatly\norganized: pencil holder, phone, "
                   "calendar, phone book. Nothing out of the ordinary on your first glance.\n"
                   "The corridor is the only way out of the room.\n")
    if room == 'kitchen':
        return str("\nYou walk into the kitchen.\nFirst thing that you notice is that the chef has to be a superior "
                   "being. The kitchen is straight from the 18th century.\nWell, at least there is enough room "
                   "for a fridge, liquor cabinet, baking oven and shelves for pans,\npots and other cutlery. The Chef "
                   "himself is leaning over the sink apparently working on lunch. He is not easily distracted "
                   "you think.\nNo sign of him noticing you are in the room.\n"
                   "The door leading back to the corridor is the only way out of the room.\n")
    if room == 'stairs':
        return str("\nYou arrive at the stairs.\n'Thank god they are wide' you think remembering last night's fumbles "
                   "downstairs.\nOtherwise it is just a staircase. Nothing of interest in here.\n"
                   "Just go up to the ballroom or down to the 1st floor corridor.\n")
    if room == 'ballroom':
        return str("You are in the ballroom.\nNot so stylish in bright daylight you think. Scarlet drapes are faded "
                   "from sunlight and the long table just looks sad and old.\nEspecially now when last night's dinner "
                   "is only partially cleaned up.\nFood and drinks are gone but there are still plates and glasses on the table.\n"
                   "The large dancing area is empty. A few chairs are located next to the walls. In daylight this looks "
                   "like a not so welcoming place to spend time.\n"
                   "From the ballroom open doors to the Master bedroom, the study, and the Lord's bathroom.\n"
                   "The stairs leading to the 1st floor corridor descend from the corner.\n")
    if room == 'bathroom':
        return str("You are in Lord Chadwick personal bathroom.\n"
                   "Apart from the usual toilet seat, mirror cabinet, ceramic sink, and a couple of towels hanging on the wall,\n"
                   "you notice hardly anything worth your attention.\n"
                   "There is however, a surprisingly large amount of shaving scum splattered around the sink.\n"
                   "Well, maybe somebody was busy with something more important than cleaning last night.\n"
                   "There are doors leading to the ballroom and the study.\n")
    if room == 'master bedroom':
        return str("You are in the Mansion's Master bedroom.\n"
                   "The late Lord's corpse is still lying on the bed. Hair white, eyes wide open, and arms stiffly grasping the air.\n"
                   "What could've caused a man such and eerie ending?\n"
                   "Looking at the remains of your late friend you feel a sense of duty that beckons you to get to the bottom of this!\n"
                   "From the bedroom it is possibly to enter the study or ballroom.\n")
    if room == 'study':
        return str("You are in Lord Chadwick's study.\n"
                   "There's a desk neatly organized by the window, a comfortable chair positioned under a reading lamp on one corner,\n"
                   "and a giant bookshelf filled with volumes gracing the wall.\n"
                   "You smell the dank cigarette smoke of countless hours spent among the books here.\n"
                   "There are 3 doors leading to the bathroom, the bedroom, and to the ballroom.\n")
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
#look-funktio tilpehööreineen
#item kuvauksia:
pagedesc = str("The page is from a book written in a strange language unknown to you.\n"
                       "There is a crude illustration of what looks like a whirlpool spinning above a crowd of robe-clad men.\n")
whiskdesc = str("Eetu kirjottaa tähän hienon viskikuvauksen\n")
bookdesc = str("The book, written in a strange language unknown to you, seems to have been mostly open at a same certain section.\n"
                   "The words 'NULLI INCANTA DEMONOS' in big letters at the end of this section strike your attention.\n")
#itse funktio
def look(db, object):
    cursor=db.cursor()
    cursor.execute("select location from player")
    room = cursor.fetchone()[0]

    if room is not None and object in ('around', 'room'):
        room = (room_desc(db))
        return location(room)

    elif room == 6 and object == 'cabinet':
        cursor.execute("select location from item where item.location=6")
        item = cursor.fetchone()
        if item is not None:
            return str("There is only a single bottle of whiskey left in the cabinet.\n")
        else:
            return str("The liquor cabinet is now empty.\n")

    elif room == 6 and object == 'whiskey':
        cursor.execute("select location from item where item.location=6")
        item = cursor.fetchone()
        if item is not None:
            return whiskdesc
        else:
            return whiskdesc

    elif room == 12 and object == 'table':
        cursor.execute("select location from item where item.location=12")
        item = cursor.fetchone()
        if item is not None:
            return str("There is a strange and very old looking book on the table.\n")
        else:
            return str("The table is just a table. A few candle stubs on it, nothing more.\n")
    elif room == 12 and object == 'book':
        return bookdesc

    elif room == 10 and object == 'lord':
        return str("The corpse lies on the bed totally rigid. You notice no signs of violence.\n"
                   "The expression on his face gives the impression of one scared to death.\n")

    elif room == 4 and object == 'bed':
        cursor.execute("select location from item where item.location=4")
        item = cursor.fetchone()
        if item is not None:
            return str("You notice a crumbled piece of paper stashed obviously in a hurry under the pillow.\n"
                   "It looks like a page torn from a book.\n")
        else:
            return str("The bed is just as it seems.")
    elif room == 4 and object == 'page':
        cursor.execute("select location from item where item.location=4")
        item = cursor.fetchone()
        if item is not None:
            return str("The paper has been crumbled and stashed under the pillow.\n"
                       "It's impossible to make out any of it's content from this angle.\n")
        else:
            return pagedesc
    elif room == 11 and object == 'bookshelf':
        return str("Examining the bookshelf closer you notice that a book is missing.\n"
                   "Judging by the dust marks it appears to have been removed quite recently.\n")

#inventaariossa olevien tavaroiden tutkimiseen:
    elif room is not None and object in ('page', 'paper'):
        cursor.execute("select itemID from item where location=13")
        item = cursor.fetchall()
        if (2,) in item:
            return pagedesc
        else:
            return str("You notice no such thing.")

    elif room is not None and object == 'whiskey':
        cursor.execute("select itemID from item where location=13")
        item = cursor.fetchall()
        if (1,) in item:
            return whiskdesc
        else:
            return str("You notice no such thing.")

    elif room is not None and object == 'book':
        cursor.execute("select itemID from item where location=13")
        item = cursor.fetchall()
        if (5,) in item:
            return bookdesc
        else:
            return str("No interesting books around here.\n")
#ja vielä koko p****n lopullinen else
    else:
        return str("You notice nothing of particular interest.")
#pitäisi toimia kunnolla


#Tarkistaa synonyymit ja palauttaa joko löydetyn synonyymin oikean sanan tai vaihtoehtoisesti palauttaa annetun
#syotteen takaisin. huoneiden osalta palauttaa vain sanan "room".
def check_noun (db, noun):
    cursor = db.cursor()
    send = "select nimi from Synocmd where Synonyymi = '" + noun + "'"
    cursor.execute(send)
    results = cursor.fetchone()
    if results is not None:
        result =results[0]
        return result
    else:
        return noun

def take(db, object):
    cursor=db.cursor()
    cursor.execute("select player.location, item.location from player, item where player.location = item.location")
    rooms = cursor.fetchone()
    if rooms is not None:
        playerroom = rooms[0]
        itemroom = rooms[1]

        if playerroom == 6 and itemroom == 6 and object == 'whiskey':
            cursor.execute("update item set location = 13 where itemid = 1")
            return str("You pick up the bottle of whiskey and think, \"That will loosen up my suspects a bit..\"")

        elif playerroom == 4 and itemroom == 4 and object == 'page':
            cursor.execute("update item set location = 13 where itemid = 2")
            return str("You pick up and unfold the torn page. \"I wonder what this is?\"")

        elif playerroom == 12 and itemroom == 12 and object == 'book':
            cursor.exevute("update item set location = 13 where itemid = 5")
            return str("You pick up the spellbook and notice that a page is missing. \" Hmmm there are pages missing..\n")
    else:
        return str("There seems to be no such object nearby.")

def inventory(db):
    cursor=db.cursor()
    cursor.execute("select item.description from item where item.location = 13")
    inv=cursor.fetchall()
    return inv

def info(db):
    cursor=db.cursor()
    cursor.execute("select player.location, item.description, npc.description, room.description from player left outer join item on (item.location = player.location) left outer join npc on (npc.location = player.location) left outer join room on (room.roomid = player.location)")
    infolist = cursor.fetchone()
    if infolist is not None:
        location = infolist[0]
        items = infolist[1]
        npc = infolist[2]
        roomdesc = infolist[3]
        info = "Location: " + str(location) + " - " + roomdesc + "\nitems: " + str(items) + "\nnpc:s " + str(npc)
        return info
    else:
        return str("info ei toimi")