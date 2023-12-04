from tkinter import *
from tkinter import ttk

expression = ""

def press(num):
    global expression

    expression = expression +str(num)

    equation.set(expression)


def equalpress():
    """door midddel van eval word de string omgezet naar pythoncode waardoor het uitgevoerd kan worden """
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = total

    except:
        expression = ""

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 


def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

if __name__ == "__main__":
    
    root = Tk()

    root.title("Calculator")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=1, row=4, sticky=(N, W, E, S))

    root.iconbitmap('C:\\Users\\sbvis\\OneDrive\\Afbeeldingen\\calculator_img.ico')
    root.geometry("320x510")
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # de berekening wordt hier opgeslagen
    equation = StringVar()


    ttk.Label( background="gainsboro", textvariable=equation, font=('Segoe UI Black', 30)).grid(column=0, row=0, columnspan=4, rowspan=4, sticky=(W, E, N, S))
    button0 = Button(mainframe, text="0", width=10, height=5, bg="#838B8B", command=lambda: press(0)).grid(column=2, row=6)

    button1 = Button(mainframe, text="1", width=10, height=5, bg="#838B8B",command=lambda: press(1)).grid(column=1, row=5)

    button2 = Button(mainframe, text="2", width=10, height=5, bg="#838B8B",command=lambda: press(2)).grid(column=2, row=5)

    button3 = Button(mainframe, text="3", width=10, height=5, bg="#838B8B",command=lambda: press(3)).grid(column=3, row=5)

    button4 = Button(mainframe, text="4", width=10, height=5, bg="#838B8B",command=lambda: press(4)).grid(column=1, row=4)

    button5 = Button(mainframe, text="5", width=10, height=5, bg="#838B8B",command=lambda: press(5)).grid(column=2, row=4)

    button6 = Button(mainframe, text="6", width=10, height=5, bg="#838B8B",command=lambda: press(6)).grid(column=3, row=4)

    button7 = Button(mainframe, text="7", width=10, height=5, bg="#838B8B",command=lambda: press(7)).grid(column=1, row=3)

    button8 = Button(mainframe, text="8", width=10, height=5, bg="#838B8B",command=lambda: press(8)).grid(column=2, row=3)

    button9 = Button(mainframe, text="9", width=10, height=5, bg="#838B8B",command=lambda: press(9)).grid(column=3, row=3)

    equal = Button(mainframe, text="=",  width=10, height=5, bg="salmon1", command=equalpress).grid(column=4, row=6)

    plus = Button(mainframe, text="+", width=10, height=5, bg="grey42",command=lambda: press("+")).grid(column=4, row=5)

    minus = Button(mainframe, text="-", width=10, height=5, bg="grey42",command=lambda: press("-")).grid(column=4, row=4)

    comma = Button(mainframe, text=",", width=10, height=5, bg="#838B8B",command=lambda: press(".")).grid(column=3, row=6)

    multiply = Button(mainframe, text="x", width=10, height=5, bg="grey42",command=lambda: press("*")).grid(column=4, row=3)

    divide = Button(mainframe, text="÷", width=10, height=5, bg="grey42",command=lambda: press("/")).grid(column=4, row=2)

    delete = Button(mainframe, text="⌫", width=10, height=5, bg="grey42",command=delete).grid(column=3, row=2)

    clear = Button(mainframe, text="C", width=10, height=5, bg="grey42",command=clear).grid(column=2, row=2)

    ButtonCE = Button(mainframe, text="CE", width=10, height=5, bg="#838B8B",command=lambda: press("")).grid(column=1, row=6)

    Smiley = Button(mainframe, text="☺", width=10, height=5, bg="grey42",command=lambda: press("")).grid(column=1, row=2)


root.mainloop()