import time
import sys

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





# -*- coding: utf-8 -*-
#tuodaan tkinter
from tkinter import *

import oma_funktiot


def execute_prints():
    ret = "HELLOOOeadadaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    T.insert(END, ret)
    return
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

frame1 = Frame(GUI, borderwidth=50 )
frame1.pack(side=TOP)

frame2=Frame(GUI, borderwidth=50)
frame2.pack()

frame3=Frame(GUI, borderwidth=20)
frame3.pack()

frame4=Frame(GUI)
frame4.pack()



#tehdään napit komennoille ja lopetukselle
execute=Button(frame3, text="execute", command=execute_prints)
execute.pack(side=RIGHT)

lopetusnappi=Button(frame4, text="Quit", command=lopeta)
lopetusnappi.pack(side=BOTTOM)



#tulostetaan syotteet
syote2=Label(frame1, padx=10, text=oma_funktiot.location("guestroom"))
syote2.pack(side=TOP)

S = Scrollbar(frame2)
T = Text(frame2, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
kuvaus = oma_funktiot.location("guestroom")
quote = kuvaus
T.insert(END, quote)




GUI.mainloop()