import Tkinter as tk
from random import shuffle

globalApp = None

timerswitch = 0
imagestimulus = []

def showPic(app):
    global globalApp
    global timerswitch
    globalApp = app
    
    globalApp.master.unbind("<Key>")
    
    if globalApp.frame:
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, 
            width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
    
    imageCanvas = tk.Canvas(globalApp.frame, 
                         width=globalApp.master.winfo_screenwidth(), 
                         height=globalApp.master.winfo_screenheight(), 
                         bg=globalApp.black, highlightthickness=0)
    imageCanvas.pack()
    
    global imagestimulus
    
    if globalApp.experimentalBlock == 2:
        if globalApp.stimulusPicCounter == 0:
            imagestimulus = ["ANCHOR", "FOX", "RABBIT", "SAILBOAT", "SALTSHAK",
                         "SAW", "SPIDER", "TRAFFICL", "UMBRELLA", "VIOLIN"]
            shuffle(imagestimulus)

    elif globalApp.experimentalBlock == 3:
        if globalApp.stimulusPicCounter == 0:
            imagestimulus = ["ANT", "ARM", "CAT", "FRENCHHO", "FRYINGPA", 
                         "GARBAGEC", "GLASSES", "KANGAROO", "STOVE", "TABLE"] 
            shuffle(imagestimulus)
    elif globalApp.experimentalBlock == 4:
        if globalApp.stimulusPicCounter == 0:
            imagestimulus = ["ACCORDIO", "AIRPLANE", "ARROW", "BABYCARR",  
                         "CAKE", "CATERPIL", "EAGLE", "PIANO", "TRUCK", 
                         "WINEGLAS"]
            shuffle(imagestimulus)
    elif globalApp.experimentalBlock == 5:
        if globalApp.stimulusPicCounter == 0:
            imagestimulus = ["BICYCLE", "BUS", "DUCK", "GRASSHOP", "HEART", 
                         "HORSE", "KETTLE", "SCISSORS", "WAGON", "WINDMILL"]
            shuffle(imagestimulus)
    elif globalApp.experimentalBlock ==6:
        if globalApp.stimulusPicCounter == 0:
            imagestimulus = ["BOTTLE", "BREAD", "CAMEL", "CANDLE", "CHURCH", 
                         "KEY", "LOCK", "MOUNTAIN", "MUSHROOM", "PEACOCK"]
            shuffle(imagestimulus)
    else:
        pass
        
    imagefolder = ""
    if globalApp.experimentalBlock == 2:
        imagefolder = "pics/pb/"
    elif globalApp.experimentalBlock == 3:
        imagefolder = "pics/e1/"    
    elif globalApp.experimentalBlock == 4:
        imagefolder = "pics/e2/"
    elif globalApp.experimentalBlock == 5:
        imagefolder = "pics/e3/"
    elif globalApp.experimentalBlock == 6:
        imagefolder = "pics/e4/"
    else:
        imagefolder = "pics/"
    
    if globalApp.stimulusPicCounter == 9:
        imagestimulus.append(" ")
    
    spic = tk.PhotoImage(file=imagefolder + 
                         imagestimulus[globalApp.stimulusPicCounter] + ".gif")
    piclabel = tk.Label(imageCanvas, image=spic)
    piclabel.config(image=spic) 
    piclabel.image = spic # keep a reference!  
    piclabel.pack()  
    
    imageCanvas.create_window(globalApp.master.winfo_screenwidth()/2, 
                               globalApp.master.winfo_screenheight()/2, 
                               anchor="center", window=piclabel)  
    
    
    
    def rebind(): 
        global timerswitch   
        globalApp.master.bind("<Return>", recognizedStimulus)
        globalApp.master.bind("<space>", notrecognizedStimulus)
        timerswitch = 1
        globalApp.master.after(2500, timedOut)
    
        
    globalApp.master.after(500, rebind)
    

    
def recognizedStimulus(event):
    globalApp.master.unbind("<Return>")
    globalApp.master.unbind("<space>")
    global timerswitch
    timerswitch = 0
    if globalApp.experimentalBlock == 2:
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracypb.append(1)
            globalApp.falsealarmpb.append(0)
        else:
            globalApp.imageaccuracypb.append(0)
            globalApp.falsealarmpb.append(1)
    elif globalApp.experimentalBlock == 3:
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy1.append(1)
            globalApp.falsealarm1.append(0)
        else:
            globalApp.imageaccuracy1.append(0)
            globalApp.falsealarm1.append(1)
            
    elif globalApp.experimentalBlock == 4:
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy2.append(1)
            globalApp.falsealarm2.append(0)
        else:
            globalApp.imageaccuracy2.append(0)
            globalApp.falsealarm2.append(1)
            
    elif globalApp.experimentalBlock == 5:
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy3.append(1)
            globalApp.falsealarm3.append(0)
        else:
            globalApp.imageaccuracy3.append(0)
            globalApp.falsealarm3.append(1)
            
    elif globalApp.experimentalBlock == 6:
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy4.append(1)
            globalApp.falsealarm4.append(0)
        else:
            globalApp.imageaccuracy4.append(0)
            globalApp.falsealarm4.append(1)
    else:
        pass
    
    globalApp.unravel(globalApp)
    globalApp.stimulusPicCounter+= 1
def notrecognizedStimulus(event):
    globalApp.master.unbind("<Return>")
    globalApp.master.unbind("<space>")
    global timerswitch
    timerswitch = 0
    
    if globalApp.experimentalBlock == 2:
        globalApp.falsealarmpb.append(0)
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracypb.append(0)
        else:
            globalApp.imageaccuracypb.append(1)
    elif globalApp.experimentalBlock == 3:
        globalApp.falsealarm1.append(0)
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy1.append(0)
        else:
            globalApp.imageaccuracy1.append(1)
            
    elif globalApp.experimentalBlock == 4:
        globalApp.falsealarm2.append(0)
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy2.append(0)
        else:
            globalApp.imageaccuracy2.append(1)
            
    elif globalApp.experimentalBlock == 5:
        globalApp.falsealarm3.append(0)
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy3.append(0)
        else:
            globalApp.imageaccuracy3.append(1)
            
    elif globalApp.experimentalBlock == 6:
        globalApp.falsealarm4.append(0)
        if imagestimulus[globalApp.stimulusPicCounter] in globalApp.images:
            globalApp.imageaccuracy4.append(0)
        else:
            globalApp.imageaccuracy4.append(1)
    else:
        pass
    
    globalApp.stimulusPicCounter+= 1
    globalApp.unravel(globalApp)

def timedOut():
    global timerswitch
    if timerswitch == 1:
        if globalApp.experimentalBlock == 2:
            globalApp.falsealarmpb.append(0)
            globalApp.imageaccuracypb.append(0)

        elif globalApp.experimentalBlock == 3:
            globalApp.falsealarm1.append(0)
            globalApp.imageaccuracy1.append(0)
                
        elif globalApp.experimentalBlock == 4:
            globalApp.falsealarm2.append(0)
            globalApp.imageaccuracy2.append(0)               

        elif globalApp.experimentalBlock == 5:
            globalApp.falsealarm3.append(0)
            globalApp.imageaccuracy3.append(0)
  
        elif globalApp.experimentalBlock == 6:
            globalApp.imageaccuracy4.append(0)
            globalApp.falsealarm4.append(0)

        else:
            pass
        
        globalApp.master.unbind("<Return>")
        globalApp.master.unbind("<space>")
        globalApp.unravel(globalApp)
        globalApp.stimulusPicCounter+= 1
    else:
        pass