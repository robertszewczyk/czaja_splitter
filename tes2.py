from Tkinter import *
import tkFileDialog
import sys
import os
from os import listdir
from os.path import isfile
import shutil


class Redir(object):
    # This is what we're using for the redirect, it needs a text box
    def __init__(self, textbox):
        self.textbox = textbox
        self.textbox.config(state=NORMAL)
        self.fileno = sys.stdout.fileno

    def write(self, message):
        # When you set this up as redirect it needs a write method as the
        # stdin/out will be looking to write to somewhere!
        self.textbox.insert(END, str(message))

def askopenfilename():
    """ Prints the selected files name """
    textbox.delete('1.0',END)
    filename = tkFileDialog.askdirectory()
    if filename:
        for f in listdir(filename):

            if(isfile(str(filename)+'/'+str(f))):
                print 'Processing ' + filename + '/' + f + ' delimited with ' + str(textbox2.get('1.0',END)).strip()
                delimiter = str(textbox2.get('1.0',END)).strip()
                list = f.split(delimiter)
                nesting = 0
                dirpath = ""
                while(nesting < len(list)-1):
                    dirpath = dirpath + list[nesting] + '/'
                    nesting = nesting + 1
                if dirpath != "":
                    if not os.path.exists(dirpath):
                        os.makedirs(dirpath)
                    shutil.move(str(filename)+'/'+str(f),dirpath)



if __name__ == '__main__':

    # Make the root window
    root = Tk()

    # Make a button to get the file name
    # The method the button executes is the askopenfilename from above
    # You don't use askopenfilename() because you only want to bind the button
    # to the function, then the button calls the function.
    button = Button(root, text='Select directory', command=askopenfilename)
    # this puts the button at the top in the middle
    button.grid(row=3, column=0)

    # Make a scroll bar so we can follow the text if it goes off a single box
    scrollbar = Scrollbar(root, orient=VERTICAL)
    # This puts the scrollbar on the right handside
    scrollbar.grid(row=2, column=3, sticky=N+S+E)

    # Make a text box to hold the text
    textbox = Text(root,font=("Helvetica",8),state=DISABLED, yscrollcommand=scrollbar.set, wrap=WORD)
    # This puts the text box on the left hand side
    textbox.grid(row=2, column=0, columnspan=3, sticky=N+S+E+W)

    label = Label(root, text="DELIMITER:")
    label.grid(row=1, column=0, columnspan=1)

    textbox2 = Text(root,height=1, font=("Helvetica",8),state=NORMAL, yscrollcommand=scrollbar.set, wrap=WORD)
    # This puts the text box on the left hand side
    textbox2.grid(row=1, column=1, columnspan=1, sticky=N+S+E+W)
    textbox2.insert(INSERT,"@")

    # Configure the scroll bar to stroll with the text box!
    scrollbar.config(command=textbox.yview)

    #Set up the redirect
    stdre = Redir(textbox)
    # Redirect stdout, stdout is where the standard messages are ouput
    sys.stdout = stdre
    # Redirect stderr, stderr is where the errors are printed too!
    sys.stderr = stdre
    # Print hello so we can see the redirect is working!
    print "Please select directory to process"
    # Start the application mainloop
    root.mainloop()
