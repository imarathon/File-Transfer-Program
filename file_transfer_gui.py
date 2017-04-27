#   Python Ver: 3.5.6
#   Author:     Anibal Huilca
#   Purpose:    Create a file transfer program using Tkinter

from tkinter import *
import tkinter as tk
import time

import file_transfer_main
import file_transfer_func

def load_gui(self):
    
    self.source_button = tk.Button(self.master,command = lambda: file_transfer_func.source_folder(self),
                                   text = 'Source Folder')
    self.source_button.grid(row=0, column=0,padx=(20,0),pady=(15,3),sticky = W)

    self.check_button = tk.Button(self.master,command = lambda: file_transfer_func.onclick(self),
                                  text = 'Check Files')
    self.check_button.grid(row=2, column=1,padx=(5,5),sticky = N)    

    self.move_button = tk.Button(self.master,command = lambda: file_transfer_func.move_files(self),
                                 text = 'Move Files')
    self.move_button.grid(row=2, column=1,padx=(5,5))

    self.clear_button = tk.Button(self.master,command = lambda: file_transfer_func.clear_items(self),
                                  text = 'Clear Items')
    self.clear_button.grid(row=2, column=1,padx=(5,5),sticky = S)

    self.destination_button = tk.Button(self.master,command = lambda: file_transfer_func.dest_folder(self),
                                        text = 'Destination Folder')
    self.destination_button.grid(row=0, column=3,padx=(0,0),pady=(15,3),sticky = W)

    self.lbl_source = tk.Label(self.master,text='Source Folder Address:')
    self.lbl_source.grid(row=10,column=0,padx=(20,0),pady=(15,0),sticky=W)

    self.txt_source_folder = tk.Entry(self.master,text='')
    self.txt_source_folder.grid(row=11,column=0, rowspan=1,columnspan=1,padx=(20,17),sticky=W+E)

    self.lbl_dest = tk.Label(self.master,text='Destination Folder Address:')
    self.lbl_dest.grid(row=10,column=3,padx=(0,0),pady=(15,0),sticky=W)
                            
    self.txt_dest_folder = tk.Entry(self.master,text='')
    self.txt_dest_folder.grid(row=11,column=3, rowspan=1,columnspan=1,padx=(0,40),sticky=W+E)

    self.txt_results = tk.Label(self.master,text='File Transfer Program Activity:')
    self.txt_results.grid(row=12,column=0,padx=(20,0),pady=(15,0),sticky=W)

    que_hora = ("Today is: " + time.strftime('%b %d, %Y %I:%M %p'))
    self.txt_time = tk.Label(self.master,text=str(que_hora))
    self.txt_time.grid(row=12,column=3,padx=(0,0),pady=(15,0),sticky=W)

    self.listbox = tk.Listbox(self.master, width = 40, height = 10)
    self.listbox.grid(row=2,column=0, padx=(20,17),pady=(0,0),sticky=(N, W, E, S))

    self.scrollbar = Scrollbar(self.master, orient=VERTICAL)
    self.scrollbar.config(command=self.listbox.yview)
    self.scrollbar.grid(row=2,column=0, padx=(0,0),pady=(0,0),sticky=N+E+S)

    self.listbox1 = tk.Listbox(self.master, width = 40, height = 10)
    self.listbox1.grid(row=2,column=3,padx=(0,37),pady=(0,0),sticky=N+E+S+W)

    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.scrollbar1.config(command=self.listbox1.yview)
    self.scrollbar1.grid(row=2,column=3, padx=(0,20),pady=(0,0),sticky=N+E+S)

    self.listbox2 = Listbox(self.master,height = 5)
    self.listbox2.grid(row=13,column=0,columnspan=4,padx=(20,37),pady=(0,15),sticky=N+E+S+W)
                            
    self.scrollbar2 = Scrollbar(self.master, orient=VERTICAL)
    self.scrollbar2.config(command=self.listbox2.yview)
    self.scrollbar2.grid(row=13,column=3,padx=(0,20),pady=(0,15),sticky=N+E+S)

    file_transfer_func.create_db(self)

if __name__== "__main__":
    pass
                             
                            
