

#määritellään koodaus
# -*- coding: utf-8 -*-
#tuodaan tkinter
from tkinter import *
import mysql.connector
import time
import sys
import tk_oma_funktiot
import getpass

#asd
hostname = 'localhost'
uname = 'player'
pswd = 'mm'
db = tk_oma_funktiot.open_database(hostname, uname, pswd)

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
introyes = input("yes")
if introyes == "yes":
    for char in story:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)
time.sleep(2)
input("\nPRESS ENTER TO START")

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
        checkedverb = tk_oma_funktiot.check_command(db, verb)
        checkednoun = tk_oma_funktiot.check_noun(db, noun)

        #tarkistaa onko palautettu "go" verbi ja "room" subst.
        if checkedverb == 'go' and checkednoun == 'room':
            #lahettaa sitten alkuperaisen noun:in
            tk_oma_funktiot.move(db, noun)
            global show_room_desc
            show_room_desc = 1
            move_ret = "\nYou stepped into " + noun + "\n"
            Infotext.insert("1.0", move_ret)
            return

        elif checkedverb == 'help':
            return tk_oma_funktiot.help()

        elif checkedverb == 'talk' and checkednoun == 'person':
            return tk_oma_funktiot.conversation(db, noun)

        elif checkedverb == 'look':
            return tk_oma_funktiot.look(db, checkednoun)

        elif checkedverb == 'take':
            return tk_oma_funktiot.take(db, checkednoun)

        elif checkedverb == 'give':
            return tk_oma_funktiot.give(db, checkednoun)

        elif verb == 'info':
            return tk_oma_funktiot.info(db)

        elif verb == 'inventory':
            return tk_oma_funktiot.inventory(db)

        else:
            elsereturn = "\nYou try to " + command + " without significant result.\n"
            return elsereturn


    except:
        IOError
starting = 0
#pluslasku
def execute_prints(anything_at_all):
    try:
        global starting
        if starting == 0:
            return
        else:

            command = str(Entry.get(cmd_line))
            ret = player_input(command)
            if ret is not None:
                Infotext.insert("1.0", ret)
                cmd_line.delete(0, END)
            else:
                Kuvaus(db)
                cmd_line.delete(0, END)
        return

#syöte jotain muuta kuin lukuja
    except ValueError:
        virhe = ("WRONG DUMBASS")
        return


#miinuslasku
def help_button_cmd():
    help = player_input("help")
    Infotext.insert("1.0", help)
    return

#kertolasku
def inv_button_cmd():
    inv = "\n" + str(player_input("inventory"))
    Infotext.insert("1.0", inv)
    return

#jakolasku
def jako():
    return


def Kuvaus(db):
    try:
        location = tk_oma_funktiot.room_desc(db)
        desc = tk_oma_funktiot.location(location)
        room_desc_widget.configure(text=str(desc))
        return desc
        #Entry.insert(syote2, desc)

    except ValueError:
        virhe = ("WRONG")
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

frame=Frame(GUI, bg="black", bd=1)
frame.pack()

frame1 = Frame(frame)
frame1.pack(side=TOP)

frame2=Frame(frame)
frame2.pack()

frame3=Frame(frame)
frame3.pack()

frame4=Frame(frame, bg="black")
frame4.pack()

#tehdään napit komennoille ja lopetukselle
#execute=Button(frame3, text="execute", bg="black", fg="white", command=execute_prints("anything"))
#execute.pack(side=RIGHT)

help_button_widget=Button(frame3, text="help", bg="black", fg="white", command=help_button_cmd)
help_button_widget.pack(side=RIGHT)

inventory_button_widget=Button(frame3, text="inventory", bg="black", fg="white", command=inv_button_cmd)
inventory_button_widget.pack(side=RIGHT)


quit_button_widget=Button(frame4, text="Quit", bg="black", fg="white", command=quit_program)
quit_button_widget.pack(side=BOTTOM)

#Kuva
back_image = PhotoImage(file="mansionBG_vaalea.gif")

#tulostetaan syotteet
room_desc_widget=Label(frame1, width=800, bd=0, padx=0, pady=0, justify= LEFT, compound= CENTER, text=tk_oma_funktiot.location("guestroom"), image=back_image, fg="white", font=("Courier", 9))
room_desc_widget.pack(side=TOP)

scroller_widget=Scrollbar(frame2, bg="black")
scroller_widget.pack(side=RIGHT, fill=Y)

Infotext = Text(frame2, height=10, width=100, bg="black", fg="white", padx=0, pady=0)
Infotext.pack(side=TOP, fill=Y)

scroller_widget.config(command=Infotext.yview)
Infotext.config(yscrollcommand=scroller_widget.set)

#tehdään ja nimetään syötekentät

what_to_do_text=Label(frame4, text="What to do?", bg="black", fg="white")
what_to_do_text.pack(side=LEFT)

cmd_line=Entry(frame4, width=50, bg="black", fg="white")
cmd_line.pack(side=LEFT)
cmd_line.bind('<Return>', execute_prints)

#Haetaan printeille arvot
#room_d= syote2(db)
syote1= execute_prints

#vastaus=Entry(frame, width=10)
#vastaus.pack(side=LEFT)
starting = 1


GUI.mainloop()

####
####