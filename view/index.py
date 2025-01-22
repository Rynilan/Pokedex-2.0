from view.tela import Tela
from tkinter import Tk, Toplevel, Button, Canvas
from view.managment import Managment
from view.view import View


class Index(Tela):
    def _html(self: object, master: Tk | Toplevel) -> None:
        self.administrar = Button(master,
                                  text='Gerir',
                                  command=self.__gerir,
                                  font=('BigBlueTerm437 nerd font', '8'),
                                  bg='#ffa500')
        self.administrar.place(x=313, y=200, width=60, anchor='center')

        self.vizualizar = Button(master,
                                 text='Listar',
                                 font=('BigBlueTerm437 nerd font', '8'),
                                 bg='#ffa500',
                                 command=self.__ver)
        self.vizualizar.place(x=411, y=200, anchor='center', width=60)

        self.sair = Button(master,
                           text='Sair',
                           font=('BigBlueTerm437 nerd font', '8'),
                           bg='#ba55d3',
                           command=master.destroy)
        self.sair.place(x=362, y=238, width=60, anchor='center')

    def _desenhar(self: object) -> None:
        self._bg: Canvas
        self._bg.create_text(120, 143, text='Pokedex\nPowered by: Linux',
                             anchor='center',
                             font=('BigBlueTerm437 nerd font', '10'),
                             justify='center')
        self._bg.create_text(315, 115,
                             text='Created by:\n Rynilan\n' +
                                  'https://github.com/Rynilan',
                             anchor='center',
                             font=('BigBlueTerm437 nerd font', '6'),
                             justify='center',
                             width=80)

    def __ver(self: object):
        View(self._master)

    def __gerir(self: object):
        Managment(self._master)
