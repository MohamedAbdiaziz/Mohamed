from tkinter import *
root=Tk()
root.title("sample calculator")
root.iconbitmap("mohamed's icon.ico")
# creating entry
enter=Entry(root,width=35,borderwidth=5)
# place of entry
enter.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# functions

def button_click(num):
	
	curren=enter.get()
	enter.delete(0,END)
	enter.insert(0,str(curren)+str(num))

def button_clear():
	enter.delete(0,END)

def button_add():
	first_num=int(enter.get())
	global f_num
	global math
	math="addition"
	f_num=int(first_num)
	enter.delete(0,END)

def button_equal():
	second_num=int(enter.get())
	enter.delete(0,END)
	if math=="addition":
		enter.insert(0,f_num+int(second_num))
	if math=="substraction":
		enter.insert(0,f_num-int(second_num))
	if math=="mutipilaction":
		enter.insert(0,f_num*int(second_num))
	if math=="division":
		enter.insert(0,f_num/int(second_num))

def button_substract():
	first_num=int(enter.get())
	global f_num
	global math
	math="substraction"
	f_num=int(first_num)
	enter.delete(0,END)

def button_multiply():
	first_num=int(enter.get())
	global f_num
	global math
	math="mutipilaction"
	f_num=int(first_num)
	enter.delete(0,END)

def button_divide():
	first_num=int(enter.get())
	global f_num
	global math
	math="division"
	f_num=int(first_num)
	enter.delete(0,END)

# creating Buttons

button_1=Button(root,text="1",pady=20 ,padx=40,command=lambda:button_click(1))
button_2=Button(root,text="2",pady=20 ,padx=40,command=lambda:button_click(2))
button_3=Button(root,text="3",pady=20 ,padx=40,command=lambda:button_click(3))
button_4=Button(root,text="4",pady=20 ,padx=40,command=lambda:button_click(4))
button_5=Button(root,text="5",pady=20 ,padx=40,command=lambda:button_click(5))
button_6=Button(root,text="6",pady=20 ,padx=40,command=lambda:button_click(6))
button_7=Button(root,text="7",pady=20 ,padx=40,command=lambda:button_click(7))
button_8=Button(root,text="8",pady=20 ,padx=40,command=lambda:button_click(8))
button_9=Button(root,text="9",pady=20 ,padx=40,command=lambda:button_click(9))
button_0=Button(root,text="0",pady=20 ,padx=40,command=lambda:button_click(0))
button_add=Button(root,text="+",pady=20 ,padx=40,command=button_add)
button_substract=Button(root,text="-",pady=20 ,padx=41.5,command=button_substract)
button_multiply=Button(root,text="*",pady=20 ,padx=40,command=button_multiply)
button_divide=Button(root,text="/",pady=20 ,padx=40,command=button_divide)
button_equal=Button(root,text="=",pady=20 ,padx=90,command=button_equal)
button_clear=Button(root,text="C",pady=20 ,padx=90,command=button_clear)

# placeholder

button_equal.grid(row=6,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_substract.grid(row=6,column=0)
button_multiply.grid(row=5,column=1)
button_divide.grid(row=5,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

root.mainloop()