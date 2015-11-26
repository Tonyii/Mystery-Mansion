import mysql.connector
import oma_funktiot
import dialog
import getpass

hostname = 'localhost'
uname = 'root'
pswd = 'Cbr600F1'
db = oma_funktiot.open_database(hostname, uname, pswd)

end_game = 0

while end_game == 0:
    location = oma_funktiot.room_desc(db)
    print(dialog.location(location))
    oma_funktiot.move(db)
    location = oma_funktiot.room_desc(db)
    print(dialog.location(location))
    print(oma_funktiot.people(db))

    end_game=1