from view.mainframe import MainFrame
from tkinter import Label, Entry, Button, Frame

class PokedexScreen(MainFrame):
    def __init__(self, *args, **kwargs):
        # Inicialização da classe MainFrame, que gerencia a janela e o frame principal
        super().__init__(*args, **kwargs)

    def _create_things(self, **kwargs):
        '''Método obrigatório que cria os widgets na tela'''

        # Frame principal dentro do _mainframe para organização
        screen_frame = Frame(self._mainframe)
        screen_frame.place(relwidth=1, relheight=1)

        title_label = Label(
            screen_frame,
            text="Bem-vindo à Pokédex!",
            font=("Arial", 24, "bold"),
            bg="#fff"
        )
        title_label.pack(pady=20)

        # Campo de texto para inserir o nome do Pokémon
        search_label = Label(screen_frame, text="Digite o nome do Pokémon:", bg="#fff")
        search_label.pack(pady=5)

        search_entry = Entry(screen_frame, font=("Arial", 14))
        search_entry.pack(pady=10)

        # Função de callback para quando o botão de pesquisa for pressionado
        def search_pokemon():
            pokemon_name = search_entry.get()
            print(f"Pesquisando Pokémon: {pokemon_name}")
            # e exibir informações sobre ele na tela.

        # Botão para pesquisar o Pokémon
        search_button = Button(
            screen_frame, text="Pesquisar", font=("Arial", 14),
            command=search_pokemon
        )
        search_button.pack(pady=20)

        # Exemplo de como mostrar um Pokémon depois de pesquisa (placeholder)
        result_label = Label(
            screen_frame,
            text="Resultado: Nenhum Pokémon encontrado",
            font=("Arial", 14),
            bg="#fff"
        )
        result_label.pack(pady=20)

