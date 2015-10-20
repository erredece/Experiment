import Tkinter as tk # importing Tkinter, change for tkinter when using Python 3
import unravel as u #importing unravel
import demographics as demo
import intro as i
import unravelIntro as ui
import PictureList as pic
import outro as out
import showPic as sp
import time


class Experiment: # Defining Fullscreen function.
        
    def __init__(self, master, **kwargs):
        '''Initializing function'''
        
        '''DEBUGGING F1 TOGGLE, DELETE THIS LINE AND THE LINE AFTER THE CODE 
        TO ACTIVATE
        
        This sets the key to toggle 
        out and in of the fullscreen, so it is possible to close the experiment 
        in case of any technical issue.'''
        self.master = master
        self._geom = '1000x500+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<F1>', self.toggle_geom)     # 
        self.frame = tk.Frame(self.master, 
                              width=self.master.winfo_screenwidth(), 
                              height=self.master.winfo_screenheight(), 
                              bg=self.black)
        self.frame.pack()  
        
        '''DELETE THIS LINE TOO FOR ACTIVATING THE F1 DEBUG'''
    
    black = "#000" #Defining black
    white = "#fff" #Defining white
    red = "#f00" #Defining red
    yellow = "#ff0" #Defining yellow

    def toggle_geom(self,event): 
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
        
    def demographics(self):
        demo.demographics(self)

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
        self.elapsedTime += 1
        self.master.after(1000, self.getElapsedTime)
    
    def PictureList(self, event):
        pic.PictureList(self)
    
    def showPic(self, event):
        sp.showPic(self)    
        
    def outro(self, event):
        out.outro(self)
        
    gender = 0
    age = 0
    ID = 0
        
    experimentalBlock = 1
    
    images = []
    
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    
    pdata1 = 0
    pdata2 = 0
    pdata3 = 0
    pdata4 = 0
    
    imageaccuracypb = []
    falsealarmpb = []
    imageaccuracy1 = []
    falsealarm1 = []
    imageaccuracy2 = []
    falsealarm2 = []
    imageaccuracy3 = []
    falsealarm3 = []
    imageaccuracy4 = []
    falsealarm4 = []
    
    stimulusPicCounter = 0

root = tk.Tk() #Calls the Root frame
globalApp=Experiment(root) # Fullscreen
root.configure(bg=globalApp.black, cursor="none") #Root settings, black background
root.overrideredirect(1) # Hides header

#globalApp.PictureList()
globalApp.demographics()

root.mainloop() #Runs root
