from tkinter import Tk, Button, Frame
from view.mainframe import MainFrame
from view.bio import Biografia


class Master:
    def __init__(self: object) -> None:
        # Instância da janela (Tk) e mainframe (frame principal).
        self._master = Tk()
        self._mainframe = Frame(self._master)

        # Declaração dos objetos mainframe.
        # (Falta atribuir objeto).
        self._gerenciar: MainFrame
        self._ver: MainFrame
        self._biografia: MainFrame = Biografia(
            self._master, self._mainframe, self
        )
        self._index: MainFrame

        # Criação dos botões de sair e menu principal
        self.__buttons = Frame(self._master)
        self.__buttons.place(relwidth=1, relheight=0.05, rely=0.95)
        self.__main_menu = Button(self.__buttons, command=self._home,
                                  text='Menu principal')
        self.__main_menu.pack(side='right', expand=True, pady=0)
        self.__exit = Button(self.__buttons, command=self._master.destroy,
                             text='Sair')
        self.__exit.pack(side='right', expand=True, pady=0)

        # Posicionamento do mainframe.
        self._mainframe.place(relwidth=1, relheight=0.95)
        self._home()
        self._master.mainloop()

    def _home(self: object, called_by: object = None) -> None:
        if called_by:
            called_by._kill_own_widgets()
        self.__main_menu.config(state='disabled')
        self._html()

    def _html(self: object) -> None:
        # self._index.create_things()
        self._biografia._create_things(numero=1)

    def _css(self: object) -> None:
        # Adicione os outros atributos a para o design nesse método.
        BG1 = '#fff'
        for name, child in self._mainframe.children.items():
            child.config(bg=BG1)
