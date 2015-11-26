import mysql.connector

#
# Avaa tietokantayhteyden.
#
def avaa_tietokanta(hostname, uname, pswd):
    return mysql.connector.connect(
        host=hostname, user=uname, passwd=pswd, db="peli",buffered=True
    )

#
# Palauttaa pelaajan nykyisen sijainnin.
#
def sijainti(db):
    cur = db.cursor()
    cur.execute("select sijainti from pelihahmo where id = 1");
    return (cur.fetchone())[0]

#
# Palauttaa annetun paikan kuvauksen.
#
def kuvaus(db, id):
    cur = db.cursor()
    cur.execute("select kuvaus from paikka where id = " + str(id))
    return (cur.fetchone())[0]

#
# Palauttaa listan mahdollisista kulkusuunnista.
#
def suunnat(db, id):
    cur = db.cursor()
    cur.execute("select p, e, i, l from paikka where id = " + str(id))
    rivi = cur.fetchone()
    kompassi = ['p', 'e', 'i', 'l']
    suunnat = []
    for i in range(0, 4):
        if rivi[i] is not None:
            suunnat.append(kompassi[i])
    return suunnat

#
# Palauttaa listan annetun paikan esineiden nimista.
#
def esineet(db, id):
    cur = db.cursor()
    cur.execute("select kuvaus from objekti where sijainti = " + str(id))
    esineet = []
    tulos = cur.fetchall()
    for rivi in tulos:
        esineet.append(rivi[0])
    return esineet

#
# Palauttaa tiedon siita, onko roistoon tormatty aikaisemmin.
#
def onko_roisto_tavattu(db):
    cur = db.cursor()
    cur.execute("select arvo from juonenkaanne where id = 1")
    return (cur.fetchone())[0]

#
# Paivittaa tiedon siita, etta roisto on poistunut.
#
def poista_roisto(db):
    cur = db.cursor()
    cur.execute("update juonenkaanne set arvo = 1 where id = 1")

#
# Tallettaa tiedon siita, etta roisto on hoideltu.
#
def roisto_on_hoideltu(db):
    cur = db.cursor()
    cur.execute("update juonenkaanne set arvo = 1 where id = 1")

#
# Palauttaa tiedon siita kuinka monta kertaa kayty metsaaukealla.
#
def kerrat_aukealla(db):
    cur = db.cursor()
    cur.execute("select arvo from juonenkaanne where id = 2")
    return (cur.fetchone())[0]

#
# Tallettaa kaynnin metsaaukealla.
#
def talleta_kaynti_aukealla(db):
    cur = db.cursor()
    cur.execute("update juonenkaanne set arvo = arvo + 1 where id = 2")

#
# Palauttaa annetun objektin sijainnin (None, jos hallussa)
#
def objektin_sijainti(db, kuvaus):
    cur = db.cursor()
    cur.execute(
        "select sijainti from objekti where kuvaus = '" + kuvaus + "'"
    )
    if cur.rowcount == 0:
        return None
    return (cur.fetchone())[0]

#
# Avaa yhteyden annetusta huoneesta annettuun suuntaan (p/e/i/l)
#
def avaa_suunta(db, lahto, tulo, suunta):
    cur = db.cursor()
    cur.execute(
        "update paikka set " +
        suunta + " = " + str(tulo) + " " +
        "where id = " + str(lahto)
    )

#
# Palauttaa pelaajan hallussa olevien tavaroiden painon.
#
def laske_paino(db):
    cur = db.cursor()
    cur.execute("select paino from objekti where omistaja = 1")
    tulos = cur.fetchall()
    paino = 0
    for rivi in tulos:
        paino += float(rivi[0])
    return paino

#
# Palauttaa annetun objektin painon.
#
def objektin_paino(db, kuvaus):
    cur = db.cursor()
    cur.execute(
        "select paino from objekti where kuvaus = '" + kuvaus + "'"
    )
    return float((cur.fetchone())[0])

#
# Komento: siirtyminen (p, e, i, l)
#
# Palauttaa 1 jos siirtyminen onnistui, 0 muuten.
#
def komento_siirry(db, sijainti, suunta):
    cur1 = db.cursor()
    cur1.execute(
        "select " + suunta + " from paikka where id = " + str(sijainti)
    )
    rivi = cur1.fetchone()
    if rivi[0] is None:
        return 0
    uusi_sijainti = str(rivi[0])
    cur2 = db.cursor()
    cur2.execute(
        "update pelihahmo set sijainti = " + uusi_sijainti + " where id = 1")
    return 1

#
# Komento: ota
#
def komento_ota(db, kuvaus):
    cur1 = db.cursor()
    cur1.execute(
        "update objekti set omistaja = 1 where kuvaus = '" + kuvaus + "'"
    )
    cur2 = db.cursor()
    cur2.execute(
        "update objekti set sijainti = NULL where kuvaus = '" + kuvaus + "'"
    )

#
# Komento: kamat
#
def komento_kamat(db):
    cur = db.cursor()
    cur.execute("select kuvaus from objekti where omistaja = 1")
    kamat = []
    tulos = cur.fetchall()
    for rivi in tulos:
        kamat.append(rivi[0])
    return kamat

#
# Komento: tiputa
#
def komento_tiputa(db, kuvaus, sijainti):
    cur1 = db.cursor()
    cur1.execute(
        "update objekti set sijainti = " +
        str(sijainti) +
        " where kuvaus = '" + kuvaus + "' and omistaja = 1"
    )
    cur2 = db.cursor()
    cur2.execute(
        "update objekti set omistaja = NULL where kuvaus = '" +
        kuvaus + "' and omistaja = 1"
    )
    return cur2.rowcount


