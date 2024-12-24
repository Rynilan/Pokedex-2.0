from tkinter import Tk, Toplevel, mainloop
from abc import ABC, abstractmethod


class Tela(ABC):
    def __init__(self: object, master: Tk | Toplevel) -> None:
        master.resizable(False, False)
        master.geometry('480x270')
        master.title('Pokedex')
        self.__master: Tk | Toplevel = master
        self.__widgets: list = list()
        self._html(master)
        mainloop()

    @abstractmethod
    def _html(self: object, master: Tk | Toplevel) -> None:
        pass
