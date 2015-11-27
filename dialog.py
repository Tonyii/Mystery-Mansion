#Eetu Kaivola

# -*- coding: utf-8 -*-

def location(room):
    if room == 'guestroom':
        return str('\nYou are in the mansions guest bedroom.\nThe walls are painted light yellow and there is a '
                   'painting of a man with a firm look on his face. \nThe bed you slept in is not made and '
                   'there is an empty champagne glass on the night table. You \nget the chills from this room '
                   'now even though it did not seem to matter last night.\n')
    if room == 'garage':
        return str("Yarr")
    if room == 'corridor':
        return str("insert corridor description here:")
    if room == 'maidroom':
        return str("insert maids chamber description here:")
    if room == 'office':
        return str("\nYou enter the office.\nNice view from the windows, large wooden desk and executive sized "
                   "leather chair behind it and two not-so-comfortable\nlooking chairs in front of the desk. "
                   "Would not want to work here you think. On the desk is neatly\norganized: pencil holder, phone,"
                   "calendar, phone book. Nothing out of ordinary on your first glance.\n ")
    if room == 'kitchen':
        return str("\nYou walk into the kitchen.\nFirst thing that you notice is that the chef has to be superior "
                   "being. The kitchen is straight from the 18th century.\nWell, at least there is enough room "
                   "for fridge, liquor cabinet, baking oven and shelves for pans,\npot and other cutlery. Chef "
                   "himself is leaning over the sink apparently working on lunch. He is not easily distracted "
                   "you think.\nNo sign of him noticing you are in the room.\n")
    if room == 'stairs':
        return str("\nYou arrive at the stairs.\nThank god they are wide you think remembering last nights fumbles "
                   "downstairs. Otherwise it is just a staircase. Nothing of interest in here.\nJust go up or down.\n")
    if room == 'ballroom':
        return str("You are in the ballroom\nNot so stylish in bright daylight you think. Scarlet drapes are faded "
                   "from sunlight and the long table just looks sad and old.\nSpecially now when last nights dinner "
                   "is only partially cleaned up. Food and drinks are gone but there are still\nplates and glasses. "
                   "Large dancing area is empty. Few chairs are located next to the walls. In daylight this looks "
                   "not so welcoming place to spend time.\n")
    if room == 'bathroom':
        return str("insert bathroom description here:")
    if room == 'master bedroom':
        return str("insert master bedroom description here:")
    if room == 'study':
        return str("insert study description here:")
    if room == 'attic':
        return str("insert attic description here:")

