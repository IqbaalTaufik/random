import tkinter as tk
from tkinter import filedialog, Text 
import os


rut = tk.Tk()
apps =[]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", 
                title="pilih file",filetypes=(("executables","*.exe"),("all files", "*.*")))

    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(rut, height=750, width=650, bg="#34495e")
canvas.pack()



frame = tk.Frame(rut, bg="#bdc3c7")
frame.place (relwidth=0.8, relheight=0.8, relx= 0.1, rely=0.055)


openFile = tk.Button(rut, text="Open", padx=10, pady=5, fg="white", bg="#34495e", command=addApp)
openFile.pack()


runApps = tk.Button(rut, text="Run", padx=10, pady=5, fg="white", bg="#34495e", command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()

    
rut.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app+ ',')
