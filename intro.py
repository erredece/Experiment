import Tkinter as tk

def intro(app):
    
    if app.frame:
        app.frame.destroy()
        app.frame = tk.Frame(app.master, width=app.master.winfo_screenwidth(), 
            height=app.master.winfo_screenheight())
        app.frame.pack()
    
    introCanvas = tk.Canvas(app.frame, width=app.master.winfo_screenwidth(), 
    height=app.master.winfo_screenheight(), bg=app.black, highlightthickness=0)
    
    introCanvas.pack()
    
    introtext = tk.Label(introCanvas, text="In this experiment, you will be " + 
    "performing a mechanical task known as the UNRAVEL task.\n Its" + 
    "instructions will be explained by the supervisor and also in the next" + 
    "screen \n\n\n\n You will also have to memorize a series of pictures and" +
    "then recognize them\n from a series of other pictures which  will be " +
    "rotated in 0, 90 and 180 degrees.\n\n\n\n Press any key to continue.",
    bg= app.black, fg = app.white, font="Helvetica 18", anchor="center")
    
    windowwidth = app.master.winfo_screenwidth()/2
    windowheight = app.master.winfo_screenheight()/2
    
    introCanvas.create_window(windowwidth, windowheight, anchor="center",
                               window=introtext) 
    
    app.master.bind("<space>", app.unravelIntro())