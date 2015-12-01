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

#pluslasku
def plus():
    try:
        luku1 = float(Entry.get(arvo1))
        luku2 = float(Entry.get(arvo2))
        tulos = luku1 + luku2

        Entry.delete(vastaus, 0, 30)
        Entry.insert(vastaus, 0, tulos)
#syöte jotain muuta kuin lukuja
    except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!")
        Entry.delete(vastaus, 0, 30)
        Entry.insert(vastaus, 0, virhe)



#miinuslasku
def minus():
   try:
        luku1 = float(Entry.get(arvo1))
        luku2 = float(Entry.get(arvo2))
        tulos = luku1 - luku2

        Entry.delete(vastaus, 0, 30)
        Entry.insert(vastaus, 0, tulos)
#syöte jotain muuta kuin lukuja
   except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!!")
        Entry.insert(vastaus, 0, virhe)

#kertolasku
def kerto():
   try:
        luku1 = float(Entry.get(arvo1))
        luku2 = float(Entry.get(arvo2))
        tulos = luku1 * luku2

        Entry.delete(vastaus, 0, 30)
        Entry.insert(vastaus, 0, tulos)
#syöte jotain muuta kuin lukuja
   except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!!")
        Entry.insert(vastaus, 0, virhe)
#jakolasku
def jako():
   try:
        luku1 = float(Entry.get(arvo1))
        luku2 = float(Entry.get(arvo2))
        tulos = luku1 / luku2

        Entry.delete(vastaus, 0, 30)
        Entry.insert(vastaus, 0, tulos)
#syöte jotain muuta kuin lukuja
   except ValueError:
        virhe = ("Et antanut pelkkiä lukuja!")
        Entry.insert(vastaus, 0, virhe)

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

frame2=Frame(GUI, borderwidth=0)
frame2.pack()

frame3=Frame(GUI, borderwidth=5)
frame3.pack()

frame4=Frame(GUI)
frame4.pack()

#tehdään napit laskutoimituksille ja lopetukselle
plusnappi=Button(frame3, text="+", command=plus)
plusnappi.pack(side=LEFT)

miinusnappi=Button(frame3, text="-", command=minus)
miinusnappi.pack(side=LEFT)

kertonappi=Button(frame3, text="*", command=kerto)
kertonappi.pack(side=LEFT)

jakonappi=Button(frame3, text="/", command=jako)
jakonappi.pack(side=LEFT)

lopetusnappi=Button(frame4, text="Lopeta", command=lopeta)
lopetusnappi.pack(side=BOTTOM)

#tehdään ja nimetään syötekentät
ylateksti=Label(frame2, text="Syötä kaksi lukua:")
ylateksti.pack(side=TOP)

eka_luku=Label(frame2, text="Ensimmäinen luku")
eka_luku.pack(side=LEFT)

arvo1=Entry(frame2, width=5)
arvo1.pack(side=LEFT)

toka_luku=Label(frame2, text="Toinen luku")
toka_luku.pack(side=LEFT)

arvo2=Entry(frame2, width=5)
arvo2.pack(side=LEFT)

tulos=Label(frame4, text="Tulos:")
tulos.pack()

vastaus=Entry(frame4, width=30)
vastaus.pack(side=LEFT)

GUI.mainloop()