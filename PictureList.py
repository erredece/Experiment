import Tkinter as tk
#import time

def PictureList(app):
    global showPicCounter
    if app.frame:
        app.frame.destroy()
        app.frame = tk.Frame(app.master, width=app.master.winfo_screenwidth(), 
            height=app.master.winfo_screenheight())
        app.frame.pack()
    
    pictures = tk.Canvas(app.frame, width=app.master.winfo_screenwidth(), 
    height=app.master.winfo_screenheight(), bg=app.black, highlightthickness=0)
    pictures.pack()
    images = ["ACCORDIO", "AIRPLANE", "ALLIGATO", "ANCHOR", "ANT"]
    showPicCounter = 0
    pic = tk.PhotoImage(file="pics/" + images[showPicCounter] + ".gif")
    piclabel = tk.Label(pictures, image=pic)
    piclabel.config(image=pic) 
    piclabel.image = pic # keep a reference!    
    

    def addOnePic():
        global showPicCounter
        showPicCounter += 1
        print showPicCounter
    
    showPics = True
    
    while showPics:
        piclabel.after(1, addOnePic)
       
        if showPicCounter == 6:
            showPics = False
    
    piclabel.pack()  
    pictures.create_window(app.master.winfo_screenwidth()/2, 
                               app.master.winfo_screenheight()/2, 
                               anchor="center", window=piclabel)    
    