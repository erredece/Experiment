'''Programme by Roberto de Cecilio (erredece), September-November 2015, as part  
of his senior project.

Thanks to 5unken, foleranser, Marc Sances and Gabboman for all their help on 
developing this code. 

This programme is prepared to run on Python 2.7, it will required some changes
in order to run on Python 3.

Modifications are allowed to be made on all the programme in order to adapt it
to other experiments or improve the code, just credit the previous author(s) for
the original scripts.
'''

'''Importing libraries'''
import Tkinter as tk 
import time
from random import shuffle
'''Importing the other scripts from the programme'''
import unravel as u #importing unravel
import demographics as demo
import intro as i
import unravelIntro as ui
import PictureList as pic
import outro as out
import showPic as sp

class Experiment: # Defining the Main class of the experiment.
        
    def __init__(self, master, **kwargs):
        '''Initializing function'''
        
        self.master = master
        self._geom = '1000x500+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<F1>', self.toggle_geom)#This toggles F1 screen size change 
        self.frame = tk.Frame(self.master, 
                              width=self.master.winfo_screenwidth(), 
                              height=self.master.winfo_screenheight(), 
                              bg=self.black)
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
        
    '''This sets a clock to use on the timed parts of the experiment'''
    start = time.time()
    elapsedTime = 0
    def getElapsedTime(self):
        self.elapsedTime += 1
        self.master.after(1000, self.getElapsedTime)
    
    '''Adding the other scripts so they can be accessed on the whole exp'''
        
    def demographics(self):
        demo.demographics(self)

    def intro(self):
        i.intro(self)
        
    def unravelIntro(self, event):
        ui.intro(self) 
        
    def unravel(self, event):
        u.unravel(self) # Calling the unravel function
    
    def PictureList(self, event):
        pic.PictureList(self)
    
    def showPic(self, event):
        sp.showPic(self)    
        
    def outro(self, event):
        out.outro(self)
    
    '''Global variables'''    
    gender = 0
    age = 0
    ID = 0   
    experimentalBlock = 1
    variable = ["control", "90", "180", "mix"]
    shuffle(variable)
    print variable
    phasecounter = 0
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
globalApp=Experiment(root) # Initializing the root
root.configure(bg=globalApp.black, cursor="none") #Hides mouse, black bg
root.overrideredirect(1) # Hides header
globalApp.demographics()
root.mainloop() #Runs root