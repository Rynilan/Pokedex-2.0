from view.mainframe import MainFrame
from tkinter import Button, CENTER


class PokedexScreen(MainFrame):
    def _create_things(self, **kwargs) -> None:

        botao_ver = Button(self._mainframe, text='Ver Pokemons',
                           command=lambda:
                               self._tela._load(self._tela._ver, None, None)
                           )
        botao_ver.place(relx=0.15, rely=0.25, relwidth=0.2, anchor=CENTER)
        botao_gerir = Button(self._mainframe, text='Gerir Pokemons',
                             command=lambda:
                             self._tela._load(
                                 self._tela._gerenciar, None, None
                             ))
        botao_gerir.place(relx=0.85, rely=0.25, relwidth=0.2, anchor=CENTER)
