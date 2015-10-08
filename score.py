import Tkinter as tk 

def unravel(globalApp, stimulus):
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    c = tk.Canvas(globalApp.frame, width=globalApp.master.winfo_screenwidth(), 
    height=globalApp.master.winfo_screenheight(), bg=globalApp.black, highlightthickness=0)
    
    c.pack()
    
    unravelscore = int(round((sum(stimulus) + 0.0) / (len(stimulus) + 0.0)
                              * 100))
    
    uInstructions = tk.Label(c, text="You scored a " + 
                             str(unravelscore) + "% in this block. \n\n\n" +
                             "Press any key to continue.",
    bg= globalApp.black, fg = globalApp.white, font="Helvetica 18", 
    anchor="center")
    
    windowwidth = globalApp.master.winfo_screenwidth()/2
    windowheight = globalApp.master.winfo_screenheight()/2
    
    c.create_window(windowwidth, windowheight, anchor="center", 
                    window=uInstructions) 
    
    globalApp.master.bind("<Key>", globalApp.unravel)