import tkinter as tk


calculation=""


def add_to_calculate(symbol):
   global calculation
   calculation += str(symbol)
   result.delete(1.0,"end")
   result.insert(1.0,calculation)


def evaluate_calculation():
   global calculation
   try:
      calculation_result = str(eval(calculation))
      calculation = calculation_result
      result.delete(1.0, "end")
      result.insert(1.0, calculation_result)

   except:
      clear_field()
      result.insert(1.0, "Error")


def clear_field():
   global calculation
   calculation=""
   result.delete(1.0,"end")







root = tk.Tk()
root.title("sandeepa")


result= tk.Text(root, height=2, width=16,font=("arial",24))
result.grid(columnspan=6)

btn_1=tk.Button(root,text="1",command=lambda :add_to_calculate(1),width=4,font=("arial",15))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda :add_to_calculate(2),width=4,font=("arial",15))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",command=lambda :add_to_calculate(3),width=4,font=("arial",15))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",command=lambda :add_to_calculate(4),width=4,font=("arial",15 ))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",command=lambda :add_to_calculate(5),width=4,font=("arial",15))
btn_5.grid(row=3,column=2)


btn_6=tk.Button(root,text="6",command=lambda :add_to_calculate(6),width=4,font=("arial",15))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7",command=lambda :add_to_calculate(7),width=4,font=("arial",15))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8",command=lambda :add_to_calculate(8),width=4,font=("arial",15))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9",command=lambda :add_to_calculate(9),width=4,font=("arial",15 ))
btn_9.grid(row=4,column=3)

btn_10=tk.Button(root,text="0",command=lambda :add_to_calculate(0),width=4,font=("arial",15))
btn_10.grid(row=5,column=3)


btn_plus=tk.Button(root,text="+",command=lambda :add_to_calculate("+"),width=4,font=("arial",15))
btn_plus.grid(row=2,column=4)

btn_minus=tk.Button(root,text="-",command=lambda :add_to_calculate("-"),width=4,font=("arial",15))
btn_minus.grid(row=3,column=4)

btn_multiply=tk.Button(root,text="x",command=lambda :add_to_calculate("*"),width=4,font=("arial",15))
btn_multiply.grid(row=4,column=4)

btn_division=tk.Button(root,text="/",command=lambda :add_to_calculate("/"),width=4,font=("arial",15))
btn_division.grid(row=5,column=4)

btn_open=tk.Button(root,text="(",command=lambda :add_to_calculate("("),width=4,font=("arial",15))
btn_open.grid(row=5,column=1)

btn_close=tk.Button(root,text=")",command=lambda :add_to_calculate(")"),width=4,font=("arial",15))
btn_close.grid(row=5,column=2)




btn_clear=tk.Button(root,text="CC",command=clear_field,width=4,font=("arial",15))
btn_clear.grid(row=6,column=4)

btn_equal=tk.Button(root,text="=",command=evaluate_calculation,width=4,font=("arial",15))
btn_equal.grid(row=6,column=3)














root.geometry("300x275")
root.mainloop()
