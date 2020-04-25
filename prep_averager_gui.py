from tkinter import *

window = Tk()

window.title("Prep Averager __V__3.0")
#sets default window size
window.geometry('350x200')
window.configure(bg = 'purple')
lbl = Label(window, text="Hello")
#setting lbl position in window
lbl.grid(column=0, row=0)
#function for handleing the button click
def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)

#creates a button
btn = Button(window, text="Click Me")
#sets positionof button
btn.grid(column=5, row=0)
#endless loop of window being displyed. (required to show window)
window.mainloop()
