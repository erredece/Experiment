import Tkinter as tk

PictureListCounter = 0
globalApp = None


def PictureList(app):
    global globalApp
    globalApp = app
    globalApp.master.unbind("<Key>")
    tick()

def tick():
    global PictureListCounter
    if globalApp.experimentalBlock == 2:
        globalApp.images = ["SAW", "RABBIT", "SALTSHAK", "ANCHOR", "VIOLIN"]
    #Please note that the first image to be reproduced will be the last one of
    #the array. 
    elif globalApp.experimentalBlock == 3:
        globalApp.images = ["ANT", "FRYINGPA", "GLASSES", "CAT", "STOVE"]
    elif globalApp.experimentalBlock == 4:
        globalApp.images = ["ARROW", "AIRPLANE", "BABYCARR", "EAGLE",
                             "WINEGLAS"]
    elif globalApp.experimentalBlock == 5:
        globalApp.images = ["WAGON", "WINDMILL", "HORSE", "HEART", "BUS"]
    elif globalApp.experimentalBlock == 6:
        globalApp.images = ["CANDLE", "CAMEL", "CHURCH", "PEACOCK", "MOUNTAIN"]
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