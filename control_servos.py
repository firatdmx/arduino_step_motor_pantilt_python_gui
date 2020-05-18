from tkinter import *
from tkinter.ttk import *
import serial

ser = serial.Serial('COM8', 9600, timeout=1)
ser.write(b'p 90 p')
ser.write(b't 90 t')
multiX = 10
sx = 90
sy = 90


def okk():
    global multiX
    xa = int(multiplier.get())
    if xa < 1 or xa > 180:
        print("Error: Number can't be more than 179 or less than 1")
        if xa > 180:
            multiplier.delete(0, END)
            multiplier.insert(0, "180")
            xa = 179
        if xa < 1:
            multiplier.delete(0, END)
            multiplier.insert(0, "1")
            xa = 1
    else:
        multiX = int(multiplier.get())
        print(int(multiX))


def panleft():
    global sx
    if sx > 180:
        print("bigger than 180")
    else:
        sx += multiX
        my_str = 'p ' + str(sx) + ' p'
        ser.write(my_str.encode())
        print(my_str.encode())


def panright():
    global sx
    if sx < 1:
        print("smaller than 1")
    else:
        sx -= multiX
        my_str = 'p ' + str(sx) + ' p'
        ser.write(my_str.encode())
        print(my_str.encode())


def tiltdown():
    global sy
    if sy > 178:
        print("bigger than 178")
    else:
        sy += multiX
        my_str = 't ' + str(sy) + ' t'
        ser.write(my_str.encode())
        print(my_str.encode())


def tiltup():
    global sy
    if sy < 15:
        print("smaller than 15")
    else:
        sy -= multiX
        my_str = 't ' + str(sy) + ' t'
        ser.write(my_str.encode())
        print(my_str.encode())

def centerx():
    global sx
    global sy
    ser.write(b'p 90 p')
    ser.write(b't 90 t')
    sx = 90
    sy = 90


root = Tk()

root.resizable(0, 0)
root.geometry("312x336")
root.title("PAN & TILT")

labelMul = Label(text="Multiplier:")
labelMul.grid(row=0, column=0, stick=E)

multiplier = Entry(width=10)
multiplier.grid(row=0, column=1, stick=W)
multiplier.insert(0, "10")

multipBut = Button(text="OK", command=okk)
multipBut.grid(row=0, column=2)

phup = PhotoImage(file = r"./images/up.png")
tiltupl = Label(text="UP", image=phup)
tiltupl.grid(row=1, column=1)
tiltupl.bind("<Button-1>", lambda _ : tiltup())

phleft = PhotoImage(file = r"./images/left.png")
panleftl = Label(text="LEFT", image=phleft)
panleftl.grid(row=2, column=0)
panleftl.bind("<Button-1>", lambda _ : panleft())

phmid = PhotoImage(file = r"./images/mid.png")
centerl = Label(image=phmid)
centerl.grid(row=2, column=1)
centerl.bind("<Button-1>", lambda _ : centerx())

phright = PhotoImage(file = r"./images/right.png")
panrightl = Label(text="RIGHT", image=phright)
panrightl.grid(row=2, column=2)
panrightl.bind("<Button-1>", lambda _ : panright())

phdown = PhotoImage(file = r"./images/down.png")
tiltdownl = Label(text="DOWN", image=phdown)
tiltdownl.grid(row=3, column=1)
tiltdownl.bind("<Button-1>", lambda _ : tiltdown())


root.mainloop()
