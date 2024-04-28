import os
import tkinter as tk
root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=300)
canvas1.pack()

label1 = tk.Label(root, text='Hand Gesture Recognition')
label1.config(font=('Arial', 30))
canvas1.create_window(400, 50, window=label1)


def create_charts():
    os.system('AiVirtualMouseProject.py')


button1 = tk.Button(root, text='AI Virtual Mouse ', command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(300, 180, window=button1)
button2 = tk.Button(root, text='project description', command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(500, 180, window=button2)
root.mainloop()
