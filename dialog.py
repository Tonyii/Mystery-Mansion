#Eetu Kaivola

# -*- coding: utf-8 -*-
import oma_funktiot
import mysql.connector


def location(room):
    if room == 'guestroom':
        return str("\nYou are in the mansion's guest bedroom.\nThe walls are painted light yellow and there is a "
                   "painting of a man with a firm look on his face. \nThe bed you slept in is not made and "
                   "there is an empty champagne glass on the night table. \nYou get the chills from this room "
                   "now even though it did not seem to matter last night.\n")
    if room == 'garage':
        return str("You enter the groundskeepers garage.\n"
                   "The door barely opens enough for you to slip in. There's boxes behind the door that havent been "
                   "touched \n"
                   "in ages. Rakes, shovels and picks fill the walls and a moist air mixed with the scent of wood "
                   "fills \n"
                   "your lugns. At the end of the room theres a small lamp that glances yellowy light across the "
                   "room and a workdesk.\n")
    if room == 'corridor':
        return str("You look across a long corridor.\n"
                   "The patterns on wallpapers run through the corridor. Few seemingly old mablewood sideboards with \n"
                   "golden finishing and red silken veils on the walls resemble just how wealthy the residents living\n"
                   "here are. There's paintings of noble men lined up on the walls and you feel a quiet breeze coming\n"
                   "from the window.\n")
    if room == 'maidroom':
        return str("insert maids chamber description here:")
    if room == 'office':
        return str("\nYou enter the office.\nThere's a nice view from the windows, a large wooden desk and an executive sized "
                   "leather chair behind it and two not-so-comfortable\nlooking chairs in front of the desk. "
                   "Wouldn't want to work here, you think. The desk is neatly\norganized: pencil holder, phone, "
                   "calendar, phone book. Nothing out of the ordinary on your first glance.\n ")
    if room == 'kitchen':
        return str("\nYou walk into the kitchen.\nFirst thing that you notice is that the chef has to be a superior "
                   "being. The kitchen is straight from the 18th century.\nWell, at least there is enough room "
                   "for a fridge, liquor cabinet, baking oven and shelves for pans,\npots and other cutlery. The Chef "
                   "himself is leaning over the sink apparently working on lunch. He is not easily distracted "
                   "you think.\nNo sign of him noticing you are in the room.\n")
    if room == 'stairs':
        return str("\nYou arrive at the stairs.\nThank god they are wide you think remembering last nights fumbles "
                   "downstairs. Otherwise it is just a staircase. Nothing of interest in here.\nJust go up or down.\n")
    if room == 'ballroom':
        return str("You are in the ballroom.\nNot so stylish in bright daylight you think. Scarlet drapes are faded "
                   "from sunlight and the long table just looks sad and old.\nEspecially now when last nights dinner "
                   "is only partially cleaned up. Food and drinks are gone but there are still\nplates and glasses. "
                   "The large dancing area is empty. A few chairs are located next to the walls. In daylight this looks "
                   "like a not so welcoming place to spend time.\n")
    if room == 'bathroom':
        return str("You are in the bathroom. \n"
                   "Apart from the usual toilet seat, mirror cabinet, ceramic sink, and a couple of towels hanging on the wall,\n"
                   "you notice hardly anything worth your attention. \n"
                   "There is however, a surprisingly large amount of shaving scum splattered around the sink.\n"
                   "Well, maybe somebody was busy with something more important than cleaning last night.\n")
    if room == 'master bedroom':
        return str("You are in the Mansion's master bedroom.\n"
                   "The late Lord's corpse is still lying on the bed. Hair white, eyes wide open, and arms stiffly grasping the air.\n"
                   "What could've caused a man such and eerie ending? You feel a sense of duty that beckons you to get to the bottom of this!\n")
    if room == 'study':
        return str("You are in Lord Chadwick's personal study.\n"
                   "There's a desk neatly organized by the window, a comfortable chair positioned under a reading lamp on one corner,\n"
                   "and a giant bookshelf filled with volumes gracing the wall.\n"
                   "You smell the dank cigarette smoke of countless hours spent among the books here.\n")
    if room == 'attic':
        return str("You are in the attic of the Mansion.\n"
                   "The atmosphere is very musty, and you can see many cobwebs hanging from the beams supporting the roof.\n"
                   "The light is dim, but you can make out heeps of cardboard boxes along the walls.\n"
                   "A little light from a small window on the western end of the room reveals a small table with a chair.\n")

