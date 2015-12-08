#Eetu Kaivola

# -*- coding: utf-8 -*-

#Eetu Kaivola
#224777
#eetu.kaivola@student.tut.fi
#harjoitustyö2

#Toteutettu hyvin yksinkertainen nelilaskin.
#Ohjelman käynnistyessä pyydetään syöttämään kaksi desmaalilukua,
#joille voidaan tehdä neljä eri laskutoimitusta nappia painamalla.
#Valitsemalla lopeta, ohjelma kuolee.

#määritellään koodaus
# -*- coding: utf-8 -*-
#tuodaan tkinter
from tkinter import *
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
        elif checkedverb == 'help':
            return oma_funktiot.help()

        elif checkedverb == 'talk' and checkednoun == 'person':
            return oma_funktiot.conversation(db, noun)

        elif checkedverb == 'look':
            return oma_funktiot.look(db, checkednoun)

        elif checkedverb == 'take':
            return oma_funktiot.take(db, checkednoun)

        elif checkedverb == 'give':
            return oma_funktiot.give(db, checkednoun)

        elif verb in oma_funktiot.known_helps:
            if verb == 'info':
                return oma_funktiot.info(db)
            if verb == 'inventory':
                return oma_funktiot.inventory(db)

        else:
            elsereturn = "You try to " + command + " without significant result.\n"
            return elsereturn


    except:
        IOError
alku = 0
#pluslasku
def execute_prints(anything_at_all):
    try:
        global alku
        if alku == 0:
            return
        else:

            command = str(Entry.get(cmd_line))
            ret = player_input(command)
            if ret is not None:
                Infotext.insert(END, ret)
                cmd_line.delete(0, END)
            else:
                Kuvaus(db)
        return

#syöte jotain muuta kuin lukuja
    except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!")
        return


#miinuslasku
def help_button_cmd():
    help = "\n" + str(player_input("help"))
    Infotext.insert(END, help)
    return

#kertolasku
def inv_button_cmd():
    inv = "\n" + str(player_input("inventory"))
    Infotext.insert(END, inv)
    return

#jakolasku
def jako():
    return

def Kuvaus(db):
    try:
        location = oma_funktiot.room_desc(db)
        desc = oma_funktiot.location(location)
        syote2.configure(text=str(desc))
        return desc
        #Entry.insert(syote2, desc)

    except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!")
        return virhe
        #Entry.insert(syote2, virhe)

#ohjelman lopetus
def quit_program():
    GUI.destroy()
    return

#avataan ikkuna
GUI=Tk()

#annetaan ikkunalle nimi
GUI.title("Mystery mansion")

#luodaan framet ja rajat, joihin sijoitetaan tekstikentät
#ja ohjelman toiminnot

frame=Frame(GUI)
frame.pack()

frame1 = Frame(GUI)
frame1.pack(side=TOP)

frame2=Frame(GUI)
frame2.pack()

frame3=Frame(GUI)
frame3.pack()

frame4=Frame(GUI)
frame4.pack()

#tehdään napit komennoille ja lopetukselle
execute=Button(frame3, text="execute", command=execute_prints("anything"))
execute.pack(side=RIGHT)

miinusnappi=Button(frame3, text="help", command=help_button_cmd)
miinusnappi.pack(side=RIGHT)

kertonappi=Button(frame3, text="inventory", command=inv_button_cmd)
kertonappi.pack(side=RIGHT)


lopetusnappi=Button(frame4, text="Quit", command=quit_program)
lopetusnappi.pack(side=BOTTOM)

#Kuva
back_image = PhotoImage(file="mansionBG_vaalea.gif", height = 300, width=800)

#tulostetaan syotteet
syote2=Label(frame1, justify= LEFT, compound= CENTER, padx=10, text=oma_funktiot.location("guestroom"), image=back_image, fg="white", font=("Courier", 9))
syote2.pack(side=TOP)

Printframe=Scrollbar(frame4)
Printframe.pack(side=RIGHT, fill=Y)

Infotext = Text(frame2, height=10, width=100, bg="black", fg="white")
Infotext.pack(side=TOP, fill=Y)

Printframe.config(command=Infotext.yview)
Infotext.config(yscrollcommand=Printframe.set)

#tehdään ja nimetään syötekentät

eka_luku=Label(frame4, text="What to do?",)
eka_luku.pack(side=LEFT)

cmd_line=Entry(frame4, width=50)
cmd_line.pack(side=LEFT)
cmd_line.bind('<Return>', execute_prints)

#Haetaan printeille arvot
#room_d= syote2(db)
syote1= execute_prints

#vastaus=Entry(frame, width=10)
#vastaus.pack(side=LEFT)
alku = 1


GUI.mainloop()

####
####









###VAIHTUUUUU








#######

######
THANK_YOU_FOR_PLAYING_MYSTERY_MANSION()

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
        elif checkedverb == 'help':
            oma_funktiot.help()

        elif checkedverb == 'talk' and checkednoun == 'person':
            print(oma_funktiot.conversation(db, noun))

        elif checkedverb == 'look':
            print(oma_funktiot.look(db, checkednoun))

        elif checkedverb == 'take':
            print(oma_funktiot.take(db, checkednoun))

        elif checkedverb == 'give':
            print(oma_funktiot.give(db, checkednoun))

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
      "The corpse shows no signs of violence. In fact it looks like he's been scared to death.\n"
      "You have known Lord Chadwick a long time and know his tendency to make enemies easily.\n"
      "Everyone here is a suspect. And it is your job to find out who is behind this horrible act.\n\n"
      "Eventually everyone agrees to wait in the Mansion for the phone lines to be fixed and the police notified.\n")
#intro=input("intro?, no?")
#if intro == "yes":
for char in story:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)
time.sleep(2)
input("\nPRESS ENTER TO START")

cursor=db.cursor()
cursor.execute("select * from plot")
plot = cursor.fetchone()
show_room_desc = 1

#pelin päälooppi
while plot !=(1, 1, 1, 1, 0) and plot !=(1, 1, 1, 1, 1):

    if show_room_desc == 1:
        location = oma_funktiot.room_desc(db)
        print(oma_funktiot.location(location))
        show_room_desc = 0
        print(oma_funktiot.people(db))

    first_input=input("\nWhat do you want to do?\n")
    if first_input != "quit":
        player_input(first_input)

    else:
        cursor.execute("update plot set state1=1,state2=1,state3=1,state4=1,state5=1")
        print("Thanks for playing Mystery Mansion!")
    cursor.execute("select * from plot")
    plot=cursor.fetchone()

    if plot == (1, 1, 1, 0, 0):
        cursor.execute("update npc set trust=2 where npcID=2")
#BOSSFIGHT!
while plot == (1, 1, 1, 1, 0):

    print(oma_funktiot.location("bossfight"))
    whatnow=input("What now?!\n")
    whatnow=whatnow.lower()
    while "attic" not in whatnow:
        whatnow=input("\nThere's no time for that now!\n"
                      "The strange noises from the attic become louder with each wasted moment!\n"
                      "You have to put an end to this!\n")
        whatnow=whatnow.lower()

        if "book" in whatnow:
            print("\nYou really think this is a good time for reading?!\n"
                  "Only the words 'NULLI INCANTA DEMONUM' spring to your mind.")
            whatnow=(input("What then?\n"))
            whatnow=whatnow.lower()


    whatnow=input("\nWhen you enter the attic you notice Penelope chanting at the back of the room.\n"
                        "The air is filled with acrid smoke and the room temperature plummets toward zero.\n"
                        "A horrifiying undescribable entity rushes toward you through the smoke.\n"
                        "Do something!\n")
    whatnow=whatnow.lower()
    if "nulli" in whatnow and "incanta" in whatnow and "demonum" in whatnow:
        print("\nYou hear a distant scream, like it is coming from another dimension. Penelope collapses to the floor.\n"
              "You are victorious. The demon is gone and it will never come back.\n"
              "\nAfter a few hours the police will arrive and take away the still unconscious maid with them. A happy\n"
              "ending after all. \n"
              "THANK YOU FOR PLAYING MYSTERY MANSION <3")
        cursor.execute("update plot set state5=1")
        cursor.execute("select * from plot")
        plot=cursor.fetchone()
        continue
    elif "book" in whatnow:
        print("\nYou really think this is good a time for reading?!\n"
                  "Only the words 'NULLI INCANTA DEMONUM' spring to your mind.\n")

    whatnow=(input("\nThe demonic force surrounds you in an instant!\n"
                   "You feel a choking shortness of breath!\n"
                   "Last chance, detective!\n"))
    whatnow=whatnow.lower()

    if "nulli" in whatnow and "incanta" in whatnow and "demonum" in whatnow:
        print("\nYou hear a distant scream, like it is coming from another dimension. Penelope collapses to the floor.\n"
              "You are victorious. The demon is gone and it will never come back.\n"
              "\nAfter a few hours the police will arrive and take away the still unconscious maid with them. A happy\n"
              "ending after all. \n"
              "THANK YOU FOR PLAYING MYSTERY MANSION <3")
        cursor.execute("update plot set state5=1")
        cursor.execute("select * from plot")
        plot=cursor.fetchone()
    else:
        print("\nA black hole appears to the floor. A dark hand grabs you from your chest. You can't breathe.\n"
              "The hand drags you down to eternal coldness. Only thing that you can think is NULLI INCANTA DEMONUM.\n"
              "And then. Silence...\n"
              "THANK YOU FOR PLAYING MYSTERY MANSION. TRY AGAIN WITH BETTER LUCK!")
        cursor.execute("update plot set state5=1")
        cursor.execute("select * from plot")
        plot=cursor.fetchone()
    #herp derpf