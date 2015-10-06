import Tkinter as tk
import time

showPicCounter = 0
globalApp = None

def PictureList(app):
    global globalApp
    globalApp = app
    
    '''while showPics:
        elapsedTime = globalApp.elapsedTime
        
        if elapsedTime % 3 == 0:
            addOnePic()
            
        if showPicCounter == 3:
            showPics = False'''
    
    tick()

def tick():
    global showPicCounter
    showPicCounter += 1
    
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    pictures = tk.Canvas(globalApp.frame, width=globalApp.master.winfo_screenwidth(), 
    height=globalApp.master.winfo_screenheight(), bg=globalApp.black, highlightthickness=0)
    pictures.pack()
    images = ["ACCORDIO", "AIRPLANE", "ALLIGATO", "ANCHOR", "ANT"]
    
    pic = tk.PhotoImage(file="pics/" + images[showPicCounter - 1] + ".gif")
    piclabel = tk.Label(pictures, image=pic)
    piclabel.config(image=pic) 
    piclabel.image = pic # keep a reference!  
    piclabel.pack()  
    
    pictures.create_window(globalApp.master.winfo_screenwidth()/2, 
                               globalApp.master.winfo_screenheight()/2, 
                               anchor="center", window=piclabel)  
    
    if showPicCounter < 5:
        globalApp.master.after(3000, tick)
    else:
        globalApp.master.destroy()
        