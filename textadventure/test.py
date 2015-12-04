import mysql.connector
import oma_funktiot

hostname = 'localhost'
uname = 'player'
pswd = 'mm'
db = oma_funktiot.open_database(hostname, uname, pswd)

cursor=db.cursor()
send = "select npc.npcid, npc.trust from SynoPerson, npc where synoperson.Synonyymi = '" + suspect + "' and where npc.location in (select location from player) and Synoperson.personID = npc.npcid"
cursor.execute(send)
plot=cursor.fetchone()
print(plot)

