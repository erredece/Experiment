import Tkinter as tk 

def demographics(globalApp):
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, 
            width=globalApp.master.winfo_screenwidth()/2, 
            height=globalApp.master.winfo_screenheight()/2)
        globalApp.frame.pack()
    
    c = tk.Canvas(globalApp.frame, width=globalApp.master.winfo_screenwidth(), 
    height=globalApp.master.winfo_screenheight(),  
    highlightthickness=0)
    
    c.pack()
    
    globalApp.master.configure(cursor ="arrow") 
        
    gender = 0
    male = tk.IntVar()
    female = tk.IntVar()
    
    def gender():
        age.get()
        print age
        if male.get() == 1 and female.get() == 0:
            gender = "M"
            print gender

        elif female.get() == 1 and male.get() == 0:
            gender = "F"
            print gender
        else:
            print "MEEECK"
        
    gendertext = tk.Label(c, text="Your sex:", font = "Helvetica 18")
    malebox = tk.Checkbutton(c, text="Male", variable=male, 
                             font = "Helvetica 18")
    femalebox = tk.Checkbutton(c, text="Female", variable=female,
                                font = "Helvetica 18")
    abort = tk.Button(c, text='Quit', command=globalApp.master.quit, 
                      font = "Helvetica 18")
    statusbutton = tk.Button(c, text='Show', command=gender, 
                              font = "Helvetica 18")
    age = tk.Entry(c, font = "Helvetica 18")

    windowwidth = globalApp.master.winfo_screenwidth()/2
    windowheight = globalApp.master.winfo_screenheight()/2
    
    c.create_window(windowwidth, windowheight-150, anchor="center", 
                    window=gendertext)  
    c.create_window(windowwidth, windowheight-50, anchor="center", 
                    window=malebox)    
    c.create_window(windowwidth, windowheight, anchor="center", 
                    window=femalebox)  
    c.create_window(windowwidth, windowheight+50, anchor="center", 
                    window=abort)  
    c.create_window(windowwidth, windowheight+200, anchor="center", 
                    window=statusbutton)  
    c.create_window(windowwidth, windowheight+100, anchor = "center",
                    window = age)
    
