from view.mainframe import MainFrame
from tkinter import Label, Entry, Button, Frame


class PokedexScreen(MainFrame):
    def _create_things(self, **kwargs) -> None:

        screen_frame = Frame(self.mainframe)
        screen_frame.place(relwidth=1, relheight=1)

        title_label = Label(
                screen_frame,
                text='Bem vindo à Pokedex',
                font=('Arial', 24, 'bold'),
                bg='#fff'
        )
        title_label.pack(pady=20)

        search_label = Label(screen_frame, text='Digite o nome do Pokémon:', bg='#fff')
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
