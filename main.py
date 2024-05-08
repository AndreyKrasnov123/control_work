import tkinter as tk
class Hare:
    def calculate_area(self):
        pass

class Rectangle(Hare):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Hare):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r * self.r

    def conclusion(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=500, height=500)
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canvas.pack()

        root.mainloop()


rectangle1 = Rectangle(10,20,48,67)
print(rectangle1.calculate_area())

Circle1 = Circle(225,250,50)
Circle2 = Circle(300, 250, 10)

Circle1.conclusion()
Circle2.conclusion()

