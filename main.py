import mysql.connector
import oma_funktiot
import dialog
import getpass

hostname = 'localhost'
uname = 'player'
pswd = 'mm'
db = oma_funktiot.open_database(hostname, uname, pswd)

def player_input(command):
    try:
        command_list=command.split()

        verb = command_list[0]
        noun = command_list[-1]
        #ignore hurr all capital letters in commands
        verb = verb.lower()
        noun = noun.lower()
        flag = 0



        if verb not in oma_funktiot.known_commands or noun not in oma_funktiot.known_rooms\
                and noun not in oma_funktiot.known_people and noun not in oma_funktiot.known_objects\
                and noun not in oma_funktiot.known_items:
            print("You try to", command, "without significant result.")

        elif verb == 'go' or 'move' or 'exit' or 'walk' or 'travel' or 'climb' or 'crawl' or 'run' and noun in oma_funktiot.known_rooms:
            #print(verb, noun)
            oma_funktiot.move(db, noun)
            global show_room_desc
            show_room_desc = 1

        elif verb == 'talk'or 'ask' or 'interrogate' or 'interview' or 'speak' or 'tell' and noun in oma_funktiot.known_people:
            print("foo")


    except:
        IOError


end_game = 0
show_room_desc = 1

#pelin päälooppi
while end_game == 0:

    if show_room_desc == 1:
        location = oma_funktiot.room_desc(db)
        print(dialog.location(location))
        show_room_desc = 0

    #print(oma_funktiot.people(db))
    first_input=input("What do you want to do?\n")
    if first_input != "quit":
        player_input(first_input)
    else: end_game = 1

