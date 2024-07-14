from tkinter import * 
from tkinter import StringVar

window = Tk()
window.title('Calculator')
window.geometry('600x400')

#buttons
current_calc = ''
def WriteNumber(num):
    global current_calc
    current_calc += num
    var.set(current_calc)
    print(current_calc)

def calculate_num():
    global current_calc
    var.set('')
    try:
        total = eval(current_calc)
        current_calc = ''
        var.set(total)
    except:
        current_calc = ''
        var.set('Invalid Calculation')
        






number_zero = Button(text='0', width=6, height=3, command=lambda: WriteNumber('0'))
number_one = Button(text='1', width=6, height=3, command=lambda: WriteNumber('1'))
number_two = Button(text='2', width=6, height=3, command=lambda: WriteNumber('2'))
number_three = Button(text='3', width=6, height=3, command=lambda: WriteNumber('3'))
number_four = Button(text='4', width=6, height=3, command=lambda: WriteNumber('4'))
number_five = Button(text='5', width=6, height=3, command=lambda: WriteNumber('5'))
number_six = Button(text='6', width=6, height=3, command=lambda: WriteNumber('6'))
number_seven = Button(text='7', width=6, height=3, command=lambda: WriteNumber('7'))
number_eight = Button(text='8', width=6, height=3, command=lambda: WriteNumber('8'))
number_nine = Button(text='9', width=6, height=3, command=lambda: WriteNumber('9'))

#operators
add = Button(text='+', width=6, height=3, command=lambda: WriteNumber('+'))
subtraction = Button(text='-', width=6, height=3, command=lambda: WriteNumber('-'))
multiply = Button(text='×', width=6, height=3, command=lambda: WriteNumber('*'))
divide = Button(text='/', width=6, height=3, command=lambda: WriteNumber('/'))
equals = Button(text='=', width=6, height=3, command=calculate_num)



#screen
var = StringVar()
screen = Label(window, textvariable=var, font=('aerial', 30))
screen.grid(row=9, column=20)
var.set('')


#positioning 
number_zero.grid(row=1, column=1)
number_one.grid(row=1, column=2)
number_two.grid(row=1, column=3)
number_three.grid(row=2, column=1)
number_four.grid(row=2, column=2)
number_five.grid(row=2, column=3)
number_six.grid(row=3, column=1)
number_seven.grid(row=3, column=2)
number_eight.grid(row=3, column=3)
number_nine.grid(row=4, column=1)
add.grid(row=4, column=2)
subtraction.grid(row=4, column=3)
multiply.grid(row=5, column=1)
equals.grid(row=5, column=2)
divide.grid(row=5, column=3)
print(current_calc)


window.mainloop()
