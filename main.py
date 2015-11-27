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
        #ignore all capital letters in commands
        verb = verb.lower()
        noun = noun.lower()


        if verb not in oma_funktiot.known_commands or noun not in oma_funktiot.known_rooms:
            print("You try to", command, "without significant result.")

        elif verb == 'go' or 'move' or 'exit' or 'walk' or 'travel' or 'climb' or 'crawl' or 'run' and noun in oma_funktiot.known_rooms:
            print(verb, noun)
            oma_funktiot.move(db, noun)



    except:
        IOError


end_game = 0

while end_game == 0:


    location = oma_funktiot.room_desc(db)
    print(dialog.location(location))
    #oma_funktiot.move(db)
    location = oma_funktiot.room_desc(db)
    print(dialog.location(location))
    #print(oma_funktiot.people(db))

    player_input(input("What do you want to do? "))
    location = oma_funktiot.room_desc(db)
    print(dialog.location(location))

    end_game=1