#Eetu Kaivola
#testataan branchia
#testataan gitti�
# -*- coding: utf-8 -*-
import mysql.connector

#opens connection to database...
def open_database(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="MM", buffered=True
   )


def help():

    ret = str("\nFor moving around there are following commands:\n") + str("'go', 'move', 'exit', 'walk', 'travel', 'climb', 'crawl', 'run'")
    ret = ret + str("\nIf you want to pick up an object you can:\n") + str("'look', 'inspect', 'examine', 'search', 'investigate'")
    ret = ret + str("\nFor character interaction:\n") + str("'take', 'lift', 'pick', 'get', 'grab'")
    ret = ret + str("\nTo examine things you have:\n") + str("'talk', 'ask', 'interrogate', 'interview', 'speak', 'tell'") + str("\n")
    return ret
#where you are
def room_desc(db):
    cursor=db.cursor()
    cursor.execute("select description from room "
                   "where roomID "
                   "in (select location from player)")
    return (cursor.fetchone())[0]

def move(db, noun):
    cursor=db.cursor()
    sql = "update player set location = (select roomid from room where description = '" + noun + "')"
    cursor.execute(sql)
    return


def people(db):
    cursor=db.cursor()
    cursor.execute("select description from npc where npc.location in (select location from player)")

    #hakee kaikki arvot ja sitten tarkistaa onko ket��n huoneessa
    rows = cursor.fetchone()
    if rows is not None:
        rperson = rows[0]
        return_person = str(rperson + " is in the room.")

    else:
        return_person = "There's no one beside you in the room."

    return return_person

def conversation(db, suspect):
    cursor=db.cursor()

    #jos pelaajalla kaikki vihjeet vaihdetaan maidille uusi trust
    cursor.execute("select * from plot")
    plotnow = cursor.fetchone()
    if plotnow == (1, 1, 1, 0, 0):
        cursor.execute("update npc set trust=2 where npcID=2")

    #Tarkistaa nimen synonyymit ja vaihtaa oikean nimen
    send = "select npc.npcid, npc.trust from synoPerson, npc, player where synoperson.synonyymi = '" + suspect + "' and player.location and synoperson.personid = npc.npcid and npc.location in (select location from player)"
    cursor.execute(send)
    person = cursor.fetchone()
    if person is None:
        print("There is no such character here to talk to.")


    if person is not None:
        personid = person[0]
        trust = person[1]



    if trust == 1:
        #WILLY
        if personid == 1:
            answer = str("\n\"There are weird things going on in this mansion. If I hadn't been working here all my life\n"
                   "and my father before me and his father before him, I would have quit a long time ago. \n"
                   "I am feeling a bit thirsty, you don't happen to have any water of life?\"\n")

            return answer
        #CHEF
        elif personid == 3:
            answer = str("\nChef angrily stops what he is doing and turns to you. \"What do you want?\n"
                         "My job is to cook food and not to answer questions! Go away, I am trying to work! "
                         "Go talk to Willy, if there is something to know he knows.\"\n")
            return answer
        #MAID
        elif personid == 2:
            answer = str("\n\"What a horrible thing to happen! I think I must find a new job... \nI guess this"
                         " wasn't a success for me.\" \n")
            return answer
        #BUTLER
        elif personid == 4:
            answer = str("\n\"Oh how horrible act of violence this is! My dear master and friend is gone!\n"
                         "Terrible night, I slept like a log after catering your marvelous party. What a "
                         "shame.\nI hope that police arrives shortly and we can put the monster behind bars!\"\n")
            return answer
        #SONYA
        elif personid == 5:
            answer = str("\n\"Bohoo! My love is gone! Go away you idiot! Can't you see that I am in grief. "
                         "I have nothing to say to you. Leave me alone! \"\n")
            return answer

    elif trust == 2 :
        if personid == 1:
            answer = str("\n\"I heard her, miss Penelope. In the attic. She did some weird things! *hiccup* I went to war\n"
                     "and I never heard anything as scary as that.\"\n")
            cursor.execute("update plot set state1=1")
            return answer

        if personid == 2:
            answer = str("As you try to confront Penelope she gives you an evil glance,\n"
                         "mumbles something under her breath, and vanishes suddenly in a puff of smoke!\n\n"
                         "################################################################################"
                         "\nGONGRATULATIONS! YOU HAVE SOLVED THE MURDER AND FINISHED THE GAME IN GRAPHICAL INTERFACE."
                         "TO SEE THE 'BOSSFIGHT', PLEASE USE THE TEXT VERSION!\n"
                         "################################################################################\n\n\n\n")
            cursor.execute("update plot set state4=1")
            return answer


def location(room):
    if room == 'guestroom':
        return str("\nYou are in the Mansion's guest bedroom.\nThe walls are painted light yellow and there is a "
                   "painting of a man with a firm look on his face.\nThe bed you slept in is not made and "
                   "there is an empty champagne glass on the night table.\nYou get the chills from this room "
                   "now even though it did not seem to matter last night.\n\n"
                   "There is a single door leading to the corridor.\n")
    if room == 'garage':
        return str("\nYou enter the groundskeeper's garage.\n"
                   "The door barely opens enough for you to slip in.\nThere are boxes behind the door that haven't been "
                   "touched in ages.\nRakes, shovels and picks fill the walls and a moist air mixed with the scent of wood "
                   "fills your lugns.\nAt the end of the room there's a small lamp that glances yellowy light across the "
                   "room and a workdesk.\n\nThe only door in the room leads back to the corridor.\n")
    if room == 'corridor':
        return str("\nYou look across a long corridor.\n"
                   "The patterns on the wallpaper run through the corridor.\nFew seemingly old maple wood sideboards with "
                   "golden finishing and red silken veils on the walls \nresemble just how wealthy the residents are. "
                   "There are paintings of noble men lined up on the walls \nand you feel a quiet breeze coming from the window."
                   "\n\nThe corridor's five doors lead to the guestroom, maidroom, the kitchen, office, and the garage."
                   "\nAt the end of the corridor ascend the stairs leading to the second floor ballroom. ")
    if room == 'maidroom':
        return str("\nYou enter the maid's chamber.\n"
                   "The ascetic furnishing and lack of ornaments give an impression of efficiency.\n"
                   "The bed though seems to have been made in a hurry. The pillow for instance is halfway exposed.\n\n"
                   "The only door out of the room leads back to the corridor.\n")
    if room == 'office':
        return str("\nYou enter the office.\nThere's a nice view from the windows, a large wooden desk and an executive sized "
                   "leather chair \nbehind it and two not-so-comfortable looking chairs in front of the desk. "
                   "Wouldn't \nwant to work here, you think. The desk is neatly organized: pencil holder, phone, "
                   "calendar, \nphone book. Nothing out of the ordinary on your first glance.\n\n"
                   "The corridor is the only way out of the room.\n")
    if room == 'kitchen':
        return str("\nYou walk into the kitchen.\nFirst thing that you notice is that the chef has to be a superior "
                   "being. The kitchen is straight \nfrom the 18th century. Well, at least there is enough room "
                   "for a fridge, liquor cabinet, \nbaking oven and shelves for pans, pots and other cutlery. The Chef "
                   "himself is leaning over the sink \napparently working on lunch. He is not easily distracted "
                   "you think.\nNo sign of him noticing you are in the room.\n\n"
                   "The door leading back to the corridor is the only way out of the room.\n")
    if room == 'stairs':
        return str("\nYou arrive at the stairs.\n\"Thank god they are wide\" you think remembering last night's fumbles "
                   "downstairs.\nOtherwise it is just a staircase. Nothing of interest in here.\n\n"
                   "Just go up to the ballroom or down to the 1st floor corridor.\n")
    if room == 'ballroom':
        return str("\nYou are in the ballroom.\nNot so stylish in bright daylight you think. Scarlet drapes are faded "
                   "from sunlight and the long table \njust looks sad and old. Especially now when last night's dinner "
                   "is only partially cleaned up.\nFood and drinks are gone but there are still plates and glasses on the table."
                   "\nThe large dancing area is empty. A few chairs are located next to the walls. In daylight this looks "
                   "\nlike a not so welcoming place to spend time."
                   "\n\nFrom the ballroom open doors to the Master bedroom, the study, and the Lord's bathroom."
                   "\nThe stairs leading to the 1st floor corridor descend from the corner."
                   "\nThere's also a pull down ladder leading to the attic here.")
    if room == 'bathroom':
        return str("\nYou are in Lord Chadwick's personal bathroom.\n"
                   "Apart from the usual toilet seat, mirror cabinet, ceramic sink, and a couple of towels hanging \non the wall,"
                   "you notice hardly anything worth your attention.\n"
                   "There is however, a surprisingly large amount of shaving scum splattered around the sink.\n"
                   "Well, maybe somebody was busy with something more important than cleaning last night.\n\n"
                   "There are doors leading to the ballroom and the study.\n")
    if room == 'bedroom':
        return str("\nYou are in the Mansion's Master bedroom.\n"
                   "The late Lord's corpse is still lying on the bed. Hair white, eyes wide open, and arms \nstiffly grasping the air. "
                   "What could've caused a man such and eerie ending?\n"
                   "Looking at the remains of your late friend you feel a sense of duty that beckons you to get \nto the bottom of this!\n\n"
                   "From the bedroom it is possible to enter the study or ballroom.\n")
    if room == 'study':
        return str("\nYou are in Lord Chadwick's study.\n"
                   "There's a desk neatly organized by the window, a comfortable chair positioned under a reading \nlamp on one corner, "
                   "and a giant bookshelf filled with volumes gracing the wall.\n"
                   "You smell the dank cigarette smoke of countless hours spent among the books here.\n\n"
                   "There are 3 doors leading to the bathroom, the bedroom, and to the ballroom.\n")
    if room == 'attic':
        return str("\nYou are in the attic of the Mansion.\n"
                   "The atmosphere is very musty, and you can see many cobwebs hanging from the beams supporting the roof.\n"
                   "The light is dim, but you can make out heeps of cardboard boxes along the walls.\n"
                   "A little light from a small window on the western end of the room reveals a small table with a chair.\n\n"
                   "The only way out is back down the ladder to the ballroom.\n")
    if room == 'bossfight':
        return str("\nYou hear strange chanting and eerie noises from the attic above you.\n"
                   "The rest of the household crowd in the ballroom franticly.\n")
        cursor=db.cursor()
        cursor.execute("update player set location=14")
def check_command (db, cmd):
    cursor = db.cursor()
    send = "select nimi from Synocmd where Synonyymi = '" + str(cmd) + "'"
    cursor.execute(send)
    results = cursor.fetchone()
    if results is not None:
        result = results[0]
        return result
    else:
        return cmd

#look-funktio tilpeh��reineen
#item kuvauksia:
pagedesc = str("\nThe page is from a book written in a strange language unknown to you.\n"
                       "There is a crude illustration of what looks like a maelstrom spinning \nabove a crowd of robe-clad men.\n")
whiskdesc = str("\nYou look at the bottle, \"Glenlivet 12yo\", nice. This is truly a great whiskey.\n")
bookdesc = str("\nThe book, written in a strange language unknown to you, seems to have been \nmostly open at a same certain section. "
                   "The words 'NULLI INCANTA DEMONUM' \nin big letters at the end of this section strike your attention.\n")
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
            return str("\nThere is only a single bottle of whiskey left in the cabinet.\n")
        else:
            return str("\nThe liquor cabinet is now empty.\n")

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
            return str("\nThere is a strange and very old looking book on the table.\n")
        else:
            return str("\nThe table is just a table. A few candle stubs on it, nothing more.\n")
    elif room == 12 and object == 'book':
        cursor.execute("update plot set state2=1")
        return bookdesc

    elif room == 10 and object == 'lord':
        return str("\nThe corpse lies on the bed totally rigid. You notice no signs of violence.\n"
                   "The expression on his face gives the impression of one scared to death.\n")

    elif room == 4 and object == 'bed':
        cursor.execute("select location from item where item.location=4")
        item = cursor.fetchone()
        if item is not None:
            return str("\nYou notice a crumbled piece of paper stashed obviously in a hurry under the pillow.\n"
                   "It looks like a page torn from a book.\n")
        else:
            return str("\nThe bed is just as it seems.")
    elif room == 4 and object == 'page':
        cursor.execute("select location from item where item.location=4")
        item = cursor.fetchone()
        if item is not None:
            return str("\nThe paper has been crumbled and stashed under the pillow.\n"
                       "It's impossible to make out any of it's content from this angle.\n")
        else:
            return pagedesc
    elif room == 11 and object == 'bookshelf':
        return str("\nExamining the bookshelf closer you notice that a book is missing.\n"
                   "Judging by the dust marks it appears to have been removed quite recently.\n")

#inventaariossa olevien tavaroiden tutkimiseen:
    elif room is not None and object in ('page', 'paper'):
        cursor.execute("select itemid from item where location=13")
        item = cursor.fetchall()
        if (2,) in item:
            return pagedesc
        else:
            return str("\nYou notice no such thing.")

    elif room is not None and object == 'whiskey':
        cursor.execute("select itemid from item where location=13")
        item = cursor.fetchall()
        if (1,) in item:
            return whiskdesc
        else:
            return str("\nYou notice no such thing.")

    elif room is not None and object == 'book':
        cursor.execute("select itemid from item where location=13")
        item = cursor.fetchall()
        if (5,) in item:
            cursor.execute("update plot set state2=1")
            return bookdesc
        else:
            return str("\nNo interesting books around here.\n")
#ja viel� koko p****n lopullinen else
    else:
        return str("\nYou notice nothing of particular interest.")
#pit�isi toimia kunnolla


#Tarkistaa synonyymit ja palauttaa joko l�ydetyn synonyymin oikean sanan tai vaihtoehtoisesti palauttaa annetun
#syotteen takaisin. huoneiden osalta palauttaa vain sanan "room".
def check_noun (db, noun):
    cursor = db.cursor()
    send = "select nimi from synocmd where synonyymi = '" + noun + "'"
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
            return str("\nYou pick up the bottle of whiskey and think, \"That will loosen up my suspects a bit..\"\n")

        elif playerroom == 4 and itemroom == 4 and object == 'page':
            cursor.execute("update item set location = 13 where itemid = 2")
            cursor.execute("update plot set state3=1")
            return str("\nYou pick up and unfold the torn page. \"I wonder what this is?\"\n")

        elif playerroom == 12 and itemroom == 12 and object == 'book':
            cursor.execute("update item set location = 13 where itemid = 5")
            return str("\nYou pick up the spellbook and notice that a page is missing. \" Hmmm there are pages missing..\"\n")
    else:
        return str("\nThere seems to be no such object nearby.\n")

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
        return str("\ninfo ei toimi")

def give(db, item):
    cursor = db.cursor()
    cursor.execute("select player.location, item.location from player left outer join item on (item.location = 13)")
    infos = cursor.fetchone()
    if infos is not None:
        playerroom = infos[0]
        itemplace = infos[1]
        if itemplace == 13:
            if playerroom == 2 and item == 'whiskey':
                cursor.execute("update item set location = null where itemid = 1")
                cursor.execute("update npc set trust = 2 where npcid = 1")
                return str("\nYou gave Willy the bottle of whiskey. \n\"OH! Papa's here! My darling!\" *followed by unadhesive irish mumble*\n")
            else:
                return str("\nThere's no one in this room who'd want that.\n")
        else:
            return str("\nYou have nothing to give.\n")
    else:
        return str("\nYou have nothing to give.\n")
#kukkuu