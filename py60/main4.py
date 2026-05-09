import tkinter as tk

def display():

    parc = spanz.get()
    parc2 = 'voce se cadrastou em Spanzgram'
    spanz2.config(text = f'{parc2}')


#criar janela
janela = tk.Tk()
janela.title('Spanzgram')

# texto na tela
text = tk.Label(janela, text = 'bem-vindo ao Spanzgram ' , fg = '#ff0093')
text.pack()


#input
email = tk.Label(janela , text = 'digite seu e-mail')
email.pack()
spanz = tk.Entry(janela , fg = '#ff0093')
spanz.pack()
senha = tk.Label(janela , text = 'digite sua senha')
senha.pack()
spanz = tk.Entry(janela , fg = '#ff0093')
spanz.pack()
#criar botao
botao = tk.Button(janela, text='cadastrar-se' , command = display) 
botao.pack()


spanz2 = tk.Label(janela , text  = '')
spanz2.pack()


#resoluçao da tela
janela.geometry('1000x1000')

janela.mainloop()