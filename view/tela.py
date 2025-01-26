from tkinter import Tk, Button, Frame
from view.mainframe import MainFrame
from view.bio import Biografia


class Master:
    def __init__(self: object) -> None:
        ''' Cria instância de Tk e de Frame (master e mainframe),
        instância os objetos do tipo MainFrame (os que irão criar
        widgets no mainframe) cria botões de navegação (sair e tela
        incial) e carrega o index, além de por tudo no laço principal.'''

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
        self.__main_menu = Button(
            self.__buttons, text='Menu principal',
            command=lambda: self._load(
                self._index, self.__main_menu.config, 'disabled'
            ),
        )
        self.__main_menu.pack(side='right', expand=True, pady=0)
        self.__exit = Button(self.__buttons, command=self._master.destroy,
                             text='Sair')
        self.__exit.pack(side='right', expand=True, pady=0)

        # Posicionamento do mainframe.
        self._mainframe.place(relwidth=1, relheight=0.95)
        self._load(self._index, self.__main_menu.config, 'disabled')
        self._master.mainloop()

    def __selfdestruct(self: object) -> None:
        ''' Destrói todo widget que estiver no self._mainframe.'''
        for name, child in self._mainframe.children.items():
            child.destroy()
        self.__main_menu.config(state='normal')

    def _load(
        self: object,
        main: MainFrame,
        function: callable = None,
        args: any = None,
        **kwargs
    ) -> None:
        ''' Responsável por chamar função 'extra' no momento de carregar
            tela (function) dando os parâmetros necessários para ela (args) e
            carregar wigets do MainFrame dado (main._create_things) dando
            parâmtros específicos necessários (kwargs).'''
        if bool(self._mainframe.children):
            self.__selfdestruct()
        if bool(kwargs):
            main._create_things(**kwargs)
        else:
            main._create_things()
        if function:
            if args:
                function(args)
            else:
                function()
        self._css_recursivo(self._master)

    def __css(self: object, child: object) -> None:
        ''' Aplica o estilo dado ao widget especificado. '''
        # Adicione os outros atributos a para o design nesse método.
        BG1 = '#fff'
        child.config(bg=BG1)

    def _css_recursivo(
        self: object, objeto: Frame | Tk, nivel: int = 0
    ) -> None:
        ''' Dado um widget inicial (esperado instância de Tk) e ignorado o
            nível inicialmente irá iterar pelos filhos do 'pai' e aplicar 
            estilo, irá olhar os filhos dos filhos do pai (até cinco níveis)
            caso este tenha.'''
        if nivel > 5:
            print(objeto.config)
            raise RecursionError('Recursion limit acheived, max is 5.')
        self.__css(objeto)
        for name, child in objeto.children.items():
            self.__css(child)
            tipo = type(child)
            if (tipo is Frame or tipo is Tk) and child is not objeto:
                self._css_recursivo(child, nivel + 1)
