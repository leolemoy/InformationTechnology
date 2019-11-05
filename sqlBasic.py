import sqlite3
from guizero import App, PushButton, Picture

database = 'world.db'  # create variable name for database
app = App(title='Cool Guy Leo', bg = 'blue', width=200, height=200)
conn = sqlite3.connect(database)  # connect to database

def select_all():
    record2 = conn.execute('SELECT LifeExpectancy, Name FROM Country WHERE LifeExpectancy > 60 ORDER By LifeExpectancy;')
    #printer(record)
    for row in record2:
        print(row)

button1 = PushButton(app, text='Population', command = select_all)
button2 = PushButton(app, text='Life Expectancy', command = select_all)
button3 = PushButton(app, text='Republic')
button4 = PushButton(app, text='Counties Independents')


app.display()
conn.close()

# record1 = conn.execute('SELECT LifeExpectancy, Name FROM Country WHERE LifeExpectancy > 60 ORDER By LifeExpectancy;')
# record2 = conn.execute('SELECT Name, population FROM Country WHERE Population < 1000000 ORDER BY NAME;')
# record3 = conn.execute('SELECT Name, IndepYear FROM Country WHERE IndepYear > 1900 ORDER BY NAME;')


