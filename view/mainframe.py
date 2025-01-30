from tkinter import Frame, Tk
from abc import ABC, abstractmethod


class MainFrame(ABC):
    def __init__(
        self: object,
        master: Tk,
        mainframe: Frame,
        tela: object,
    ) -> None:
        self._master = master
        self._mainframe = mainframe
        self._tela = tela

    @abstractmethod
    def _create_things(self: object, **kwargs) -> None:
        pass
