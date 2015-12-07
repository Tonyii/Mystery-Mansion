
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