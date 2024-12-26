from tkinter import Tk, Toplevel, Canvas, mainloop
from abc import ABC, abstractmethod
from PIL import ImageTk
from os import path


class Tela(ABC):
    def __init__(self: object, master: Tk | Toplevel) -> None:
        master.resizable(False, False)
        master.geometry('480x270')
        master.title('Pokedex')
        SEPARADOR = '/'
        imagem = ImageTk.PhotoImage(
            file=str(
                path.dirname(
                    path.realpath(__file__)
                ).removesuffix('view')
                + SEPARADOR + 'assets' + SEPARADOR +
                'background' + SEPARADOR + 'background.png'
            )
        )
        self._bg = Canvas(master, bg='#F2BFA4')
        self._bg.pack(fill='both')
        self._html(master)
        self._bg.create_rectangle(35, 98, 205, 188, fill='lightblue')
        self._bg.create_image((0, 0), image=imagem, anchor='nw')
        self._desenhar()
        self._master: Tk | Toplevel = master
        self._widgets: list = list()
        mainloop()

    @abstractmethod
    def _html(self: object, master: Tk | Toplevel) -> None:
        pass

    @abstractmethod
    def _desenhar(self: object) -> None:
        pass
