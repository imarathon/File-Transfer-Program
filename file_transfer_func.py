#   Python Ver: 3.5.6
#   Author:     Anibal Huilca
#   Purpose:    Create a phonebook using Tkinter


import os
from os import path
import glob
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import time
import datetime
from datetime import datetime
import sqlite3
import file_transfer_main
import file_transfer_gui

archived_ctr = 0
ready_to_archive_ctr = 0

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo  = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program","Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def source_folder(self):
    self.listbox.delete(0,END)
    self.txt_source_folder.delete(0,END)
    global folder
    folder = filedialog.askdirectory(parent=self.master,initialdir="/")
    self.txt_source_folder.insert(0,str(folder))
    
    if len(folder) > 0:
        x = os.listdir(folder)
        for i in x:
            self.listbox.insert(END, i)
    
    if self.listbox.size() == 0:
        empty = ("This directory is empty")
        self.listbox.insert(END, empty)
    
def dest_folder(self):
    self.listbox1.delete(0, END)
    self.txt_dest_folder.delete(0, END)
    global folder1
    folder1 = filedialog.askdirectory(parent=self.master,initialdir="/")
    self.txt_dest_folder.insert(0,str(folder1))

    if len(folder1) > 0:
        self.listbox1.insert(END)
        x = os.listdir(folder1)
        for i in x:
            self.listbox1.insert(END, i)

    if self.listbox1.size() == 0:
        empty = ("This directory is empty.")
        self.listbox1.insert(0, str(empty))
  
def update_list(self):
    self.listbox.delete(0, END)
    self.listbox1.delete(0, END)
    self.listbox2.delete(0, END)
        
    if len(folder) > 0:
        self.listbox.insert(END)
        x = os.listdir(folder)
        for i in x:
            self.listbox.insert(END, i)

    if len(folder1) > 0:
        self.listbox1.insert(END)
        x = os.listdir(folder1)
        for i in x:
            self.listbox1.insert(END, i)

    if (archived_ctr) > 0:
        done = ("%s file(s) have been moved to your destination folder." %archived_ctr)
        self.listbox2.insert(END, done)          
    
def clear_items(self):
    self.listbox.delete(0, END)
    self.listbox1.delete(0,END)
    self.listbox2.delete(0, END)
    self.txt_source_folder.delete(0,END)
    self.txt_dest_folder.delete(0,END)
    global archived_ctr
    global ready_to_archive_ctr
    archived_ctr = 0
    ready_to_archive_ctr = 0
    folder = None
    folder1 = None

def file_has_changed(fname):
    global file_m_time
    file_m_time = datetime.fromtimestamp(path.getmtime(fname))
    td = datetime.now() - file_m_time

    if td.days == 0:
        global ready_to_archive_ctr
        ready_to_archive_ctr = ready_to_archive_ctr + 1
        return True
    else: return False

def onclick(self):
    try:
        folder and folder1
    except NameError:
        messagebox.showinfo("Select Folder", "Please select a Source and Destination folder.")
    else:
        check_files(self)
    
def check_files(self):
    self.listbox2.delete(0, END)
    ready = ("The file(s) below have been modified in the last 24 hours.")
    self.listbox2.insert(0, str(ready))

    for fname in os.listdir(folder):
        src_fname = '%s\%s' % (folder, fname)
        
        if file_has_changed(src_fname):
            dst_fname = '%s\%s' % (folder1, fname)
            form_file_time = (file_m_time.strftime("%I:%M %p"))
            month_file_time = (file_m_time.strftime("%B %d, %Y"))
            show = 'File: %s, was modifed at %s on %s.' % (fname,form_file_time,month_file_time)
            self.listbox2.insert(END,show)
     
    if ready_to_archive_ctr == 0:
        self.listbox2.delete(0, END)
        done1 = ("0 file(s) have been modifited in the last 24 hours.")
        self.listbox2.insert(END, done1)
        
def move_files(self):
    global archived_ctr
    try:
        folder and folder1
    except NameError:
        messagebox.showinfo("Select Folder", "Please select a Source and Destination folder.")
    else:   
        for fname in os.listdir(folder):
            src_fname = '%s\%s' % (folder, fname)
                
            if file_has_changed(src_fname):    
              dst_fname = '%s\%s' % (folder1, fname)
             
              try:
                shutil.move(src_fname, folder1)
                archived_ctr = archived_ctr + 1
                update_list(self)
              except IOError as e:
                print ('could not open the file: %s ' % e)
        clicklog(self)
#===============================================================================
def create_db(self):
    conn = sqlite3.connect('file_transfer_log.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_file_transfer_log( \
            ID INTEGER PRIMARY KEY, \
            col_date TEXT, \
            col_time TEXT, \
            col_dtime TEXT \
            );")
        conn.commit()

def clicklog(self):
    date = time.strftime('%b %d, %Y')
    timenow = time.strftime('%I:%M %p')
    dtime = ("{} {}".format(date,timenow))
    data = (timenow,date,dtime)
    conn = sqlite3.connect('file_transfer_log.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO tbl_file_transfer_log (col_date,col_time, col_dtime) VALUES (?,?,?)""", (data))
        conn.commit()
    conn.close()
    shwtmstmp(self)
    
def shwtmstmp(self):
    conn = sqlite3.connect('file_transfer_log.db')
    c = conn.cursor()
    c.execute("SELECT col_dtime FROM tbl_file_transfer_log ORDER BY ID DESC")
    timestmp = (c.fetchone()[0])
    messagebox.showinfo("Last File Check", " The last file check was done on: " + timestmp)
    conn.close()
    
if __name__ == "__main__":
    pass                                                                                          
