from tkinter import Tk, Button, Frame, Label
from view.mainframe import MainFrame
from view.bio import Biografia
from view.index import PokedexScreen
from view.view import View
from view.managment import Managment
from os import path
from model.crud import SEPARADOR
from PIL import ImageTk, Image


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
        args = (self._master, self._mainframe, self)
        self._gerenciar: MainFrame = Managment(*args, 'manage')
        self._ver: MainFrame = View(*args, 'manage')
        self._biografia: MainFrame = Biografia(*args, 'background')
        self._index: MainFrame = PokedexScreen(*args, 'start')
        del args

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

        # Posicionamento do mainframe.e
        self._mainframe.place(relwidth=1, relheight=0.95)
        self.__background = Label(self._mainframe, name='background_label')
        self.__background.place(x=0, y=0, relwidth=1, relheight=1)
        self._load(self._index, self.__main_menu.config, {'state': 'disabled'})
        self._master.mainloop()

    def __selfdestruct(self: object) -> None:
        ''' Destrói todo widget que estiver no self._mainframe.'''
        elementos = tuple(self._mainframe.children.values())
        for child in elementos:
            if child._name != 'background_label':
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
        self._image(main._bg)
        self._css_recursivo(self._master)

    def _image(self: object, imagem: str) -> None:
        if not imagem:
            return
        imagem = ImageTk.PhotoImage(Image.open(path.dirname(
                                    path.realpath(__file__)
                                    ).removesuffix('view')
            + 'assets' + SEPARADOR + 'background'
            + SEPARADOR + imagem + '.png').resize((1024, 712)))
        self.__background.config(image=imagem)
        self.__background.image = imagem

    def __css(self: object, child: object) -> None:
        ''' Aplica o estilo dado ao widget especificado. '''
        # Adicione os outros atributos a para o design nesse método.
        FONT = ('Times New Roman', '14')
        BG = '#fff'
        FG = '#000'
        CAMPOS = ('botoesr', 'botoesl', 'nome', 'dados')
        try:
            for campo in CAMPOS:
                if child._name.startswith(campo):
                    match (campo):
                        case 'botoesr':
                            child.config(bg='#db4aff')
                            child.config(fg=FG, font=FONT)
                        case 'botoesl':
                            child.config(bg='#ffa922')
                            child.config(fg=FG, font=FONT)
                        case 'nome':
                            child.config(bg='#3fbd4a')
                            child.config(fg='#000', font=FONT + ('bold', ))
                        case 'dados':
                            child.config(bg='#b3fff5')
                            child.config(fg=FG, font=(FONT[0], '10', 'bold'),
                                         justify='left')
                    return
            child.config(bg=BG)
            child.config(fg=FG, font=FONT)
        except Exception:
            pass

    def _css_recursivo(
        self: object, objeto: Frame | Tk, nivel: int = 0
    ) -> None:
        ''' Dado um widget inicial (esperado instância de Tk) e ignorado o
            nível inicialmente irá iterar pelos filhos do 'pai' e aplicar
            estilo, irá olhar os filhos dos filhos do pai (até cinco níveis)
            caso este tenha.'''
        if type(objeto) is Tk:
            objeto.geometry("1024x712")
            objeto.title("pokedex SENAC")
            objeto.resizable(False, False)
        if nivel > 5:
            print(objeto.config)
            raise RecursionError('Recursion limit acheived, max is 5.')
        self.__css(objeto)
        for name, child in objeto.children.items():
            self.__css(child)
            tipo = type(child)
            if (tipo is Frame or tipo is Tk) and child is not objeto:
                self._css_recursivo(child, nivel + 1)
