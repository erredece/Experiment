import Tkinter as tk

showPicCounter = 0
globalApp = None

def PictureList(app):
    global globalApp
    globalApp = app
    tick()

def tick():
    global showPicCounter
    images = ["ACCORDIO", "AIRPLANE", "ALLIGATO", "ANCHOR", "ANT"]
    #Please note that the first image to be reproduced will be the last one of
    #the array. 
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
    
    
    pic = tk.PhotoImage(file="pics/" + images[showPicCounter - 1] + ".gif")
    piclabel = tk.Label(pictures, image=pic)
    piclabel.config(image=pic) 
    piclabel.image = pic # keep a reference!  
    piclabel.pack()  
    
    pictures.create_window(globalApp.master.winfo_screenwidth()/2, 
                               globalApp.master.winfo_screenheight()/2, 
                               anchor="center", window=piclabel)  
    
    if showPicCounter <= len(images) -1 :
        showPicCounter += 1
        globalApp.master.after(3000, tick)
    else:
        showPicCounter = 0
        globalApp.unravel(globalApp)
    print showPicCounter