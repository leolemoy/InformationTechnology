from guizero import App, Text, TextBox, PushButton, Picture

app = App(title='Cool Guy Leo', bg = 'blue', width=200, height=200)
username = 'Leo'
password = 'password'
def check_input():
    if un_box.value == username and pw_box.value == password:
        message = Text(app, text='Correct')
    else:
        message = Text(app, text='Incorrect')
un_box = TextBox(app, text = 'Enter Name')
pw_box = TextBox(app, text = 'Enter Password')
submit = PushButton(app, text='Submit', command=check_input)
picture = Picture(app, image="Boo.png")


# text1 = Text(app, text = 'Hello, you suck the big clocks', size = 20, font = 'Californian FB', color=(255,0,255), align='120,500')
# app.yesno(title="yes or no", text = 'Would you like to close this window?')
# app.warn(title='Oh no', text='You have 13 viruses')

app.display()