import Tkinter as tk

def intro(globalApp):
    
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    introCanvas = tk.Canvas(globalApp.frame, width=globalApp.master.winfo_screenwidth(), 
    height=globalApp.master.winfo_screenheight(), bg=globalApp.black, highlightthickness=0)
    
    introCanvas.pack()
    
    introtext = tk.Label(introCanvas, text="In this experiment, you will be " + 
    "performing a mechanical task known as the UNRAVEL task.\n Its" + 
    "instructions will be explained by the supervisor and also in the next" + 
    "screen \n\n\n\n You will also have to memorize a series of pictures and" +
    "then recognize them\n from a series of other pictures which  will be " +
    "rotated in 0, 90 and 180 degrees.\n\n\n\n Press any key to continue.",
    bg= globalApp.black, fg = globalApp.white, font="Helvetica 18", anchor="center")
    
    windowwidth = globalApp.master.winfo_screenwidth()/2
    windowheight = globalApp.master.winfo_screenheight()/2
    
    introCanvas.create_window(windowwidth, windowheight, anchor="center",
                               window=introtext) 
    
    globalApp.master.bind("<Key>", globalApp.unravelIntro)