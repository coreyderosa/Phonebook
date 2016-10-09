#Python Version: 3.5.2
#
#Author:                Corey DeROsa
#
#Purpose:             Create a phone book app that allows the user to add entries as well as retrieve entries
#
#Python Course:   Items 49-51

from tkinter import *
import tkinter as tk

#Importing my other modules needed to run the phone book
import phonebook_gui
import phonebook_func

#Setting up the class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define the master frame config
        self.master = master
        self.master.minsize(500, 300) #height, width
        self.master.maxsize(500, 300)
        phonebook_func.center_window(self, 500, 300) #center_window will center the GUI window in the center of the screen
        self.master.title('The Tkinter Phonebook')
        self.master.configure(bg='white') #bg = background
        #WM_DELETE_WINDOW is 'X' in upper corner of window that closes window
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master
        phonebook_gui.load_gui(self) #calls the load_gui function from the phonebook_gui file


if __name__== '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
