import tkinter as tk
from tkinter import filedialog, Text
import os

import webbrowser

root = tk.Tk()
apps= [
    "C:/Users/samue/AppData/Local/Programs/Microsoft VS Code/Code.exe", 
    "C:/Users/samue/AppData/Local/insomnia/Insomnia.exe",
    "C:/Users/samue/AppData/Roaming/Zoom/bin/Zoom.exe",
    "C:/Users/samue/AppData/Local/MongoDBCompass/MongoDBCompass.exe",
    "C:/WINDOWS/system32/cmd.exe",
    "C:/Program Files/Git/git-bash.exe"
    ]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables","*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)

    for app in apps: 
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)
    
    webbrowser.open('https://github.com/sosoberg') 

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)

openFile.pack()

startApps = tk.Button(root, text="Start Coding!", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)

startApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')