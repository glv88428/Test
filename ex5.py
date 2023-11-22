import tkinter as tk

def draw(canvas,x):
    canvas.create_oval(150+x,50, 200+x,100)
    canvas.create_line(175+x,100, 175+x,160)
    canvas.create_line(175+x,125, 135+x,100)
    canvas.create_line(175+x,125, 215+x,100)
    canvas.create_line(175+x,160, 135+x,210)
    canvas.create_line(175+x,160, 215+x,210)

def motion():
    global x1
    canvas.delete("all")
    draw(canvas,x1)
    x1+=10
    root.after(100,motion)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
x1= 0
motion()
root.mainloop()