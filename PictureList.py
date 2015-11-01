import Tkinter as tk
from random import shuffle

PictureListCounter = 0
globalApp = None


def PictureList(app):
    global globalApp
    globalApp = app
    globalApp.master.unbind("<Key>")
    tick()

def tick():
    global PictureListCounter
    if globalApp.experimentalBlock == 2 and PictureListCounter == 0:
        globalApp.images = ["SAW", "RABBIT", "SALTSHAK", "ANCHOR", "VIOLIN"]
        shuffle(globalApp.images)
    elif globalApp.variable[globalApp.phasecounter] == "control" and PictureListCounter == 0:
        globalApp.images = ["ARROW", "AIRPLANE", "BABYCARR", "EAGLE",
                             "WINEGLAS"]
        shuffle(globalApp.images)
    elif globalApp.variable[globalApp.phasecounter] == "90" and PictureListCounter == 0:
        globalApp.images = ["ANT", "FRYINGPA", "GLASSES", "CAT", "STOVE"]
        shuffle(globalApp.images)
    elif globalApp.variable[globalApp.phasecounter] == "180" and PictureListCounter == 0:
        globalApp.images = ["WAGON", "WINDMILL", "HORSE", "HEART", "BUS"]
        shuffle(globalApp.images)
    elif globalApp.variable[globalApp.phasecounter] == "mix" and PictureListCounter == 0:
        globalApp.images = ["CANDLE", "CAMEL", "CHURCH", "PEACOCK", "MOUNTAIN"]
        shuffle(globalApp.images)
    else:
        pass
    

    
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, 
            width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    pictures = tk.Canvas(globalApp.frame, 
                         width=globalApp.master.winfo_screenwidth(), 
                         height=globalApp.master.winfo_screenheight(), 
                         bg=globalApp.black, highlightthickness=0)
    pictures.pack()
    
    
    pic = tk.PhotoImage(file="pics/" + globalApp.images[PictureListCounter - 1] +
                         ".gif")
    piclabel = tk.Label(pictures, image=pic)
    piclabel.config(image=pic) 
    piclabel.image = pic # keep a reference!  
    piclabel.pack()  
    
    pictures.create_window(globalApp.master.winfo_screenwidth()/2, 
                               globalApp.master.winfo_screenheight()/2, 
                               anchor="center", window=piclabel)  
    
    if PictureListCounter <= len(globalApp.images) -1 :
        PictureListCounter += 1
        globalApp.master.after(3000, tick)
    else:
        PictureListCounter = 0
        globalApp.unravel(globalApp)