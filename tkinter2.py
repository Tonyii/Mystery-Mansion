#Ohj1
#Eetu Kaivola
#eetu.kaivola@student.tut.fi
#224777
#ohjelma toteuttaa seitenottelun pistelaskennan
#ja tulostuksen omaan tiedostoonsa

#Globaali muuttuja (yök), joka laittaa "-" suorittamattomaan lajiin
TULOS_PUUTTUU = "-"

#Tehdään luokka, jossa listataan kaikki
#tarvittavat muuttujat ja asetetaan ne
#käyttöä varten. Nimet itsensäselittäviä.
class Kilpailija:

    def __init__(self, numero, nimi, sarja):
        self.__numero = numero
        self.__nimi = nimi
        self.__sarja = sarja
        self.__laji = 0
        self.__pikajuoksu = TULOS_PUUTTUU
        self.__pituus = TULOS_PUUTTUU
        self.__kuula = TULOS_PUUTTUU
        self.__korkeus = TULOS_PUUTTUU
        self.__aidat = TULOS_PUUTTUU
        self.__seivas = TULOS_PUUTTUU
        self.__pitka_juoksu =  TULOS_PUUTTUU
        self.__summa = 0.0

#kokonaissumma
    def __laske_summa(self, pisteet):
        self.__summa += float(pisteet)
        self.__laji = self.__laji +1
#pikajuoksun pisteet
    def aseta_pikajuoksu(self, pisteet):
        self.__pikajuoksu = pisteet
        self.__laske_summa(pisteet)
    def tarkista_pikajuoksu(self):
        return self.__pikajuoksu != TULOS_PUUTTUU
#pituushypyn pisteet
    def aseta_pituus(self, pisteet):
        self.__pituus = pisteet
        self.__laske_summa(pisteet)
    def tarkista_pituus(self):
        return self.__pituus != TULOS_PUUTTUU
#kuulantyönnön pisteet
    def aseta_kuula(self, pisteet):
        self.__kuula = pisteet
        self.__laske_summa(pisteet)
    def tarkista_kuula(self):
        return self.__kuula != TULOS_PUUTTUU
#korkeushypyn pisteet
    def aseta_korkeus(self, pisteet):
        self.__korkeus = pisteet
        self.__laske_summa(pisteet)
    def tarkista_korkeus(self):
        return self.__korkeus != TULOS_PUUTTUU
#aitajuoksun pisteet
    def aseta_aidat(self, pisteet):
        self.__aidat = pisteet
        self.__laske_summa(pisteet)
    def tarkista_aidat(self):
        return self.__aidat != TULOS_PUUTTUU
#seiväshypyn pisteet
    def aseta_seivas(self, pisteet):
        self.__seivas = pisteet
        self.__laske_summa(pisteet)
    def tarkista_seivas(self):
        return self.__seivas != TULOS_PUUTTUU
#1000m juoksun pisteet
    def aseta_pitka_juoksu(self, pisteet):
        self.__pitka_juoksu = pisteet
        self.__laske_summa(pisteet)
    def tarkista_pitka_juoksu(self):
        return self.__pitka_juoksu != TULOS_PUUTTUU
#tietojen tallennus ja yhdistäminen
    def tallennus(self):
        return ';'.join([str(self.__numero), self.__nimi, self.__sarja.strip('\n'),
                         self.__pikajuoksu,
                         self.__pituus,
                         self.__kuula,
                         self.__korkeus,
                         self.__aidat,
                         self.__seivas,
                         self.__pitka_juoksu,
                         "{0:0.1f}".format(self.__summa),
                         str(self.__laji) + '/7'])
#osallistujatiedoston luku ja virhetarkistus
def osallistujatiedosto(nimi, kilpailijat):
    #avataan tiedosto
    try:
        virta = open(nimi, "r",  encoding="utf-8")
    #virheilmo
    except IOError:
        print("Virhe osallistujatiedoston lukemisessa.")
        raise
    else:
        #jaetaan osiin ja tarkistellaan onko tiedosto oikeanlainen
        for rivi in virta:
            osat = rivi.split(";")
            if len(osat) != 3:
                print("Virheellinen osallistujatiedosto: rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;nimi;sarja.")
                raise ValueError

            if osat[0] in kilpailijat:
                print("Virheellinen osallistujatiedosto: tunnus "
                      + osat[0] + " toistuu.")
                raise KeyError
            #viedään tiedot luokkaan
            #selite: osat [0] numero, [1] nimi, [2] sarja,
            # [:-1] puolipisteen poistaminen
            kilpailijat[osat[0]] = Kilpailija(osat[0], osat[1], osat[2])
        virta.close()

#asetetaan eri lajeille omat aliohjelmansa
def pikajuoksu(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise ValueError

            elif kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            elif kilpailijat[osat[0]].tarkista_pikajuoksu():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_pikajuoksu("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()

def pituushyppy(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise ValueError
            if kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            if kilpailijat[osat[0]].tarkista_pituus():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_pituus("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    #ei saada auki
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()

def kuulantyonto(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise ValueError
            if kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            if kilpailijat[osat[0]].tarkista_kuula():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_kuula("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    #ei saada auki
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()

def korkeushyppy(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise ValueError
            if kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            if kilpailijat[osat[0]].tarkista_korkeus():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_korkeus("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    #ei saada auki
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()

def aitajuoksu(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise ValueError
            if kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            if kilpailijat[osat[0]].tarkista_aidat():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_aidat("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    #ei saada auki
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()

def seivashyppy(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise SyntaxError

            if kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            if kilpailijat[osat[0]].tarkista_seivas():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_seivas("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    #ei saada auki
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()

def pitka_juoksu(nimi, kilpailijat):

    try:
        #avataan
        stream = open(nimi, "r",  encoding="utf-8")
        for rivi in stream:
            #pilkotaan
            osat = rivi.split(";")
            #virheelliset sisällöt
            if len(osat) != 2 or not osat[1][:-1].isnumeric():
                print("Virheellinen lajitiedosto " + nimi + ": rivi '"
                      + rivi[:-1] + "' ei ole muodossa tunnus;pisteet.")
                raise ValueError
            if kilpailijat.get(osat[0]) is None:
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " puuttuu osallistujatiedostosta.")
                raise KeyError
            if kilpailijat[osat[0]].tarkista_pitka_juoksu():
                print("Virheellinen lajitiedosto " + nimi + ": tunnus "
                      + osat[0] + " toistuu.")
                raise ValueError
            #viedään pisteet
            kilpailijat[osat[0]].aseta_pitka_juoksu("{0:0.1f}".format(float
                                                (osat[1][:-1])))
    #ei saada auki
    except IOError:
        print("Virhe lajitiedoston " + nimi + " lukemisessa.")
        raise
    else:
        stream.close()




def tuloskirjaus(nimi, kilpailijat):

    try:
        #avataan tuloskirjaus
        stream = open(nimi, "w",  encoding="utf-8")
        #ensimmäinen rivi tiedostossa on aina tämä
        stream.write("tunnus;nimi;sarja;juoksu-60m;pituushyppy;kuulantyonto;"
                     "korkeushyppy;aitajuoksu-60m;seivashyppy;juoksu-1000m;"
                     "kokonaispisteet;lajeja\n")
        #sortataan osallistujat järjestykseen
        for numero in sorted(kilpailijat):
            stream.write(kilpailijat[numero].tallennus() + '\n')
    #ei pysty kirjoittamaan
    except IOError:
        print("Virhe tulostiedoston kirjoittamisessa.")
    else:
        #onnistunut suoritus
        stream.close()
        print ("Tulokset kirjoitettu tiedostoon " + nimi + ".")


def main():
    #kilpailijoiden säilö
    kilpailijat = {}


    try:
        #avataan yksi kerrallaan tiedostoja luettavaksi
        #käyttäen aliohjlemia

        osallistujatiedosto("osallistujat.txt", kilpailijat)

        pikajuoksu("juoksu-60m.txt", kilpailijat)

        pituushyppy("pituushyppy.txt", kilpailijat)

        kuulantyonto("kuulantyonto.txt", kilpailijat)

        korkeushyppy("korkeushyppy.txt", kilpailijat)

        aitajuoksu("aitajuoksu-60m.txt", kilpailijat)

        seivashyppy("seivashyppy.txt", kilpailijat)

        pitka_juoksu("juoksu-1000m.txt", kilpailijat)

        tuloskirjaus("tulokset.txt", kilpailijat)
    #mahdolliset virhetilanteet
    except IOError:
        pass
    except ValueError:
        pass
    except KeyError:
        pass


main()