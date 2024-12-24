from view.tela import Tela
from tkinter import Tk, Toplevel, Button, Canvas
from view.managment import Administracao
from view.list import Lista


class Index(Tela):
    def html(self: object, master: Tk | Toplevel) -> None:
        self.bg = Canvas(master, bg='#eef')
        self.bg.pack(fill='both')

        self.administrar = Button(master,
                                  text='Administrar',
                                  command=self.__gerir)
        self.administrar.place(x=100, y=100)

        self.vizualizar = Button(master,
                                 text='Ver Pokemons',
                                 command=self.__listar)
        self.vizualizar.place(x=200, y=100)

    def __listar(self: object):
        self.vizualizar.conf(state='disabled')
        Lista(self.__master)
        self.vizualizar.conf(state='normal')

    def __gerir(self: object):
        self.administrar.conf(state='disabled')
        Administracao(self.__master)
        self.administrar.conf(state='normal')
