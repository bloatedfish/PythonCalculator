from tkinter import *

# Colors
color = "#26292e"
highlightedColor = "#171a1f"

# Window and Window Title
Screen = Tk()
Screen.geometry('370x435')
Screen.resizable(False, False)
Screen.configure(bg=color)
Screen.title("Calculator")


# Methods

# addtoTextBox(input)
#
# Takes a string input.
#
# Concatenates string input to the current outputted text in outputVar.
def addToTextBox(input):
    outputVar.set(outputVar.get() + input)

# clearTextBox()
#
# Takes no input.
#
# Clears out all text in outputVar.
def clearTextBox():
    outputVar.set('')

# calculate()
#
# Takes no input.
#
# Attempts to evaluate an expression in the current outputted text in outputVar.
# If there is a syntax error, ouputVar lets the user know it is a malformed expression.
def calculate():
    try:
        outputVar.set(eval(outputVar.get()))
    except SyntaxError:
        pass
        outputVar.set('Malformed Expression') 

# TextBox for the entry of numbers
outputVar = StringVar()
textBox = Entry(Screen,textvariable=outputVar).grid(row=0,column=0,columnspan=4)

# Buttons
buttonEquals = Button(Screen,text="=",command= lambda: calculate(), relief = GROOVE, bg = color, fg = "white", height=4, width=42).grid(row=5,column=0,columnspan=4)
buttonDivide = Button(Screen,text="/",command= lambda: addToTextBox('/'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=4,column=3)
buttonMultiply = Button(Screen,text="*",command= lambda: addToTextBox('*'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=3,column=3)
buttonSubtract = Button(Screen,text="-",command= lambda: addToTextBox('-'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=2,column=3)
buttonAdd = Button(Screen,text="+",command= lambda: addToTextBox('+'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=1,column=3)
buttonC = Button(Screen,text="C",command= lambda: clearTextBox(), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=4,column=2)
buttonDecimal = Button(Screen,text=".",command= lambda: addToTextBox('.'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=4,column=1)
button0 = Button(Screen,text="0",command= lambda: addToTextBox('0'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=4,column=0)
button1 = Button(Screen,text="1",command= lambda: addToTextBox('1'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=3,column=0)
button2 = Button(Screen,text="2",command= lambda: addToTextBox('2'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=3,column=1)
button3 = Button(Screen,text="3",command= lambda: addToTextBox('3'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=3,column=2)
button4 = Button(Screen,text="4",command= lambda: addToTextBox('4'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=2,column=0)
button5 = Button(Screen,text="5",command= lambda: addToTextBox('5'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=2,column=1)
button6 = Button(Screen,text="6",command= lambda: addToTextBox('6'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=2,column=2)
button7 = Button(Screen,text="7",command= lambda: addToTextBox('7'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=1,column=0)
button8 = Button(Screen,text="8",command= lambda: addToTextBox('8'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=1,column=1)
button9 = Button(Screen,text="9",command= lambda: addToTextBox('9'), relief = GROOVE, bg = color, fg = "white", height=4, width=8).grid(row=1,column=2)

# Main Loop
mainloop()