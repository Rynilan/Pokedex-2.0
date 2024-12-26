from tkinter import Tk, messagebox
from view.index import Index
from model.estruturação_do_banco import banco_de_dados


def main() -> None:
    try:
        banco_de_dados()
    except Exception as e:
        messagebox.showerror('ERRO', e)
    finally:
        Index(Tk())
