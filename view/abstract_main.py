from tkinter import Tk, messagebox
from view.index import Index
from model.estruturação_do_banco import banco_de_dados


try:
    banco_de_dados()
except:
    messagebox.showinfo('INFO', 'Tudo pronto, ou algum erro aconteceu.')
finally:
    Index(Tk())
