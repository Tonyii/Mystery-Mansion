#Eetu Kaivola

# -*- coding: utf-8 -*-

def location(room):
    if room == 'guestroom':
        return str('\nYou are in the mansions guest bedroom.\nThe walls are painted light yellow and there is a '
                   'painting of a man with a firm look on his face. \nThe bed you slept in is not made and '
                   'theres an empty champagne glass on the night table. You \nget the chills from this room '
                   'now even though it didnt seem to matter last night.\n')
    if room == 'garage':
        return str("Yarr")
    if room == 'corridor':
        return str("insert corridor description here:")
    if room == 'maidroom':
        return str("insert maids chamber description here:")
    if room == 'office':
        return str("insert butlers room description here:")
    if room == 'kitchen':
        return str("insert kitchen description here:")
    if room == 'stairs':
        return str("insert stairs description here:")
    if room == 'ballroom':
        return str("insert balroom description here:")
    if room == 'bathroom':
        return str("insert bathroom description here:")
    if room == 'master bedroom':
        return str("insert master bedroom description here:")
    if room == 'study':
        return str("insert study description here:")
    if room == 'attic':
        return str("insert attic description here:")

