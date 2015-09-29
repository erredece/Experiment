import Tkinter as tk

def intro(app):
    

    if app.frame:
        app.frame.destroy()
        app.frame = tk.Frame(app.master, width=app.master.winfo_screenwidth(), 
            height=app.master.winfo_screenheight())
        app.frame.pack()
    
    c = tk.Canvas(app.frame, width=app.master.winfo_screenwidth(), 
    height=app.master.winfo_screenheight(), bg=app.black, highlightthickness=0)
    
    c.pack()
    
    uInstructions = tk.Label(c, text="PLACEHOLDER",
    bg= app.black, fg = app.white, font="Helvetica 18", anchor="center")
    
    windowwidth = app.master.winfo_screenwidth()/2
    windowheight = app.master.winfo_screenheight()/2
    
    c.create_window(windowwidth, windowheight, anchor="center", 
                    window=uInstructions) 
    
    app.master.bind("<space>", app.unravel)