from tkinter import Tk, messagebox
from view.index import Index
from model.estruturação_do_banco import banco_de_dados


def main() -> None:
    try:
        banco_de_dados()
        import PIL as p
        p.__version__
    except Exception as general_error:
        messagebox.showerror('ERRO', general_error)
    except ModuleNotFoundError as import_erro:
        messagebox.showerror('ERRO', 'Imagens não poderão ser carregadas;\n' +
                             import_erro.__str__())
    finally:
        Index(Tk())
