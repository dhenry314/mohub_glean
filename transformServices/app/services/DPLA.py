import sqlite3
from sqlite3 import Error
 
try:
    db = sqlite3.connect("DPLA_IDs.db")
except Error as e:
    print(e)
    exit()
    
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE ids(identifier TEXT PRIMARY KEY, link TEXT)
''')
db.commit()

with open("/home/dhenry/Downloads/records.txt") as fileobject:
    for line in fileobject:
        parts = line.split("|")
        identifier = parts[1]
        link = parts[2]
        cursor.execute('''INSERT INTO ids(identifier,link) VALUES(?,?)''', (identifier,link))
        db.commit()
        print(str(identifier) + " | " + str(link))
