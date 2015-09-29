import Tkinter as tk #Importing Tkinter
from random import randint, choice

UnravelFont = ("Helvetica 72 ") #Defining font for unravel

def unravel(app):
    root = app.master
    def unravelEngine(self):
            
        if app.frame:
            app.Recording = False
            app.frame.destroy()
            app.frame = tk.Frame(app.master, width=app.master.winfo_screenwidth(), 
                height=app.master.winfo_screenheight())
            app.frame.pack()
            
        app.Recording = True
        screen_width = root.winfo_screenwidth() #Calculates the screen width
        screen_height = root.winfo_screenheight() #Idem, height
               
        top = tk.Canvas(app.frame, width=screen_width/5, height=screen_height/3+50, 
                        bg=app.black, highlightthickness=0) #Top Canvas      
        top.pack()
    
        mid = tk.Canvas(app.frame, width=screen_width/5, height=screen_height/4 - 60 , 
                        bg=app.black, highlightthickness=0) #Mid canvas
        mid.create_rectangle(screen_width/5 - 20, screen_height/4 - 60,
                              10, 10, fill=app.black, outline= app.white,
                              width=4) #Creates rectangle  
    
        mid.pack()
        
        bot = tk.Canvas(app.frame, width=screen_width/5, height=screen_height/3, 
                        bg=app.black, highlightthickness=0)
        bot.pack()
        
        letters = ["A", "B", "U", "X"]
        numbers = ["1", "2", "8", "9"]
        characters = letters + numbers
        positions = [1, 2, 2, 3] #2 is duplicated to have 50% inside the box
        
        positionleft = positions[randint(0, len(positions)-1)]  
        textleft = characters[randint(0,
                                      len(characters)-1)] #Test for the text in box
        colourleft = choice([app.white, app.white, app.yellow, app.red])
        fontleft = choice(["", "", "italic", "underline"]) #Duplicated to have 50%
               
        if positionleft == 1: 
            topleft = tk.Label(top, text= textleft,
                        bg=app.black, fg=colourleft, font= 
                        UnravelFont + fontleft,
                        anchor="center") #Top Left char properties
            
            top.create_window(60, screen_height/3, width=80, height=100, 
                              window=topleft, anchor='center') 
       
        elif positionleft == 2:
        
            insideBoxleft = tk.Label(mid, text= textleft,
                                bg=app.black, fg=colourleft, font= 
                                UnravelFont + fontleft,
                                anchor="center") #Box Left char properties    
            
            
            mid.create_window(60, 70, width=80, height=100, 
                              window=insideBoxleft, 
                              anchor='center') #Left char window
        else: 
            
            botleft = tk.Label(bot, text= textleft,
                               bg=app.black, fg=colourleft, font=
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
              
        if colourleft != app.white:
            colourright = app.white   
        else:
            colourright = choice([app.red, app.yellow])   
            
        if fontleft != "":
            fontright = ""
        else:
            fontright = choice(["underline", "italic"])
           
         
        if positionright == 1:
            
            topright = tk.Label(top, text = textright, bg=app.black,
                                fg=colourright, font = UnravelFont + 
                                fontright, anchor ="center") #Top right properties
            
            top.create_window(screen_width/5-80, screen_height/3, width=80,
                              height=100, window=topright, anchor="center")  
        elif positionright == 2:
             
            insideBoxright = tk.Label(mid, text = textright, 
                                bg=app.black, fg=colourright, font= 
                                UnravelFont + fontright,
                                anchor="center") #Right char properties
        
            mid.create_window(screen_width/5-80, 70, width=80, 
                              height=100, window=insideBoxright,
                              anchor="center") #Right char window
            
        else:
            botright = tk.Label(bot, text = textright, bg=app.black,
                                fg=colourright, font= UnravelFont + 
                                fontright, anchor= "center")
            
            bot.create_window(screen_width/5-80, 50, width=80, height=100,
                              window=botright, anchor="center")
    root.bind("<a>", unravelEngine)