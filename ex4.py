import tkinter as tk

def draw(canvas):
    canvas.create_oval(150,50, 200,100)
    canvas.create_line(175,100, 175,160)
    canvas.create_line(175,125, 135,100)
    canvas.create_line(175,125, 215,100)
    canvas.create_line(175,160, 135,210)
    canvas.create_line(175,160, 215,210)

root=tk.Tk()
canvas=tk.Canvas(root, width=400, height=300)
canvas.pack()
draw(canvas)
root.mainloop()