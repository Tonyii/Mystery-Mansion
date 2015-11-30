import mysql.connector

import oma_funktiot
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

        #if verb not in oma_funktiot.known_commands:
            #print("You try to", command, "without significant result.")
        checkedcmd = oma_funktiot.check_command(db, verb)
        if checkedcmd in oma_funktiot.known_moves and noun in oma_funktiot.known_rooms:
            oma_funktiot.move(db, noun)
            global show_room_desc
            show_room_desc = 1

        elif verb in oma_funktiot.known_talks and noun in oma_funktiot.known_people:
            print(oma_funktiot.conversation(db, noun))

        else:
            print("You try to", command, "without significant result.")


    except:
        IOError


end_game = 0
show_room_desc = 1

#pelin päälooppi
while end_game == 0:

    if show_room_desc == 1:
        location = oma_funktiot.room_desc(db)
        print(oma_funktiot.location(location))
        show_room_desc = 0
        print(oma_funktiot.people(db))

    first_input=input("What do you want to do?\n")
    if first_input != "quit":
        player_input(first_input)
    else: end_game = 1

