from view.mainframe import MainFrame
from tkinter import Label, Entry, Button, Frame, Canvas
from PIL import ImageTk


class PokedexScreen(MainFrame):
    def _create_things(self, **kwargs) -> None:

        # Preparando e adicionando imagem de fundo.
        from model.crud import SEPARADOR
        from os import path
        self.background = Canvas(self._mainframe)
        imagem = ImageTk.PhotoImage(
            file=path.realpath(__file__).removesuffix(
                'view' + SEPARADOR + 'index.py'
            ) + 'assets' + SEPARADOR + 'background' +
                SEPARADOR + 'background.png'
        )
        self.background.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.background.create_image(0, 0, image=imagem)
        self.imagem = imagem

        screen_frame = Frame(self._mainframe)
        screen_frame.place(relwidth=1, relheight=1)

        title_label = Label(
                screen_frame,
                text='Bem vindo à Pokedex',
                font=('Arial', 24, 'bold'),
                bg='#fff'
        )
        title_label.pack(pady=20)

        search_label = Label(screen_frame, text='Digite o nome do Pokémon:',
                             bg='#fff')
        search_label.pack(pady=5)

        search_entry = Entry(screen_frame, font=('Arial', 14))
        search_entry.pack(pady=18)

        def search_pokemon():
            pokemon_name = search_entry.get()
            print(f'Pesquisando Pokémon: {pokemon_name}')

        search_button = Button(
                screen_frame, text='Pesquisar', font=('Arial', 14),
                command=search_pokemon
        )
        search_button.pack(pady=20)

        result_label = Label(
                screen_frame,
                text='Resultado: Nenhum Pokémon encontrado',
                font=('Arial', 14),
                bg='#fff'
        )
        result_label.pack(pady=20)

        botao_ver = Button(screen_frame, text='Ver Pokemons',
                           command=lambda:
                               self._tela._load(self._tela._ver, None, None)
                           )
        botao_ver.pack(pady=10)
        botao_gerir = Button(screen_frame, text='Gerir Pokemons',
                             command=lambda:
                             self._tela._load(
                                 self._tela._gerenciar, None, None
                             ))
        botao_gerir.pack(pady=10)
