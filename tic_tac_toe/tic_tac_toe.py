import os
import sys
import requests

from tkinter import *

import tkinter.messagebox 
root=Tk()
root.title("Tic_Tac_Toe")
count=0


bclick = True

def tictactoe(buttons):
    global bclick
    
    if buttons["text"] == "Restart":
        root.destroy()
        CallBack()
    
    elif buttons["text"] == "Close":
        root.destroy()
         
    elif(button1["text"]== "X" and button2["text"]== "X" and button3["text"]=="X" or
         button1["text"]== "X" and button5["text"]== "X" and button9["text"]=="X" or
         button1["text"]== "X" and button4["text"]== "X" and button7["text"]=="X" or
         button4["text"]== "X" and button5["text"]== "X" and button6["text"]=="X" or
         button7["text"]== "X" and button8["text"]== "X" and button9["text"]=="X" or
         button3["text"]== "X" and button5["text"]== "X" and button7["text"]=="X" or
         button2["text"]== "X" and button5["text"]== "X" and button8["text"]=="X" or
         button3["text"]== "X" and button6["text"]== "X" and button9["text"]=="X"):
        
        tkinter.messagebox.showinfo("Winner X","Player X Wins the game")
        
        
    elif(button1["text"]== "O" and button2["text"]== "O" and button3["text"]=="O" or
         button1["text"]== "O" and button5["text"]== "O" and button9["text"]=="O" or
         button1["text"]== "O" and button4["text"]== "O" and button7["text"]=="O" or
         button4["text"]== "O" and button5["text"]== "O" and button6["text"]=="O" or
         button7["text"]== "O" and button8["text"]== "O" and button9["text"]=="O" or
         button3["text"]== "O" and button5["text"]== "O" and button7["text"]=="O" or
         button2["text"]== "O" and button5["text"]== "O" and button8["text"]=="O" or
         button3["text"]== "O" and button6["text"]== "O" and button9["text"]=="O" ):
        
        tkinter.messagebox.showinfo("Winner O","Player O Wins the game")
        
        
        
    elif buttons["text"] == " " and bclick == True:
        buttons["text"]="X"
        buttons.configure(bg="green")
        bclick = False
    elif buttons["text"]==" " and bclick == False:
        buttons["text"]="O"
        buttons.configure(bg="maroon")
        bclick = True
    
    
    else:
    
        tkinter.messagebox.showinfo("Boooo","Game Draw")
    
        
        
buttons=StringVar()


button1=Button(root,text=" ",font=('Arial 20 bold '),height=4,width=8,command=lambda:tictactoe(button1))
button1.grid(row=2,column=0,sticky=S+N+E+W)

button2=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button2))
button2.grid(row=2,column=1,sticky=S+N+E+W)

button3=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button3))
button3.grid(row=2,column=2,sticky=S+N+E+W)

button4=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button4))
button4.grid(row=3,column=0,sticky=S+N+E+W)

button5=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button5))
button5.grid(row=3,column=1,sticky=S+N+E+W)

button6=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button6))
button6.grid(row=3,column=2,sticky=S+N+E+W)

button7=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button7))
button7.grid(row=4,column=0,sticky=S+N+E+W)

button8=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button8))
button8.grid(row=4,column=1,sticky=S+N+E+W)
 
button9=Button(root,text=" ",font=('Arial 20 bold'),height=4,width=8,command=lambda:tictactoe(button9))
button9.grid(row=4,column=2,sticky=S+N+E+W)

button10=Button(root,text="Close",font=('Arial 10 bold'),height=1,width=8,command=lambda:tictactoe(button10))
button10.grid(row=1,column=2,sticky=S+N+E+W)

button11=Button(root,text="Restart",font=('Arial 10 bold'),height=1,width=8,command=lambda:tictactoe(button11))
button11.grid(row=1,column=0,sticky=S+N+E+W)
def CallBack():
    os.system('Tic_Tac_Toe.py')

root.mainloop()