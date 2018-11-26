import sqlite3
from sqlite3 import Error
 
try:
    db = sqlite3.connect("/app/services/DPLA_IDs.db")
except Error as e:
    print("You may need to run populateDPLAIDs.py")
    print(e)
    exit()

def DPLAID(link):
    """
    cur = db.cursor()
    cur.execute("SELECT identifier FROM ids WHERE link=?", (link,))
    rows = cur.fetchall()
    for row in rows:
        return row
    """
    return None

def shortValidationError(fullError):
    parts = fullError.split(' in schema:')
    return parts[0]


def getISO639(langTerm):
    iso = ["eng|English","ger|German",
           "fre|French","heb|Hebrew",
           "yid|Yiddish","spa|Spanish",
		   "lat|Latin","ita|Italian",
		   "rus|Russian","jpn|Japanese",
		   "chi|Chinese", "dut|Dutch",
		   "por|Portuguese", "hun|Hungarian",
		   "ara|Arabic", "cze|Czech",
		   "swe|Swedish", "dan|Danish",
		   "pol|Polish", "nor|Norwegian"
		   "gre|Greek"]
    for line in iso:
        if langTerm in line:
            return line
