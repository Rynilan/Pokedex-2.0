from tkinter import Frame, Tk
from abc import ABC, abstractmethod
from os import path


class MainFrame(ABC):
    def __init__(
        self: object,
        master: Tk,
        mainframe: Frame,
        tela: object,
        bg: path = None
    ) -> None:
        self._master = master
        self._mainframe = mainframe
        self._tela = tela
        self._bg = bg

    @abstractmethod
    def _create_things(self: object, **kwargs) -> None:
        pass
