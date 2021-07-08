from tkinter import*
"""
App name "Calculator"
Author: Enkhbat B.
©2021 Enkhbat and ©2021 Alice
Version 1.1

Some terms to define:
padding = the space between its content and its border.
"""
# display whatever the user clicks on
def btnOnClick(numb):
    global operator  # operator will hold my expressions for manipulation
    operator = operator + str(numb);
    text_input.set(operator);
    
# perfom the user's operation and display the result 
def btnEqual():
    try:
        global operator
        Op_res = str(eval(operator));
        text_input.set(Op_res);
        operator = "";
    # if error is generate then handle
    except:
        text_input.set("Error")
#         messagebox.showerror("An error has occurred", "Invalid Operation")
        operator = "";

# clearing everything on sreen
def btnClear():
    global operator
    operator = "";
    text_input.set("");
# bellow function supposed to show squre root but it was not working!
def sq_btn(x):
    import math
    num = math.sqrt(x);
    text_input.set(num)
# create window
UiCal = Tk();
UiCal.title('"Calculator" ©Alice')
# UiCal.geometry("200x300") # set GUI size in pixel: width x height
operator = ""
text_input = StringVar()

# display screen creation (i.e. an entry text)
txtDisplay = Entry(UiCal,
           font = ('Comic Sans MS', 20, 'bold'),
           textvariable = text_input,
           bd = 5,
           insertwidth = 4,
           fg = 'blue',
           bg = 'white',
           justify = 'right').grid(columnspan=4);

# creation of buttons
btn1 = Button(UiCal,
             padx = 20, # you can also add pady = 16
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '1',
             command = lambda:btnOnClick(1),
             height=1, width=2).grid(row=1, column=0)

btn2 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '2',
             command = lambda:btnOnClick(2),
             height=1, width=2).grid(row=1, column=1)
btn3 = Button(UiCal,
              padx = 20,
              bd = 4,
              fg = 'black',
              bg = 'grey',
              font = ('Comic Sans MS', 20, 'bold'),
              text = '3',
              command = lambda:btnOnClick(3),
              height=1, width=2).grid(row=1, column=2)
btn4 = Button(UiCal,
              padx = 20,
              bd = 4,
              fg = 'black',
              bg = 'grey',
              font = ('Comic Sans MS', 20, 'bold'),
              text = '4',
              command = lambda:btnOnClick(4),
              height=1, width=2).grid(row=2, column=0)
btn5 = Button(UiCal,
              padx = 20,
              bd = 4,
              fg = 'black',
              bg = 'grey',
              font = ('Comic Sans MS', 20, 'bold'),
              text = '5',
              command = lambda:btnOnClick(5),
              height=1, width=2).grid(row=2, column=1)
btn6 = Button(UiCal,
              padx = 20,
              bd = 4,
              fg = 'black',
              bg = 'grey',
              font = ('Comic Sans MS', 20, 'bold'),
              text = '6',
              command = lambda:btnOnClick(6),
              height=1, width=2).grid(row=2, column=2)
div_btn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '/', # or '÷' equally as valid
             command = lambda:btnOnClick("/"), # or '÷' equally as valid
             height=1, width=2).grid(row=3, column=3)
mult_btn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'x', # or '*' equally as valid
             command = lambda:btnOnClick("*"), 
             height=1, width=2).grid(row=2, column=3)
min_btn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '-', # or '-' equally as valid
             command = lambda:btnOnClick("-"),
             height=1, width=2).grid(row=4, column=2)
# i could not figure out how to make it work
sq_btn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20,'bold'),
             text = '√',
             command = lambda:sq_btn(x),
             height=1, width=2).grid(row=4, column=1)
plu_btn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '+',
             command = lambda:btnOnClick("+"),
             height=1, width=2).grid(row=4, column=3)
Eqbtn = Button(UiCal,
             padx = 90,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '=',
             command = btnEqual,
             height=1, width=2).grid(row=5, column=1, columnspan=3)

Clrbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'Cl',
             command = btnClear,
             height=1, width=2).grid(row=1, column=3)

Exitbtn = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = 'EXIT',
             command = UiCal.destroy, # use destroy to close GUI
             height=1, width=2).grid(row=5, column=0)
btn7 = Button(UiCal,
             padx = 20, # you can also add pady = 16
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '7',
             command = lambda:btnOnClick(7),
             height=1, width=2).grid(row=3, column=0)

btn8 = Button(UiCal,
             padx = 20,
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '8',
             command = lambda:btnOnClick(8),
             height=1, width=2).grid(row=3, column=1)
btn9 = Button(UiCal,
              padx = 20,
              bd = 4,
              fg = 'black',
              bg = 'grey',
              font = ('Comic Sans MS', 20, 'bold'),
              text = '9',
              command = lambda:btnOnClick(9),
              height=1, width=2).grid(row=3, column=2)
btn0 = Button(UiCal,
             padx = 20, # you can also add pady = 16
             bd = 4,
             fg = 'black',
             bg = 'grey',
             font = ('Comic Sans MS', 20, 'bold'),
             text = '0',
             command = lambda:btnOnClick(0),
             height=1, width=2).grid(row=4, column=0)

# start the App
UiCal.mainloop()