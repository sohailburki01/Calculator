from tkinter import *

first_num = second_num = operator = None

def getDigit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def getOperator(op):
    global first_num, operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text='')

def getResult():
    global first_num,second_num, operator
    second_num = int(result_label['text'])
    if operator == '+':
        result_label.config(text= str(first_num + second_num))
    elif operator == '-':
        result_label.config(text= str(first_num - second_num))
    elif operator == '*':
        result_label.config(text= str(first_num * second_num))
    else:
        if second_num == 0:
            result_label.config(text='error')
        else:
            result_label.config(text=str(round(first_num /second_num, 2)))
root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.configure(bg='black')

result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, columnspan=5, column=0, pady=(50, 20), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))

btb7 = Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(7))
btb7.grid(row=1, column=0)
btb7.config(font=('verdana', 14))

btb8 = Button(root, text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(8))
btb8.grid(row=1, column=1)
btb8.config(font=('verdana', 14))

btb9 = Button(root, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(9))
btb9.grid(row=1, column=2)
btb9.config(font=('verdana', 14))

btb_add = Button(root, text='+', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getOperator('+'))
btb_add.grid(row=1, column=3)
btb_add.config(font=('verdana', 14))

btb4 = Button(root, text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(4))
btb4.grid(row=2, column=0)
btb4.config(font=('verdana', 14))

btb5 = Button(root, text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(5))
btb5.grid(row=2, column=1)
btb5.config(font=('verdana', 14))

btb6 = Button(root, text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(6))
btb6.grid(row=2, column=2)
btb6.config(font=('verdana', 14))

btb_sub = Button(root, text='-', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getOperator('-'))
btb_sub.grid(row=2, column=3)
btb_sub.config(font=('verdana', 14))

btb1 = Button(root, text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(1))
btb1.grid(row=4, column=0)
btb1.config(font=('verdana', 14))

btb2 = Button(root, text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(2))
btb2.grid(row=4, column=1)
btb2.config(font=('verdana', 14))

btb3 = Button(root, text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(3))
btb3.grid(row=4, column=2)
btb3.config(font=('verdana', 14))

btb_mul = Button(root, text='*', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getOperator('*'))
btb_mul.grid(row=4, column=3)
btb_mul.config(font=('verdana', 14))

btb_clr = Button(root, text='C', bg='#00a65a', fg='white', width=5, height=2, command=lambda: clear())
btb_clr.grid(row=5, column=1)
btb_clr.config(font=('verdana', 14))

btb0 = Button(root, text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getDigit(0))
btb0.grid(row=5, column=0)
btb0.config(font=('verdana', 14))

btb_equal = Button(root, text='=', bg='#00a65a', fg='white', width=5, height=2, command=getResult)
btb_equal.grid(row=5, column=2)
btb_equal.config(font=('verdana', 14))

btb_div = Button(root, text='/', bg='#00a65a', fg='white', width=5, height=2, command=lambda: getOperator('/'))
btb_div.grid(row=5, column=3)
btb_div.config(font=('verdana', 14))

root.mainloop()
