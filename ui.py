import os
import subprocess
import tkinter as tk

def launch_0():             
    os.system('./shell/init.sh')
    

def launch_1():             
    os.system('./shell/wake.sh')


def launch_2():             
    os.system('./sequential.sh')


def launch_3():             
    os.system('./shell/battery.sh')


def launch_4():             
    os.system('./shell/init.sh')


def launch_5():             
    os.system('./shell/cancel.sh')
    
    
window = tk.Tk()
window.geometry('275x200')
window.title('Controller')

button0 = tk.Button(window, text="Wake Robot", command=launch_0).pack()
button1 = tk.Button(window, text="Stand Robot", command=launch_1).pack()
button2 = tk.Button(window, text="Run Robot", command=launch_2).pack()
button3 = tk.Button(window, text="Check Battery", command=launch_3).pack()
button4 = tk.Button(window, text="Sleep Robot", command=launch_4).pack()
button5 = tk.Button(window, text="Cancel Process", command=launch_5).pack()

window.eval('tk::PlaceWindow . center')
window.mainloop()
