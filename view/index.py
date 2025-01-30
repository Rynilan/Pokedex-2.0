from tkinter import Label, Entry, Button, Frame, Canvas, Tk
from PIL import Image, ImageTk
import os

class PokedexScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokedex")
        self.root.geometry("800x500")

        # Criar um Frame para a interface
        self.mainframe = Frame(root)
        self.mainframe.pack(fill="both", expand=True)

        # Adicionar Imagem de Fundo
        self._set_background()

        # Criar elementos da interface
        self._create_things()

    def _set_background(self):
        """Carrega e define uma imagem como fundo da tela"""
        caminho_imagem = os.path.join(os.getcwd(), "assets", "background", "Pokemons ofc.jpg")

        if not os.path.exists(caminho_imagem):
            print(f"Imagem de fundo não encontrada: {caminho_imagem}")
            return  # Se a imagem não for encontrada, evita erro

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
        # Frame para os elementos da interface
        self.ui_frame = Frame(self.mainframe, bg='#ffffff', bd=2)
        self.ui_frame.place(relx=0.5, rely=0.3, anchor="center", width=400, height=200)

        title_label = Label(self.ui_frame, text='Bem-vindo à Pokedex',
                            font=('Arial', 18, 'bold'), bg='#ffffff')
        title_label.pack(pady=10)

        search_label = Label(self.ui_frame, text='Digite o nome do Pokémon:',
                             bg='#ffffff', font=('Arial', 12))
        search_label.pack()

        self.search_entry = Entry(self.ui_frame, font=('Arial', 14), width=25)
        self.search_entry.pack(pady=5)

        search_button = Button(self.ui_frame, text='Pesquisar', font=('Arial', 14),
                               command=self.search_pokemon)
        search_button.pack(pady=5)

    def search_pokemon(self):
        """Função para buscar Pokémon (futura implementação)"""
        pokemon_name = self.search_entry.get().strip()
        if not pokemon_name:
            print("Nenhum nome digitado.")
            return
        print(f'Pesquisando Pokémon: {pokemon_name}')

# Criar e rodar a aplicação
if __name__ == "__main__":
    root = Tk()
    app = PokedexScreen(root)
    root.mainloop()

