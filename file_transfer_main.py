#	Python Ver:     3.5.6
#	Author:	        Anibal Huilca
#       Purpose:        Create a file transfer program using Tkinter


from tkinter import *
import tkinter as tk

import file_transfer_gui
import file_transfer_func

class ParentWindow(Frame):
        def __init__(self, master, *args, **kwargs):
                Frame.__init__(self, master, *args, **kwargs)

                self.master = master

                self.master.minsize(635,400) 
                self.master.maxsize(635,400)
                
                file_transfer_func.center_window(self,635,400)

                self.master.title("File Transfer 5002")
                self.master.configure(bg="#F0F0F0")
   
                self.master.protocol("WM_DELETE_WINDOW",
                                     lambda: file_transfer_func.ask_quit(self))

                arg = self.master
                file_transfer_gui.load_gui(self)
	
if __name__ == "__main__":
	root = Tk()
	App = ParentWindow(root)
	root.mainloop()
