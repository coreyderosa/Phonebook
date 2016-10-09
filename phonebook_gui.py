#Python Version: 3.5.2
#
#Author:                Corey DeROsa
#
#Purpose:             Create a phone book app that allows the user to add entries as well as retrieve entries
#
#Python Course:   Items 49-51
#
#creating the phonebook_gui module to be imprted into the phonebook_main module

from tkinter import *
import tkinter as ttk

#Importing other phonebook modules
import phonebook_main
import phonebook_func


def load_gui(self):
    #setting up gui labels
    self.lbl_fname = ttk.Label(self.master, text = 'First Name: ')
    self.lbl_fname.grid(row = 0, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
    self.lbl_lname = ttk.Label(self.master, text = 'Last Name: ')
    self.lbl_lname.grid(row = 2, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
    self.lbl_phone = ttk.Label(self.master, text = 'Phone: ')
    self.lbl_phone.grid(row = 4, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
    self.lbl_email = ttk.Label(self.master, text = 'Email: ')
    self.lbl_email.grid(row = 6, column = 0, padx = (27,0), pady = (10,0), sticky = 'nw')
    self.lbl_user = ttk.Label(self.master, text = 'User: ')
    self.lbl_user.grid(row = 0, column = 2, padx = (0,0), pady = (10,0), sticky = 'nw')
    #setting up gui entry fields
    self.txt_fname = ttk.Entry(self.master, text = '')
    self.txt_fname.grid(row = 1, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
    self.txt_lname = ttk.Entry(self.master, text = '')
    self.txt_lname.grid(row = 3, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
    self.txt_phone = ttk.Entry(self.master, text = '')
    self.txt_phone.grid(row = 5, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
    self.txt_email = ttk.Entry(self.master, text = '')
    self.txt_email.grid(row = 7, column = 0, columnspan = 2, padx = (30,40), pady = (0,0), sticky = 'new')
    #setting up listbox and the scrollbar
    self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection = 0, yscrollcommand = self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect(self, event))
    self.scrollbar1.config(command = self.lstList1.yview)
    self.scrollbar1.grid(row = 1, column = 5, rowspan = 7, sticky = 'nes')
    self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')
    #setting up buttons
    self.btn_add = ttk.Button(self.master, width = 12, height = 2, text = 'Add', command = lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row = 8, column = 0, padx = (25,0), pady = (45,10), sticky = 'w')
    self.btn_update = ttk.Button(self.master, width = 12, height = 2, text = 'Update', command = lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row = 8, column = 1, padx = (15,0), pady = (45,10), sticky = 'w')
    self.btn_delete = ttk.Button(self.master, width = 12, height = 2, text = 'Delete', command = lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row = 8, column = 2, padx = (15,0), pady = (45,10), sticky = 'w')
    self.btn_close = ttk.Button(self.master, width = 12, height = 2, text = 'Close', command = lambda: phonebook_func.ask_quit(self))
    self.btn_close.grid(row = 8, column = 4, padx = (15,0), pady = (45,10), sticky = 'e')
    
