from tkinter import Label, Entry, Button, Frame, Canvas, Tk
from PIL import Image, ImageTk
import os

class PokedexScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokedex")
        self.root.geometry("800x500")  # Ajuste conforme o tamanho da imagem

        # Criar um Frame para a interface
        self.mainframe = Frame(root)
        self.mainframe.pack(fill="both", expand=True)

        # ** Adicionar Imagem de Fundo **
        self._set_background()

        # Criar elementos da interface
        self._create_things()

    def _set_background(self):
        """Carrega e define uma imagem como fundo da tela"""
        caminho_imagem = os.path.join(os.getcwd(), "assets", "background", "Pokemons ofc.jpg")

        # Abrir a imagem e converter para o formato do Tkinter
        imagem = Image.open(caminho_imagem)
        imagem = imagem.resize((800, 500), Image.LANCZOS)  # Ajuste para o tamanho da janela
        self.bg_image = ImageTk.PhotoImage(imagem)  # Armazena a referência na classe

        # Criar Canvas para exibir a imagem
        self.background = Canvas(self.mainframe, width=800, height=500)
        self.background.pack(fill="both", expand=True)
        self.background.create_image(0, 0, image=self.bg_image, anchor="nw")  # Posiciona no topo esquerdo

    def _create_things(self):
        """Cria os componentes da interface"""
        title_label = Label(self.mainframe, text='Bem-vindo à Pokedex',
                            font=('Arial', 24, 'bold'), bg='#fff')
        title_label.place(relx=0.5, rely=0.1, anchor="center")

        search_label = Label(self.mainframe, text='Digite o nome do Pokémon:', bg='#fff')
        search_label.place(relx=0.5, rely=0.3, anchor="center")

        search_entry = Entry(self.mainframe, font=('Arial', 14))
        search_entry.place(relx=0.5, rely=0.4, anchor="center")

        def search_pokemon():
            pokemon_name = search_entry.get()
            print(f'Pesquisando Pokémon: {pokemon_name}')

        search_button = Button(self.mainframe, text='Pesquisar', font=('Arial', 14),
                               command=search_pokemon)
        search_button.place(relx=0.5, rely=0.5, anchor="center")

# Criar e rodar a aplicação
if __name__ == "__main__":
    root = Tk()
    app = PokedexScreen(root)
    root.mainloop()
