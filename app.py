from tkinter import *
from tkinter import messagebox
import requests

#Requisição da API
req = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL").json()

#Pegando o valor atual do dolar e euro
dolar = float(req["USDBRL"]["bid"])
euro = float(req["EURBRL"]["bid"])

#Congiurações da GUI
window = Tk()
window.title("Conversor de Moedas")
window.geometry("395x185+550+300")
window.resizable(False, False)
window.iconbitmap("icon.ico")
window.config(bg='#004e92')


#Função Converter
def converter():
    while True:
        if e_real.get() == '':
            messagebox.showerror("Error", "Digite uma quantia em real")
        else:
            conv_dolar = float(e_real.get()) / dolar
            conv_dolar = f'$ {conv_dolar:_.2f}'
            dolar_txt = conv_dolar.replace('.', ',').replace('_', '.')

            conv_euro = float(e_real.get()) / euro
            conv_euro = f'€ {conv_euro:_.2f}'
            euro_txt = conv_euro.replace('.', ',').replace('_', '.')

            Label(frame_dolar, text=dolar_txt, font=('Arial 19 bold'), fg='black').place(x=5, y=0, width=180, height=29)
            Label(frame_euro, text=euro_txt, font=('Arial 19 bold'), fg='black').place(x=5, y=0, width=180, height=29)
        break

#Frames
frame_cima = Frame(window, relief="solid", bg='#004e92')
frame_real = Frame(window, borderwidth=2, relief="solid")
frame_euro = Frame(window, borderwidth=2, relief="solid")
frame_dolar = Frame(window, borderwidth=2, relief="solid")

#Labels para os frames
l_titulo = Label(frame_cima, text="Conversor de Moedas", fg='white', font=('Arial 19'), bg='#004e92')
l_real = Label(window, text="Real", bg='#004e92', fg='white')
l_euro = Label(window, text="Euro", bg='#004e92', fg='white')
l_dolar = Label(window, text="Dólar", bg='#004e92', fg='white')

#Buttons
btn_converter = Button(window, text="Converter", command=converter, fg='black', font='Arial 12')

#Entrys
e_real = Entry(frame_real)

#Placing Widgtes
e_real.place(x=0, y=0, width=100, height=32)
btn_converter.place(x=120, y=60,  width=100, height=36)
frame_cima.place(x=0, y=0, width=400, height=35)
frame_real.place(x=10, y=60, width=100, height=35)
frame_euro.place(x=10, y=140, width=180, height=35)
frame_dolar.place(x=204, y=140, width=180, height=35)
l_titulo.place(x=78, y=0)
l_real.place(x=7, y=39)
l_euro.place(x=6, y=118)
l_dolar.place(x=200, y=118)

window.mainloop()
