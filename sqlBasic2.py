import sqlite3
import pyttsx3

tts = pyttsx3.init()

voice = tts.getProperty('voices')
tts.setProerty('voice', voices[1],id)

database = 'world.db'

conn = sqlite3.connect(database)

record = conn.execute('SELECT Name, LifeExpectancy FROM Country WHERE LifeExpectancy > 80 ORDER BY LifeExpectancy;')
# record = conn.execute('SELECT Name, population FROM Country WHERE Population < 1000000000 ORDER BY NAME;')
# record = conn.execute('SELECT Name, HeadOfState FROM Country WHERE HeadOfState < Republic ORDER BY NAME')
for row in record:
    print(row)
    tts.say(row)
    tts.runAndWait()