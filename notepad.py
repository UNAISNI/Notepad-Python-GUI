from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    file = None
    root.title("Untitled - Notepad")
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=(".txt"),filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        f = open(file,"r")
        TextArea.delete(1.0,END)
        TextArea.insert(1.0,f.read())
        f.close()



def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untiled.txt",defaultextension=(".txt"),filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file))
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def copy():
    TextArea.event_generate(("<<Copy>>"))

def cut():
    TextArea.event_generate(("<<Cut>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad By devUnais")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")

    root.geometry("700x500")

    TextArea = Text(root,font="lucida 16")
    file = None
    TextArea.pack(fill=BOTH,expand=True)

    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New",command=newFile)
    FileMenu.add_command(label="Open",command=openFile)
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)



    EditMenu = Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    # HelpMenu = Menu(MenuBar)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)




    MenuBar.add_cascade(label="Help", menu=HelpMenu)


    root.config(menu=MenuBar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill="y")
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)




    root.mainloop()