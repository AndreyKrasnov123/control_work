import tkinter as tk

def print_direction(event):
    if event.keysym == 'Up':
        label.config(text="верх")
    elif event.keysym == 'Down':
        label.config(text="низ")
    elif event.keysym == 'Right':
        label.config(text="право")
    elif event.keysym == 'Left':
        label.config(text="лево")

root = tk.Tk()
label = tk.Label(root, text="")
label.pack()
root.bind('<Up>', print_direction)
root.bind('<Down>', print_direction)
root.bind('<Right>', print_direction)
root.bind('<Left>', print_direction)
root.mainloop()