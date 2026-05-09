import tkinter as tk

def somar():
    numero1 = float(n3.get())
    numero2 = float(n4.get())
    soma1 = numero1 + numero2
    resultado.config(text = f'{soma1}')

def sub():
    numero1 = float(n3.get())
    numero2 = float(n4.get())
    sub1 = numero1 - numero2
    resultado.config(text= f'{sub1}')
def multi():
    numero1 = float(n3.get())
    numero2 = float(n4.get())
    multi1 = numero1 * numero2
    resultado.config(text= f'{multi1}')
def div():
    numero1 = float(n3.get())
    numero2 = float(n4.get())
    div1 = numero1 / numero2
    resultado.config(text = f'{div1}')



root = tk.Tk()
root.title('Calculadora Do SPanzzzzzz' )
root.geometry('300x500')
text = tk.Label(root , text = 'Calculadora Do SPanzzzzzz' , fg = 'blue' , bg = 'pink')
text.pack()
root['bg'] = 'pink'

n1 = tk.Label(root , text = 'Digite Um Numero' , fg = 'blue' , bg = 'pink')
n1.pack()
n3 = tk.Entry(root , fg = 'blue')
n3.pack()
n2 = tk.Label(root , text = 'Digite Um Numero' , fg = 'blue', bg = 'pink')
n2.pack()
n4= tk.Entry(root , fg = 'blue')
n4.pack()


calc = tk.Button(root , text = '+' , fg = 'blue' , command = somar) 
calc.pack()
calc = tk.Button(root , text = '-' , fg = 'blue' , command = sub)
calc.pack()
calc = tk.Button(root , text = '*' , fg = 'blue' , command = multi)
calc.pack()
calc = tk.Button(root , text = '/' , fg = 'blue' , command = div)
calc.pack()

resultado = tk.Label(root , text = 'resultado' , fg = 'blue' , bg = 'pink')
resultado.pack()

root.mainloop()