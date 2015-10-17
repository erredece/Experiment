import Tkinter as tk 
import os.path

def demographics(globalApp):
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, 
            width=400, 
            height=400)
        globalApp.frame.pack()
    
    c = tk.Canvas(globalApp.frame, width=400, 
    height=400,  
    highlightthickness=0)
    
    c.pack()
    
    globalApp.master.configure(cursor ="arrow") 
    globalApp.master.geometry("{0}x{1}+0+0".format(
            400, 400))
    male = tk.IntVar()
    female = tk.IntVar()
    windowwidth = 200
    windowheight = 200
    
    def start():
        checkage = False
        checkgender = False
        checkID = False
        missingtext = "       Please introduce your data.     "
        if male.get() == 1 and female.get() == 0:
            globalApp.gender = "M"
            checkgender = True

        elif female.get() == 1 and male.get() == 0:
            globalApp.gender = "F"
            checkgender = True
        else:
            checkgender = False
            
        try:
            globalApp.age = int(age.get())
            checkage = True

        except:
            checkage = False
        
        try:
            globalApp.ID = int(ID.get())
            if os.path.exists("data/participant_"+ str(globalApp.ID) + ".txt"):
                checkID = False
            else:
                checkID = True
            
        except:
            checkID = False          
        
        if checkage == False or checkgender == False or checkID == False:

            if checkage  and checkgender:
                missingtext = "Please introduce a valid ID number."
            elif checkage  and checkID:
                missingtext = "       Please select your gender.      "
            elif checkgender and checkID:
                missingtext = "       Please introduce your age.      "
            else:
                pass
                
            missingdata = tk.Label(c, text = missingtext,
                              font ="Helvetica 18", fg = globalApp.red)
            c.create_window(windowwidth, windowheight+170, anchor="center",
                              window=missingdata)
        else:
            globalApp.master.configure(cursor ="none") 
            globalApp.master.geometry("{0}x{1}+0+0".format(
            globalApp.master.winfo_screenwidth(), 
            globalApp.master.winfo_screenheight()))
            globalApp.intro()
            
    welcome = tk.Label(c, text="Please, fill in the data below:", font="Helvetica 18")        
    IDtext = tk.Label(c, text="Participant ID:",
                               font = "Helvetica 18")
    ID = tk.Entry(c, font="Helvetica 18", width = 5)
        
    gendertext = tk.Label(c, text="Gender:", font = "Helvetica 18")
    malebox = tk.Checkbutton(c, text="Male    ", variable=male, 
                             font = "Helvetica 18")
    femalebox = tk.Checkbutton(c, text="Female", variable=female,
                                font = "Helvetica 18")
    abort = tk.Button(c, text='Abort', command=globalApp.master.quit, 
                      font = "Helvetica 18")
    startbutton = tk.Button(c, text='Start', command=start, 
                              font = "Helvetica 18")
    agetext = tk.Label(c, text="Age:", font= "Helvetica 18")
    age = tk.Entry(c, font = "Helvetica 18", width=5)
    
    c.create_window(windowwidth, windowheight-150, anchor="center",
                    window=welcome)
    c.create_window(windowwidth-80, windowheight-80, anchor="center", 
                    window=IDtext)
    c.create_window(windowwidth+50, windowheight-80, anchor="center",
                    window=ID)
    c.create_window(windowwidth-50, windowheight-15, anchor="center", 
                    window=gendertext)  
    c.create_window(windowwidth+70, windowheight-30, anchor="center", 
                    window=malebox)    
    c.create_window(windowwidth+70, windowheight, anchor="center", 
                    window=femalebox)  
    c.create_window(windowwidth-30, windowheight+40, anchor="center",
                    window=agetext)
    c.create_window(windowwidth+50, windowheight+40, anchor = "center",
                    window = age)
    c.create_window(windowwidth-50, windowheight+120, anchor="center", 
                    window=abort)  
    c.create_window(windowwidth+50, windowheight+120, anchor="center", 
                    window=startbutton)  
