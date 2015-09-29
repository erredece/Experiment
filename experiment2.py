import Tkinter as tk # importing libraries
import unravel as u #importing unravel

black = "#000" # setting colour black

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

    def toggle_geom(self,event): 
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


root = tk.Tk() #Calls the Root frame
root.configure(bg=black) #Root settings, black background 
app=Experiment(root) # Fullscreen
root.overrideredirect(1) # Hides header

u.unravel(root) #Calling the unravel function    

root.mainloop() #Runs root.

    