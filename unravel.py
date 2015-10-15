import Tkinter as tk #Importing Tkinter
from random import randint, choice #Importing random
import score

UnravelFont = ("Helvetica 72 ") #Defining font for unravel
unravelCounter = 0
key = ""
globalApp = None
UnravelStep = 0
stimulus = []
memoryfontleft = []
memoryfontright = []
memorytextleft = []
memorytextright = []
memoryposleft = []
memoryposright = [] 
memorycolourleft = []
memorycolourright = []
numberofruns = 13 #Number of runs - 1
stimulusGenerator = randint(4,8)

def keyIsPressed(event):
    ''' Records the pressed key and calls the unravelBuilder function each time
    the key is pressed, which generates a new layout to then call the
    unravelEngine function'''
    global key
    global UnravelStep
    global unravelCounter
    global globalApp
    global memoryfontleft
    global memoryfontright
    global memoryposleft
    global memoryposright
    global memorytextleft
    global memorytextright
    global memorycolourleft
    global memorycolourright
    global numberofruns
    global stimulusGenerator
    global unravelCounter
    
    key = event.char    
    
    def rebind():
        globalApp.master.bind("<Key>", keyIsPressed)
    
    globalApp.master.unbind("<Key>")
    
    if (unravelCounter <= numberofruns): 
        if globalApp.experimentalBlock == 1:
            globalApp.master.after(250, rebind) 
            unravelBuilder()
        else:
            if unravelCounter % stimulusGenerator == 0:
                unravelEngine()
                unravelCounter -= 1
                UnravelStep -= 1
                globalApp.master.unbind("<Key>")
                globalApp.showPic(globalApp)
                stimulusGenerator = randint(4,8)
            else:
                globalApp.master.after(250, rebind) 
                unravelBuilder()
    
    else:
        unravelEngine()
        score.unravel(globalApp, stimulus)
        UnravelStep = 0
        unravelCounter = 0
        memoryfontleft = []
        memoryfontright = []
        memoryposleft = []
        memoryposright = []
        memorytextleft = []
        memorytextright = []
        memorycolourleft = []
        memorycolourright = []
        if globalApp.experimentalBlock == 3:
            globalApp.data1 = stimulus
        elif globalApp.experimentalBlock == 4:
            globalApp.data2 = stimulus
        elif globalApp.experimentalBlock == 5:
            globalApp.data3 = stimulus
        elif globalApp.experimentalBlock == 6:
            globalApp.data4 = stimulus
        else:
            pass
        globalApp.experimentalBlock += 1            

def unravel(app):
    '''This is the main process function called by the Experiment Class'''
    global globalApp
    globalApp = app
    
    globalApp.master.unbind("<Key>")
    def unlockbind():
        globalApp.master.bind("<Key>", keyIsPressed)
    globalApp.master.after(250, unlockbind)
    unravelBuilder()

def unravelBuilder():
    '''Builds the layout for the UNRAVEL task, as well as storing the values
    into memory so they can then be compared by the unravelEngine function'''
    
    global globalApp
    if globalApp.frame:
        globalApp.Recording = False
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, 
            width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
        
    globalApp.Recording = True
    screen_width = globalApp.master.winfo_screenwidth() #Calculates the screen width
    screen_height = globalApp.master.winfo_screenheight() #Idem, height
           
    top = tk.Canvas(globalApp.frame, width=screen_width/5, 
                    height=screen_height/3+50, 
                    bg=globalApp.black, highlightthickness=0) #Top Canvas      
    top.pack()

    mid = tk.Canvas(globalApp.frame, width=screen_width/5, 
                    height=screen_height/4 - 60 , 
                    bg=globalApp.black, highlightthickness=0) #Mid canvas
    mid.create_rectangle(screen_width/5 - 20, screen_height/4 - 60,
                          10, 10, fill=globalApp.black, 
                          outline= globalApp.white,
                          width=4) #Creates rectangle  

    mid.pack()
    
    bot = tk.Canvas(globalApp.frame, width=screen_width/5, 
                    height=screen_height/3, 
                    bg=globalApp.black, highlightthickness=0)
    bot.pack()
    
    letters = ["A", "B", "U", "X"]
    numbers = ["1", "2", "8", "9"]
    characters = letters + numbers
    positions = [1, 2, 2, 3] #2 is duplicated to have 50% inside the box
    
    positionleft = positions[randint(0, len(positions) - 1)]  
    textleft = characters[randint(0,
                                  len(characters)-1)] #Test for the text in box
    colourleft = choice([globalApp.white, globalApp.white, 
                         globalApp.yellow, globalApp.red])
    fontleft = choice(["", "", "italic", "underline"]) #Duplicated to have 50%
           
    if positionleft == 1: 
        topleft = tk.Label(top, text= textleft,
                    bg=globalApp.black, fg=colourleft, font= 
                    UnravelFont + fontleft,
                    anchor="center") #Top Left char properties
        
        top.create_window(60, screen_height/3, width=80, height=100, 
                          window=topleft, anchor='center') 
   
    elif positionleft == 2:
    
        insideBoxleft = tk.Label(mid, text= textleft,
                            bg=globalApp.black, fg=colourleft, font= 
                            UnravelFont + fontleft,
                            anchor="center") #Box Left char properties    
        
        
        mid.create_window(60, 70, width=80, height=100, 
                          window=insideBoxleft, 
                          anchor='center') #Left char window
    else: 
        
        botleft = tk.Label(bot, text= textleft,
                           bg=globalApp.black, fg=colourleft, font=
                           UnravelFont + fontleft,
                           anchor="center") #Bot left char properties
        
        bot.create_window(60, 50, width=80, height=100,
                          window=botleft, anchor="center")
    
    if positionleft != 2:
        positionright = 2
    else:
        positionright = choice([1,3])

    if textleft in letters:
        textright = numbers[randint(0, len(numbers)-1)]
    else:
        textright = letters[randint(0, len(letters)-1)]  
          
    if colourleft != globalApp.white:
        colourright = globalApp.white   
    else:
        colourright = choice([globalApp.red, globalApp.yellow])   
        
    if fontleft != "":
        fontright = ""
    else:
        fontright = choice(["underline", "italic"])
       
     
    if positionright == 1:
        
        topright = tk.Label(top, text = textright, bg=globalApp.black,
                            fg=colourright, font = UnravelFont + 
                            fontright, anchor ="center") #Top right properties
        
        top.create_window(screen_width/5-80, screen_height/3, width=80,
                          height=100, window=topright, anchor="center")  
    elif positionright == 2:
         
        insideBoxright = tk.Label(mid, text = textright, 
                            bg=globalApp.black, fg=colourright, font= 
                            UnravelFont + fontright,
                            anchor="center") #Right char properties
    
        mid.create_window(screen_width/5-80, 70, width=80, 
                          height=100, window=insideBoxright,
                          anchor="center") #Right char window
        
    else:
        botright = tk.Label(bot, text = textright, bg=globalApp.black,
                            fg=colourright, font= UnravelFont + 
                            fontright, anchor= "center")
        
        bot.create_window(screen_width/5-80, 50, width=80, height=100,
                          window=botright, anchor="center")

    unravelEngine()
    
    global memoryfontleft
    global memoryfontright
    global memoryposleft
    global memoryposright
    global memorytextleft
    global memorytextright
    global memorycolourleft
    global memorycolourright
    memoryfontleft.append(fontleft)
    memoryfontright.append(fontright)
    memoryposleft.append(positionleft)
    memoryposright.append(positionright)
    memorytextleft.append(textleft)
    memorytextright.append(textright)
    memorycolourleft.append(colourleft)
    memorycolourright.append(colourright)   

def unravelEngine():
    ''' Compares all the key inputs to the values present on screen, recording
    the responses as correct or not and moves to the next step. If the person
    presses a key from a different step, it will also move to the step
    following the one the participant thought s/he was'''
    global key
    global unravelCounter
    global UnravelStep
    global stimulus
    global memoryfontleft
    global memoryfontright
    global memoryposleft
    global memoryposright
    global memorytextleft
    global memorytextright
    global memorycolourleft
    global memorycolourright
    
    if key == "u":
        if UnravelStep == 1: 
            if memoryfontleft[unravelCounter - 1] == "underline":
                stimulus.append(1)
            elif memoryfontright[unravelCounter - 1] == "underline":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 2
    elif key =="i":
        if UnravelStep == 1:
            if memoryfontleft[unravelCounter - 1] == "italic":
                stimulus.append(1)
            elif memoryfontright[unravelCounter - 1] == "italic":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 2
    elif key == "n":
        if UnravelStep == 2:
            if memorytextleft[unravelCounter -1] == "A":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "B":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "A":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "B":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 3
    elif key == "f":
        if UnravelStep == 2:
            if memorytextleft[unravelCounter -1] == "U":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "X":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "U":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "X":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 3
    elif key == "r":
        if UnravelStep == 3:
            if memorycolourleft[unravelCounter - 1] == globalApp.red: 
                stimulus.append(1)
            elif memorycolourright[unravelCounter - 1] == globalApp.red: 
                stimulus.append(1)   
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 4
    elif key == "y":
        if UnravelStep == 3:
            if memorycolourleft[unravelCounter - 1] == globalApp.yellow: 
                stimulus.append(1)
            elif memorycolourright[unravelCounter - 1] == globalApp.yellow: 
                stimulus.append(1)   
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 4
    elif key == "a":
        if UnravelStep == 4:
            if memoryposleft[unravelCounter - 1] == 1:
                stimulus.append(1)
            elif memoryposright[unravelCounter - 1] == 1:
                stimulus.append(1)
            else:
                stimulus.append(0)
        else: 
            stimulus.append(0)
        UnravelStep = 5
    elif key == "b":
        if UnravelStep == 4:
            if memoryposleft[unravelCounter - 1] == 3:
                stimulus.append(1)
            elif memoryposright[unravelCounter - 1] == 3:
                stimulus.append(1)
            else:
                stimulus.append(0)
        else: 
            stimulus.append(0)
        UnravelStep = 5
    elif key == "v":
        if UnravelStep == 5:
            if memorytextleft[unravelCounter -1] == "A":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "U":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "A":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "U":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 6
    elif key == "c":
        if UnravelStep == 5:
            if memorytextleft[unravelCounter -1] == "B":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "X":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "B":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "X":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 6
    elif key == "e":
        if UnravelStep == 6:
            if memorytextleft[unravelCounter -1] == "2":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "8":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "2":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "8":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 7
    elif key == "o":
        if UnravelStep == 6:
            if memorytextleft[unravelCounter -1] == "1":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "9":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "1":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "9":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 7
            
    elif key == "l":
        if UnravelStep == 7:
            if memorytextleft[unravelCounter -1] == "1":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "2":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "1":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "2":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 1
    elif key == "m":
        if UnravelStep == 7:
            if memorytextleft[unravelCounter -1] == "8":
                stimulus.append(1)
            elif memorytextleft[unravelCounter -1] == "9":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "8":
                stimulus.append(1)
            elif memorytextright[unravelCounter -1] == "9":
                stimulus.append(1)
            else:
                stimulus.append(0)
        else:
            stimulus.append(0)
        UnravelStep = 1
    else:
        stimulus.append(0)
        if UnravelStep < 7:
            UnravelStep += 1
        else:
            UnravelStep = 1
    if unravelCounter == 0:
        stimulus = []
        
    unravelCounter += 1
    print stimulus
    print unravelCounter
    print UnravelStep