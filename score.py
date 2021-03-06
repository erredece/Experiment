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
    
    globalApp.master.unbind("<Key>")
    
    blockscore = (sum(stimulus) + 0.0) / (len(stimulus) + 0.0) * 100
    
    unravelscore = int(round(blockscore))
    blockname = ""
    if globalApp.experimentalBlock == 1:
        blockname = "Practice Block 1"
    elif globalApp.experimentalBlock == 2:
        blockname = "Practice Block 2"
    elif globalApp.experimentalBlock == 3:
        blockname = "Experimental Block 1"
        globalApp.pdata1 = blockscore
    elif globalApp.experimentalBlock == 4:
        globalApp.pdata2 = blockscore
        blockname = "Experimental Block 2"
    elif globalApp.experimentalBlock == 5:
        globalApp.pdata3 = blockscore
        blockname = "Experimental Block 3"
    elif globalApp.experimentalBlock == 6:
        globalApp.pdata4 = blockscore
        blockname = "Experimental Block 4"
    else:
        pass
    
    uInstructions = tk.Label(c, text="That is the end of " + blockname + 
                             "\n\n\nYou " + "scored a " + str(unravelscore) + 
                             "% in this block. \n\n\n" +
                             "Press any key to continue.",
    bg= globalApp.black, fg = globalApp.white, font="Helvetica 18", 
    anchor="center")
    
    windowwidth = globalApp.master.winfo_screenwidth()/2
    windowheight = globalApp.master.winfo_screenheight()/2
    
    c.create_window(windowwidth, windowheight, anchor="center", 
                    window=uInstructions) 
    
    def Continue():
        if globalApp.experimentalBlock <= 6:
            globalApp.master.bind("<Key>", globalApp.unravelIntro)
        else:
            globalApp.master.bind("<Key>", globalApp.outro)
    
    globalApp.master.after(500, Continue)