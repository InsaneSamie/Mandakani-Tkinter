from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("Mandakani")

def myfunc1():
    print("Hello! Sub-menu of File is successful created!")

def myfunc2():
    print("Hello! Sub-menu of Edit is successful created!")

def myfunc3():
    print("Hello! Sub-menu of View is successful created!")

def myfunc4():
    print("Hello! Sub-menu of Help is successful created!")

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Text File",command=myfunc1)
m1.add_command(label="New File",command=myfunc1)
m1.add_command(label="New Window",command=myfunc1)
m1.add_separator()
m1.add_command(label="Open File",command=myfunc1)
m1.add_command(label="Open Folder",command=myfunc1)
m1.add_command(label="Open Workspace from File",command=myfunc1)
m1.add_command(label="Open Recent",command=myfunc1)
m1.add_separator()
m1.add_command(label="Add Folder to Workspace",command=myfunc1)
m1.add_command(label="Save Workspace As",command=myfunc1)
m1.add_command(label="Duplicate Workspace",command=myfunc1)
m1.add_separator()
m1.add_command(label="Save",command=myfunc1)
m1.add_command(label="Save As",command=myfunc1)
m1.add_command(label="Save All",command=myfunc1)
m1.add_command(label="Auto Save",command=myfunc1)
m1.add_command(label="Print",command=myfunc1)
m1.add_separator()
m1.add_command(label="Share",command=myfunc1)
m1.add_separator()
m1.add_command(label="Revert File",command=myfunc1)
m1.add_command(label="Close Folder",command=myfunc1)
m1.add_command(label="Close Window",command=myfunc1)
m1.add_command(label="Exit",command=quit)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo",command=myfunc2)
m2.add_command(label="Redo",command=myfunc2)
m2.add_separator()
m2.add_command(label="Cut",command=myfunc2)
m2.add_command(label="Copy",command=myfunc2)
m2.add_command(label="Paste",command=myfunc2)
m2.add_separator()
m2.add_command(label="Find",command=myfunc2)
m2.add_command(label="Replace",command=myfunc2)
m2.add_separator()
m2.add_command(label="Find in Files",command=myfunc2)
m2.add_command(label="Replace in Files",command=myfunc2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Open View",command=myfunc3)
m3.add_separator()
m3.add_command(label="Appearance",command=myfunc3)
m3.add_command(label="Editor Layout",command=myfunc3)
m3.add_separator()
m3.add_command(label="Explorer",command=myfunc3)
m3.add_command(label="Search",command=myfunc3)
m3.add_command(label="Source Control",command=myfunc3)
m3.add_command(label="Run",command=myfunc3)
m3.add_command(label="Extensions",command=myfunc3)
m3.add_separator()
m3.add_command(label="Problems",command=myfunc3)
m3.add_command(label="Output",command=myfunc3)
m3.add_separator()
m3.add_command(label="Word Wrap",command=myfunc3)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label="Welcome",command=myfunc4)
m4.add_separator()
m4.add_command(label="Show All Commonds",command=myfunc4)
m4.add_command(label="Documentation",command=myfunc4)
m4.add_command(label="Show Release Notes",command=myfunc4)
m4.add_separator()
m4.add_command(label="Keyboard Shortcut Reference",command=myfunc4)
m4.add_command(label="Video Tutorials",command=myfunc4)
m4.add_command(label="Tips and Tricks",command=myfunc4)
m4.add_separator()
m4.add_command(label="Join Us on YouTube",command=myfunc4)
m4.add_command(label="Search Feature Requests",command=myfunc4)
m4.add_command(label="Report Issue",command=myfunc4)
m4.add_separator()
m4.add_command(label="View License",command=myfunc4)
m4.add_command(label="Privacy Statement",command=myfunc4)
m4.add_separator()
m4.add_command(label="Check for Updates",command=myfunc4)
m4.add_separator()
m4.add_command(label="About",command=myfunc4)

root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)
mainmenu.add_cascade(label="Edit", menu=m2)
mainmenu.add_cascade(label="View", menu=m3)
mainmenu.add_cascade(label="Help", menu=m4)

root.mainloop()