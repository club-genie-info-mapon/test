from tkinter import *

app = Tk()
app.title('My App')
app.geometry('300x300')

label = Label(app, text="Hello World", font=('Arial', 16))
label.pack()

button = Button(app, text="Click me", background="blue", foreground="black")
button.pack()

app.mainloop()