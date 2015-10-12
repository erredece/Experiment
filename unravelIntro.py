import Tkinter as tk

def intro(globalApp):

    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    c = tk.Canvas(globalApp.frame, width=globalApp.master.winfo_screenwidth(), 
    height=globalApp.master.winfo_screenheight(), bg=globalApp.black, highlightthickness=0)
    
    c.pack()
    
    textblock =""
    if globalApp.experimentalBlock == 1:
        textblock = ("You will now perform a mechanical activity known as the "
                     "UNRAVEL task. You will see a letter\n and a digit, as " 
                     "well as a box. One of them will be inside the box and "
                     "the other one outside.\n The letter and digit will " 
                     "also change in colour, value and font. Your task will "
                     "consist\n  on following the steps provided on the sheet, "
                     "following always the same sequence.\n \n For example, "
                     "for the first step you will press U if the letter or the "
                     "digit is underlined, or I if\n one of them is in "
                     "italics. It will always be one or the other. After you "
                     "press the key, you will\n then move to the second step. "
                     "The sequence is the same for the whole experiment.\nOnce "
                     "you get to the end, you will continue at the first " 
                     "step. \n\n It is encouraged that you perform this task "
                     "as fast and efficiently as possible,\neven though there "
                     "is no time limit.\n\n This is a practice block, so your "
                     "responses will not be recorded and\n you will receive "
                     "feedback if you make any mistake.\n\nPress any key to "
                     "continue. Good luck!")
    elif globalApp.experimentalBlock == 2:
        textblock = ("Now you will perform the same UNRAVEL task, but before "
        "starting \n you will see a series of images that you have to memorize."
        "\n\nThen, while you perform the UNRAVEL task, you will be interrupted "
        "at random steps to show\n a picture. You will have to reply if the "
        "image was on the list you previously memorized.\n\n Press Enter if it "
        "was on the list or press Space if not. You will have 3 seconds to "
        "reply.\n\n This is the last practice block, and the experimental "
        "blocks will consist on the same task.\n\n Press any key to continue. " 
        "Good luck!")
    elif globalApp.experimentalBlock == 3:
        textblock = ("This is the first experimental block. Remember that now "
        "your responses will be recorded.\n\n Press any key to continue. Good "
        "luck!")
    elif globalApp.experimentalBlock == 4:
        textblock = ("This is the second experimental block.\n\n Press any key "
        "to continue.")
    elif globalApp.experimentalBlock == 5:
        textblock = ("This is the third experimental block. \n\n Press any key "
        "to continue.")
    elif globalApp.experimentalBlock == 6:
        textblock = ("This is the fourth and last experimental block. \n\n Press"
        " any key to continue.")
    else:
        pass
    
    uInstructions = tk.Label(c, text= textblock,
    bg= globalApp.black, fg = globalApp.white, font="Helvetica 18", 
    anchor="center")
    
    windowwidth = globalApp.master.winfo_screenwidth()/2
    windowheight = globalApp.master.winfo_screenheight()/2
    
    c.create_window(windowwidth, windowheight, anchor="center", 
                    window=uInstructions) 
    if globalApp.experimentalBlock == 1:
        globalApp.master.bind("<Key>", globalApp.unravel)
    else:
        globalApp.master.bind("<Key>", globalApp.PictureList)