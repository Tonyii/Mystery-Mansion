#Eetu Kaivola

# -*- coding: utf-8 -*-
from sys import argv
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host="localhost",
                      user= "root",
                      passwd="",
                      db="harjoitus",
                      buffered=True)

def avaa_tietokanta():
    print("foobar")

def move(direction):
    if direction == 'west':
        print("foo")

def beginning():
    try:
        filu=open('tarina.txt', 'r')
        teksti = filu.read()
        tekstikentta.insert(END, teksti)
        print(teksti)

    except SystemError:
        virhe = ("could not open file.")


def apuva():
    try:
        apu= open('commands.txt', 'r')
        print(apu.read())
    except SystemError:
        ei_loydy=("Could not open help file")
def lopetus():
    GUI.destroy()
    return

GUI=Tk()
menubar = Menu(GUI)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Open", command=openfile)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=lopetus)
menubar.add_cascade(label="File", menu=filemenu)
GUI.config(menu=menubar)#, background='black')#, fg='green')
GUI.geometry('720x405')



GUI.title("Mystery Mansion")

#luodaan framet ja rajat, joihin sijoitetaan tekstikentät
#ja ohjelman toiminnot

mainframe=Frame(GUI)
mainframe.pack()

frame2=Frame(GUI)
frame2.pack(side=BOTTOM)

#frame3=Frame(GUI, borderwidth=5)
#frame3.pack()

#frame4=Frame(GUI)
#frame4.pack()

aloitusnappi=Button(mainframe, text="Begin", command=beginning)
aloitusnappi.pack(side=LEFT)

lopetusnappi=Button(frame2, text="Lopeta", command=lopetus)
lopetusnappi.pack(side=BOTTOM)

tekstikentta = Text(mainframe)

GUI.mainloop()

act = ''

while act != 'quit':

    direction = ''
    act = input("What to do? ")
    if act == 'help':
        apuva()
    if act == ('go', direction) :
        move(direction)

beginning()