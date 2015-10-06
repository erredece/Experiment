import Tkinter as tk #Importing Tkinter
from random import randint, choice

UnravelFont = ("Helvetica 72 ") #Defining font for unravel
unravelCounter = 1
key = ""
globalApp = None

def keyIsPressed(event):
    global key
    key = event.char
    
    global unravelCounter
    if (unravelCounter <= 10):
        unravelEngine()
        
    else:
        unravelCounter = 1
        globalApp.unravelIntro(globalApp)

def unravel(app):
    global globalApp
    globalApp = app
    
    globalApp.master.bind("<Key>", keyIsPressed)
    unravelEngine()
    
def unravelEngine():
    
    global globalApp
    if globalApp.frame:
        globalApp.Recording = False
        globalApp.frame.destroy()
        globalApp.frame = tk.Frame(globalApp.master, width=globalApp.master.winfo_screenwidth(), 
            height=globalApp.master.winfo_screenheight())
        globalApp.frame.pack()
        
    globalApp.Recording = True
    screen_width = globalApp.master.winfo_screenwidth() #Calculates the screen width
    screen_height = globalApp.master.winfo_screenheight() #Idem, height
           
    top = tk.Canvas(globalApp.frame, width=screen_width/5, height=screen_height/3+50, 
                    bg=globalApp.black, highlightthickness=0) #Top Canvas      
    top.pack()

    mid = tk.Canvas(globalApp.frame, width=screen_width/5, height=screen_height/4 - 60 , 
                    bg=globalApp.black, highlightthickness=0) #Mid canvas
    mid.create_rectangle(screen_width/5 - 20, screen_height/4 - 60,
                          10, 10, fill=globalApp.black, outline= globalApp.white,
                          width=4) #Creates rectangle  

    mid.pack()
    
    bot = tk.Canvas(globalApp.frame, width=screen_width/5, height=screen_height/3, 
                    bg=globalApp.black, highlightthickness=0)
    bot.pack()
    
    letters = ["A", "B", "U", "X"]
    numbers = ["1", "2", "8", "9"]
    characters = letters + numbers
    positions = [1, 2, 2, 3] #2 is duplicated to have 50% inside the box
    
    positionleft = positions[randint(0, len(positions)-1)]  
    textleft = characters[randint(0,
                                  len(characters)-1)] #Test for the text in box
    colourleft = choice([globalApp.white, globalApp.white, globalApp.yellow, globalApp.red])
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

    global key
    if key.lower() == "w":
        print "blaw blaw blaw"
    elif key.lower() == "a":
        print "blaha blaha blaha"
    elif key.lower() == "s":
        print "blash blash blash"
    elif key.lower() == "d":
        print "blad blad blad"
    else:
        print key

    global unravelCounter
    unravelCounter += 1

    '''if globalApp.unravelCounter <= 10:
        globalApp.master.bind("<Key>", unravelEngine)
    else:
        globalApp.unravelCounter = 1
        globalApp.master.bind("<Key>", globalApp.unravelIntro)'''