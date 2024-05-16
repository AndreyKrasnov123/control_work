# уроыень С второе задание
import tkinter as tk

def move_circle(event):
    canvas.coords(circle, event.x-10, event.y-10, event.x+10, event.y+10)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
circle = canvas.create_oval(190, 190, 210, 210)
canvas.bind("<Button-1>", move_circle)
root.mainloop()
