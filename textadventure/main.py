import mysql.connector
import time
import sys
import oma_funktiot
import getpass

#asd
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
        checkedverb = oma_funktiot.check_command(db, verb)
        checkednoun = oma_funktiot.check_noun(db, noun)

        #tarkistaa onko palautettu "go" verbi ja "room" subst.
        if checkedverb == 'go' and checkednoun == 'room':
            #lahettaa sitten alkuperaisen noun:in
            oma_funktiot.move(db, noun)
            global show_room_desc
            show_room_desc = 1

        elif checkedverb == 'talk' and checkednoun == 'person':
            print(oma_funktiot.conversation(db, noun))

        elif checkedverb == 'look':
            print(oma_funktiot.look(db, checkednoun))

        elif checkedverb == 'take':
            print(oma_funktiot.take(db, checkednoun))

        elif verb in oma_funktiot.known_helps:
            if verb == 'info':
                print(oma_funktiot.info(db))
            if verb == 'inventory':
                print(oma_funktiot.inventory(db))

        else:
            print("You try to", command, "without significant result.")


    except:
        IOError

story = ("It was a dark and stormy night when Lord Chadwick hosted his party.\nYou remember that a falling tree cut off the electricity.\n"
      "Phones were dead and you were the only one without a chauffeur, so you stayed the night.\n"
      "After waking up to a slight hangover and terrible headache, you hear screaming from upstairs. \n"
      "You could swear it is Lady Sonya.\n\n"
      "The screaming stops but you can still hear commotion and people running up the stairs.\n"
      "You get up, put your pants and shoes on and make for the upstairs too.\n\n"
      "The scene is horrifying.\n"
      "Lord Chadwick lies dead on his bed. Stiffened arms stretched out, a frozen look of horror on his face.\n"
      "The corpse shows no signs of violence. In fact it Looks like he's been scared to death.\n"
      "You have known Lord Chadwick a long time and know his tendency to make enemies easily.\n"
      "Everyone here is a suspect. And it is your job to find out who is behind this horrible act.\n\n"
      "Eventually everyone agrees to wait in the Mansion for the phone lines to be fixed and the police notified.\n")
for char in story:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)
input("\nPRESS ENTER TO START")

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

#herp derp