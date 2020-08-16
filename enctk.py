import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

HEIGHT = 450
WIDTH = 700
root = tk.Tk()
root.title("FrowaniEncrpyt")

#defines an encrypting function that translates letters to numbers and shifts the numbers down by twenty
def encrypt(sentence):
    result = []
    for letter in sentence:
        l = ((((ord(letter) - 20) * 7) / 2) - 63) * 2
        result.append(int(l))
    full_str = ' '.join([str(elem) for elem in result])
    outputentry.insert(INSERT, (full_str))

#defines a decrypting function that changes the string input to a list, which then adds twenty to each interger in the list, finally translating the numbers to letters
def decrypt(result):
    end_string = ""
    resultinterger = result.split()
    mapresult = map(int, resultinterger)
    resultlist = list(mapresult)
    for numbers in resultlist:
        l = int(numbers)
        l = int(((((l / 2) + 63) * 2) / 7) + 20)
        l = chr(l)
        end_string = end_string + l
    outputentry.insert(INSERT, (end_string))

def clearinoutput():
    outputentry.delete('1.0', 'end')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#d8dfe6')
canvas.pack()

maintitle = tk.Label(root, text="FrowaniEncrpyt v2.0.1", font=('System', 18), fg='#303336', anchor='n', bg='#acb5bd')
maintitle.place(relx=0.28, rely=0.02, relwidth=0.41, relheight=0.08)

mainframe = tk.Frame(root, bg='#c0c9d1')
mainframe.place(relx=0.08, rely=0.12, relwidth=0.84, relheight=0.8)

inputlabel = tk.Label(mainframe, text="Input", font=('Verdana', 12), fg='#5f656b', bg='#c0c9d1')
inputlabel.place(relx=0.4, rely=0.02, relwidth=0.2, relheight=0.05)

inputentry = tk.Entry(mainframe, font=('Arial', 10), justify='left')
inputentry.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)

enbutton = tk.Button(mainframe, text="Encrypt", font=('Verdana', 10), bg='#b9c2c9', activebackground='#8a9299', command=lambda: encrypt(inputentry.get()))
enbutton.place(relx=0.25, rely=0.38, relwidth=0.1, relheight=0.05)

debutton = tk.Button(mainframe, text="Decrypt", font=('Verdana', 10), bg='#b9c2c9', activebackground='#8a9299', command=lambda: decrypt(inputentry.get()))
debutton.place(relx=0.65, rely=0.38, relwidth=0.1, relheight=0.05)

outputlabel = tk.Label(mainframe, text="Output", font=('Verdana', 12), fg='#5f656b', bg='#c0c9d1')
outputlabel.place(relx=0.4, rely=0.46, relwidth=0.2, relheight=0.05)

outputentry = tk.Text(mainframe, font=('Arial', 10), bg='#ffffff')
outputentry.place(relx=0.05, rely=0.54, relwidth=0.9, relheight=0.25)

clearbutton = tk.Button(mainframe, text="Clear Output", font=('Verdana', 10), bg='#b9c2c9', activebackground='#8a9299', command=lambda: clearinoutput())
clearbutton.place(relx=0.4, rely=0.82, relwidth=0.2, relheight=0.1)

root.mainloop()
