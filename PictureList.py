import Tkinter as tk
#import time

def PictureList(app):
    if app.frame:
        app.frame.destroy()
        app.frame = tk.Frame(app.master, width=app.master.winfo_screenwidth(), 
            height=app.master.winfo_screenheight())
        app.frame.pack()
    
    pictures = tk.Canvas(app.frame, width=app.master.winfo_screenwidth(), 
    height=app.master.winfo_screenheight(), bg=app.black, highlightthickness=0)
    pictures.pack()
    pic = tk.PhotoImage(file="pics/ACCORDIO.gif")
    piclabel = tk.Label(pictures, image=pic)
    piclabel.image = pic # keep a reference!
    piclabel.pack()
    
    pictures.create_window(app.master.winfo_screenwidth()/2, 
                           app.master.winfo_screenheight()/2, 
                           anchor="center", window=piclabel)