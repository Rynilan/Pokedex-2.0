from view.tela import Tela
from tkinter import Tk, Toplevel, Button, Canvas
from view.managment import Managment
from view.view import View


class Index(Tela):
    def _html(self: object, master: Tk | Toplevel) -> None:
        self.bg = Canvas(master, bg='#eef')
        self.bg.pack(fill='both')

        self.administrar = Button(master,
                                  text='Administrar',
                                  command=self.__gerir)
        self.administrar.place(x=100, y=100)

        self.vizualizar = Button(master,
                                 text='Ver Pokemons',
                                 command=self.__ver)
        self.vizualizar.place(x=200, y=100)

    def __ver(self: object):
        self.vizualizar.conf(state='disabled')
        View(self.__master)
        self.vizualizar.conf(state='normal')

    def __gerir(self: object):
        self.administrar.conf(state='disabled')
        Managment(self.__master)
        self.administrar.conf(state='normal')
