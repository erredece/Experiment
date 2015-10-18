import Tkinter as tk
import sys  

def outro(globalApp):
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    c = tk.Canvas(globalApp.frame, width=globalApp.master.winfo_screenwidth(), 
    height=globalApp.master.winfo_screenheight(), bg=globalApp.black, highlightthickness=0)
    
    c.pack()
    
    outrotext = tk.Label(c, text="That was the last experimental block.\n\n" + 
                         "Thank you very much for participating.\n\n " + 
                         "Press any key to finish the experiment.",
    bg= globalApp.black, fg = globalApp.white, font="Helvetica 18", 
    anchor="center")
    
    windowwidth = globalApp.master.winfo_screenwidth()/2
    windowheight = globalApp.master.winfo_screenheight()/2
    
    c.create_window(windowwidth, windowheight, anchor="center", 
                    window=outrotext) 
    
    paccuracy1 = (sum(globalApp.imageaccuracy1) + 
                  0.0) / len(globalApp.imageaccuracy1)
    pfalsealarm1 = (sum(globalApp.falsealarm1) + 
                  0.0) / len(globalApp.falsealarm1)
    paccuracy2 =(sum(globalApp.imageaccuracy2) + 
                  0.0) / len(globalApp.imageaccuracy2)
    pfalsealarm2 = (sum(globalApp.falsealarm2) + 
                  0.0) / len(globalApp.falsealarm2)
    paccuracy3 = (sum(globalApp.imageaccuracy3) + 
                  0.0) / len(globalApp.imageaccuracy3)
    pfalsealarm3 = (sum(globalApp.falsealarm3) + 
                  0.0) / len(globalApp.falsealarm3)
    paccuracy4 = (sum(globalApp.imageaccuracy4) + 
                  0.0) / len(globalApp.imageaccuracy4)
    pfalsealarm4= (sum(globalApp.falsealarm4) + 
                  0.0) / len(globalApp.falsealarm4)
    
    
    maindata = [str(globalApp.ID), str(globalApp.gender), str(globalApp.age),
                str(paccuracy1), str(pfalsealarm1), str(paccuracy2), 
                str(pfalsealarm2), str(paccuracy3), str(pfalsealarm3),
                str(paccuracy4), str(pfalsealarm4)]
    
    f = open("data/main_data.txt", "a")
    f.write(" ".join(maindata))
    f.write("\n")
    f.close()
    
    pfile = open("data/participant_"+ str(globalApp.ID) + ".txt", "a")
    for i in range(0, 9):
        pfile.write(str(globalApp.imageaccuracy1[i]) + " " + 
                    str(globalApp.falsealarm1[i]) + " " +
                    str(globalApp.imageaccuracy2[i]) + " " + 
                    str(globalApp.falsealarm2[i]) + " " +
                    str(globalApp.imageaccuracy3[i]) + " " + 
                    str(globalApp.falsealarm3[i]) + " " +
                    str(globalApp.imageaccuracy4[i]) + " " + 
                    str(globalApp.falsealarm4[i]) + "\n")
    pfile.close()
    
    globalApp.master.bind("<Key>", sys.exit)