import Tkinter as tk # importing libraries
import unravel as u #importing unravel
import intro as i
import unravelIntro as ui
import PictureList as pic


class Experiment: # Defining Fullscreen function.    
    def __init__(self, master, **kwargs):
        
        self.master=master
        pad=0
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<F1>',self.toggle_geom)     # This sets the key to toggle 
# out and in of the fullscreen, so it is possible to close the experiment in
# case of any technical issue.

        self.frame = tk.Frame(self.master, width=self.master.winfo_screenwidth(), 
            height=self.master.winfo_screenheight(), bg=self.black)
        self.frame.pack()  
    
    black = "#000" #Defining black
    white = "#fff" #Defining white
    red = "#f00" #Defining red
    yellow = "#ff0" #Defining yellow

    Recording = False
    stimulus = []

    def toggle_geom(self,event): 
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def intro(self):
        i.intro(self)
        
    def unravelIntro(self, event):
        ui.intro(self)
        print "Yo" 
    
    def unravel(self, event):
        u.unravel(self) # Calling the unravel function

    def keyRecord(self, event):
        self.stimulus = event.char
        print "You just pressed " + str(self.stimulus)   
    
    def PictureList(self):
        pic.PictureList(self)
    

            
    
    unravelCounter = 1

root = tk.Tk() #Calls the Root frame
app=Experiment(root) # Fullscreen
root.configure(bg=app.black, cursor="none") #Root settings, black background
root.overrideredirect(1) # Hides header

app.PictureList()
#app.intro()
app.Recording = False
#root.bind("<Key>", app.unravel)

root.mainloop() #Runs root
