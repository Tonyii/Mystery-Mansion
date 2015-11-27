#Eetu Kaivola

# -*- coding: utf-8 -*-

###############################################################################
#
#  S E I K K A I L U P E L I
#
# (c) Miikka Maki-Uuro, 2014
#
###############################################################################
import getpass
import mysql.connector
import referenssi_funktiot

#
# Luodaan tietokantayhteys.
#
host = input("palvelin : ")
ktunnus = input("ktunnus  : ")
salasana = getpass.getpass("salasana : ")
db = referenssi_funktiot.avaa_tietokanta(host, ktunnus, salasana)

#
# Pelin paasilmukka:
#
# - tulostetaan paikan kuvaus
# - tulostetaan mahdolliset kulkusuunnat
# - tulostetaan paikalla olevat esineet
# - tulostetaan mahdolliset erikoistapahtumat
# - luetaan ja jasennetaan kayttajan komento
# - suoritetaan komento
#
lopetus = 0
while lopetus == 0:

    # Hae sijainti ja tulosta kuvaus.
    sijainti = referenssi_funktiot.sijainti(db)
    kuvaus = referenssi_funktiot.kuvaus(db, sijainti)
    print("")
    print(kuvaus)

    # Tulosta mahdolliset kulkusuunnat.
    suunnat = referenssi_funktiot.suunnat(db, sijainti)
    if len(suunnat) > 0:
        print("Voit kulkea:", suunnat)

    # Tulosta paikalla olevat esineet.
    esineet = referenssi_funktiot.esineet(db, sijainti)
    if len(esineet) > 0:
        print("Taalla on:", esineet)

    # Erikoistapahtuma 1: roisto metsatiella.
    if sijainti == 6 and referenssi_funktiot.onko_roisto_tavattu(db) == 0:
        print("Taalla on resuinen roisto! Han ei paasta sinua etenemaan.")

    # Erikoistapahtuma 2: peli paattyy 3. kerralla metsaaukealla.
    if sijainti == 7:
        referenssi_funktiot.talleta_kaynti_aukealla(db)
        if referenssi_funktiot.kerrat_aukealla(db) == 3:
            print("Ihana tunne valtaa sinut... elama hymyilee!")
            print("Peli on paattynyt. Olet sankari!!!!!!!!!!!!")
            lopetus = 1
            continue

    # Luetaan ja jasennellaan kayttajan komento.
    print("")
    komentorivi = input("> ")
    if komentorivi == "":
        continue
    komentolista = komentorivi.split()
    if len(komentolista) == 1:
        verbi = komentolista[0]
        objekti = ""
    elif len(komentolista) == 2:
        verbi = komentolista[0]
        objekti = komentolista[1]
    else:
        print("Ymmarran vain yhden tai kahden sanan komentoja.")

    # Komento: p/e/i/l
    if verbi == "p" or verbi == "e" or verbi == "i" or verbi == "l":
        if referenssi_funktiot.komento_siirry(db, sijainti, verbi) == 0:
            print("Sinne suuntaan ei paase!")

    # Komento: ota
    elif verbi == "ota":
        if objekti == "":
            print("Mita olisi pitanyt ottaa?!")
        else:
            objektin_sijainti = referenssi_funktiot.objektin_sijainti(db, objekti)
            if objektin_sijainti is None or objektin_sijainti != sijainti:
                print(objekti, "ei ole otettavissa!")
            elif referenssi_funktiot.laske_paino(db) + referenssi_funktiot.objektin_paino(db, objekti) > 10:
                print("Liian painava!")
            else:
                referenssi_funktiot.komento_ota(db, objekti)
                print(objekti, "otettu.")

    # Komento: kamat
    elif verbi == "kamat":
        kamat = referenssi_funktiot.komento_kamat(db)
        print("Sinulla on:", kamat)

    # Komento: tiputa
    elif verbi == "tiputa":
        if objekti == "":
            print("Mita olisi pitanyt tiputtaa?!")
        elif referenssi_funktiot.komento_tiputa(db, objekti, sijainti) == 0:
            print(objekti, "ei tiputettavissa!")
        else:
            print(objekti, "tiputettu.")

    # Komento: avaa
    elif verbi == "avaa":
        if objekti != "ovi":
            print("Mita olisi pitanyt avata?!")
        elif sijainti != 1 and sijainti != 2:
            print("Ei taalla ole ovea.")
        elif referenssi_funktiot.objektin_sijainti(db, "avain") != None:
            print("Ei sinulla ole avainta.")
        else:
            referenssi_funktiot.avaa_suunta(db, 1, 2, "i")
            referenssi_funktiot.avaa_suunta(db, 2, 1, "l")
            print("Ovi on auki.")

    # Komento: anna
    elif verbi == "anna":
        if objekti == "":
            print("Mita olisi pitanyt antaa?!")
        elif referenssi_funktiot.objektin_sijainti(db, objekti) is not None:
            print("Ei sinulla ole sita.")
        elif objekti != "kolikko" or sijainti != 6 or referenssi_funktiot.onko_roisto_tavattu(db) != 0:
            print("Ei vaikutusta.")
        else:
            referenssi_funktiot.poista_roisto(db)
            referenssi_funktiot.avaa_suunta(db, 6, 7, "i")
            referenssi_funktiot.avaa_suunta(db, 7, 6, "l")
            print("Roisto ottaa tyytyvaisena kolikon ja haipyy metsaan!")

    # Komento: lopeta
    elif verbi == "lopeta":
        lopetus = 1

    # Tuntematon komento.
    else:
        print("En ymmarra...")

    # Jos haluat tallettaa tilanteen joka kierroksella: db.commit()

print("Kiitos pelista. Nahdaan taas!")
# Jos haluat etta tilanne talletetaan pelin paatteeksi: db.commit()
