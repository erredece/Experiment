import Tkinter as tk # importing Tkinter, change for tkinter when using Python 3
import unravel as u #importing unravel
import intro as i
import unravelIntro as ui
import PictureList as pic
import time


class Experiment: # Defining Fullscreen function.    
    def __init__(self, master, **kwargs):
        '''Initializing function'''
        self.master = master
        pad = 0
        self._geom = '1000x500+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<F1>', self.toggle_geom)     # This sets the key to toggle 
# out and in of the fullscreen, so it is possible to close the experiment in
# case of any technical issue.

        self.frame = tk.Frame(self.master, width=self.master.winfo_screenwidth(), 
            height=self.master.winfo_screenheight(), bg=self.black)
        self.frame.pack()  
    
    black = "#000" #Defining black
    white = "#fff" #Defining white
    red = "#f00" #Defining red
    yellow = "#ff0" #Defining yellow

    def toggle_geom(self,event): 
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def intro(self):
        i.intro(self)
        
    def unravelIntro(self, event):
        ui.intro(self) 
    
    def unravel(self, event):
        u.unravel(self) # Calling the unravel function

    '''This sets a clock to use on the timed parts of the experiment'''
    start = time.time()
    elapsedTime = 0
    def getElapsedTime(self):
        print "called"
        self.elapsedTime += 1
        self.master.after(1000, self.getElapsedTime)
    
    def PictureList(self):
        pic.PictureList(self)

root = tk.Tk() #Calls the Root frame
globalApp=Experiment(root) # Fullscreen
root.configure(bg=globalApp.black, cursor="none") #Root settings, black background
root.overrideredirect(1) # Hides header

#globalApp.PictureList()
globalApp.intro()

#root.bind("<Key>", globalApp.unravel)

root.mainloop() #Runs root
