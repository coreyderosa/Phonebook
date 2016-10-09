#Python Version: 3.5.2
#
#Author:                Corey DeROsa
#
#Purpose:             Create a phone book app that allows the user to add entries as well as retrieve entries
#
#Python Course:   Items 49-51
#
#creating the phonebook_func module to be imprted into the phonebook_main module

#importing required modules to close program, tkinter, and sqltie3 db
import os
from tkinter import *
import tkinter as tk
import sqlite3


#Importing other phonebook modules
import phonebook_main
import phonebook_gui

def center_window(self, w, h): #w, h are referenced in our phonebook_main module.  We tell the program to make w=500 and h = 300
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    #will get the the midway point of the height and width of user's screen to place the phonebook gui at that midway point
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo #returns the center position of the user's screen

#function for when the user clicks the 'X' in upper right corner to close the program
def ask_quit(self):
    if messagebox.askokcancel('Exit Program', 'Okay to exit application?'):
        self.master.destroy()
        os._exit(0) #this helps clear the memory this program takes up in the users RAM

#this function will create our phonebook database
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        conn.commit() #must commit() to save changes to the db
    conn.close() #closing the db connection
    first_run(self)

#creating data for our db
def first_run(self):
    data = ('John', 'Doe', 'John Doe', '555-555-5555', 'jdoe@email.com') #tuple
    conn = sqlite3.connect('phonebook.db') #connecting to the db
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1: #if count is 0 then execute the INSERT INTO function into the db
            cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES(?,?,?,?,?)""", (data))
            conn.commit()
        conn.close()
                        
                
def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur, count

#Select item in ListBox
def onSelect(self, event):
    #calling the even is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        #This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #clean up the data
    var_fname = var_fname.strip() #this will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip() 
    var_fname = var_fname.title() #this will capitalize the first letter
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname)) #this is like a concat
    print ('var_fullname: {}'.format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not '@' or not '.' in var_email: #email validation
        print('Incorrect email format...')
    if (len(var_fname) > 0 and len(var_lname) > 0 and len(var_phone) > 0 and len(var_email) > 0): #requires the user to input something
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            #Checks the db for duplicate fullname
            #counts the number of fullnames in the db that are the same as the user's current input
            cursor.execute("""SELECT COUNT(col_fname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: #if the number of fullnames that match the user's current input = 0 then db will allow the user's input to be stored
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook(col_fname, col_lname, col_fullname, col_phone, col_email) VALUES(?,?,?,?,?)""", (data))
                self.lstList1.insert(END, var_fullname) #updates teh listbox with the new fullname
                onClear(self) #clears all the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists. Please choose a different name".format(var_fullname))
                onClear(self) #clears all textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Missing Text Error','Please ensure there is data in all fields.')


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel('Delete Confirmation', 'All info associated with, ({}) \nwill be permanently deleted. \n\nProceed with the deletion request?'.format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #clears textboxes and data user wants to delete from db
######      onRefresh(self)
                conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted. \n\nPlease add another record before you delete ({}).".format(var_select))
    conn.close()

def onDeleted(self):
    #delete info in the textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##    onRefresh(self)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    #clears the textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onRefresh(self):
    #populate the listbox
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0, str(item))
    conn.close

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]
        var_value = self.lstList1.get(var_select)
    except:
        messagebox.showinfo('Missing selection','No name was selected from the list. \nCancelling the Update request.')
        return
    #the user will only be able to update changes to the phone and email
    #for name changes, the user will need to delete the entire record
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and len(var_email) > 0: #validates there is info in phone and email textboxes
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT Count(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print (count)
            cur.execute("""SELECT Count(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print (count2)
            if count == 0 or count2 == 0: #if the search for duplicate comes up with nothing then run the following
                response = messagebox.askokcancel('Update Request', 'The following changes ({}) and ({}) will be implemented for ({}).')
                print (response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute('''UPDATE tbl_phonebook SET col_phone = '{0}', col_email = '{1}' WHERE col_fullname = '{2}'''.format(var_phone, var_email))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo('Cancel request', 'No changes have been made to ({}).'.format(var_value))
            else:
                messagebox.showinfor('No changes detected', 'Both ({}) and ({}) \nalready exist in the database for this name.')
            onClear(self)
        conn.close()
    else:
        messagebox.showerror('Missing Info', 'Please select a name from the list \nthen edit the phone or email info.')
    onClear(self)

if __name__ == '__main__':
    pass
                                                  
            
        







                
                

















        
                        


