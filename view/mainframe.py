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

    def _image(self, imagem):
        from os import path
        from tkinter import Label
        from model.crud import SEPARADOR
        from PIL import ImageTk, Image
        self.background = Label(self._mainframe)
        imagem = ImageTk.PhotoImage(Image.open(path.dirname(
                                    path.realpath(__file__)
                                    ).removesuffix('view')
            + 'assets' + SEPARADOR + 'background'
            + SEPARADOR + imagem + '.png').resize((1024, 712)))
        self.background.config(image=imagem)
        self.background.image = imagem
        self.background.place(x=0, y=0, relheight=1, relwidth=1)

