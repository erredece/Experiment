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
    
    def showPic(piclabel):
        def addOnePic():
            global showPicCounter
            showPicCounter += 1
            piclabel.after(1000,addOnePic)
            piclabel.config(image=pic)
        addOnePic()
        
    showPic(piclabel)   
    
    piclabel.image = pic # keep a reference!    
    
    pictures.create_window(app.master.winfo_screenwidth()/2, 
                               app.master.winfo_screenheight()/2, 
                               anchor="center", window=piclabel)
    piclabel.pack()    

        