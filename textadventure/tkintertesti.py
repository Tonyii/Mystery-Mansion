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



#pluslasku
def plus(syote):
    try:
        luku1 = str(Entry.get(arvo1))
        luku2 = str(Entry.get(arvo1))
        tulos = luku1 + luku2



#syöte jotain muuta kuin lukuja
    except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!")



#miinuslasku
def minus():
    return

#kertolasku
def kerto():
    return

#jakolasku
def jako():
    return

def syote2(db):
    try:
        location = oma_funktiot.room_desc(db)
        desc = oma_funktiot.location(location)
        return desc
        #Entry.insert(syote2, desc)

    except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!")
        return virhe
        #Entry.insert(syote2, virhe)

#ohjelman lopetus
def lopeta():
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

frame1 = Frame(GUI, borderwidth=150)
frame1.pack(side=TOP)

frame2=Frame(GUI, borderwidth=150)
frame2.pack()

frame3=Frame(GUI, borderwidth=5)
frame3.pack()

frame4=Frame(GUI)
frame4.pack()

#tehdään napit laskutoimituksille ja lopetukselle
plusnappi=Button(frame3, text="execute", command=plus)
plusnappi.pack(side=RIGHT)

miinusnappi=Button(frame3, text="help", command=minus)
miinusnappi.pack(side=RIGHT)

kertonappi=Button(frame3, text="inventory", command=kerto)
kertonappi.pack(side=RIGHT)

#jakonappi=Button(frame3, text="/", command=jako)
#jakonappi.pack(side=LEFT)

lopetusnappi=Button(frame4, text="Quit", command=lopeta)
lopetusnappi.pack(side=BOTTOM)

#tehdään ja nimetään syötekentät
#ylateksti=Label(frame2, text="Syötä kaksi lukua:")
#ylateksti.pack(side=TOP)

eka_luku=Label(frame4, text="What to do?",)
eka_luku.pack(side=LEFT)

arvo1=Entry(frame4, width=5)
arvo1.pack(side=LEFT)

#toka_luku=Label(frame2, text="Toinen luku")
#toka_luku.pack(side=LEFT)

#arvo1=Entry(frame2, width=5)
#arvo1.pack(side=LEFT)
syote= """tahan tulee tapahtumia"""
#plus(syote)
syote2= syote2(db)


syote2=Label(frame1, text=syote2)
syote2.pack(side=TOP)

tulos=Label(frame2, text=syote)
tulos.pack(side=TOP)

#vastaus=Entry(frame, width=10)
#vastaus.pack(side=LEFT)



GUI.mainloop()


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