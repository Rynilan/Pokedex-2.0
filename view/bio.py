from tkinter import messagebox, Frame, Label, Button, CENTER
from model.crud import select_join
from view.mainframe import MainFrame
from PIL import Image, ImageTk  # Importado no topo para evitar exceções tardias


class Biografia(MainFrame):
    def _create_things(self, **kwargs) -> None:
        ''' Parâmetro de número é necessário, numero=int'''

        # Preparando e adicionando imagem de fundo.
        self._image('background')

        # Botões de navegação entre os Pokémon
        self.botoes = Frame(self._mainframe)
        self.botoes.place(relx=0.75, rely=0.90, anchor=CENTER)

        self.ultimo = Button(self.botoes, text='▾',
                             command=lambda: self.trocar_pokemon(151))
        self.ultimo.grid(row=2, column=1)

        self.primeiro = Button(self.botoes, text='▴',
                               command=lambda: self.trocar_pokemon(1))
        self.primeiro.grid(row=0, column=1)

        self.proximo = Button(self.botoes, text='▸',
                              command=lambda: self.trocar_pokemon(
                                self.pokemon_atual + 1
                              ))
        self.proximo.grid(row=1, column=2)

        self.anterior = Button(self.botoes, text='◂',
                               command=lambda: self.trocar_pokemon(
                                self.pokemon_atual - 1
                               ))
        self.anterior.grid(row=1, column=0)

        # Criando os elementos visuais
        self.imagem = Label(self._mainframe)
        self.imagem.place(relx=0.15, rely=0.4)

        self.titulo = Label(self._mainframe)
        self.titulo.place(relx=0.1, rely=0.9)

        self.dados = Frame(self._mainframe)
        self.dados.place(relx=0.57, rely=0.35, relwidth=0.35, relheight=0.3)

        self.tipo = Label(self.dados)
        self.tipo.pack()

        self.regiao = Label(self.dados)
        self.regiao.pack()

        self.atributos = Label(self.dados)
        self.atributos.pack()

        self.descricao = Label(self.dados, text='', justify='left',
                               wraplength=350)  # Ajuste no wraplength
        self.descricao.pack()

        self.colocar_dados(kwargs.get('numero'))

    def colocar_dados(self, numero: int) -> None:
        try:
            dados = tuple(str(dado) for dado in select_join(
                True, ('numero_geral',), (str(numero),)
            )[0])
        except Exception as error:
            messagebox.showwarning('ERRO', str(error))  # Convertendo erro para string
            return

        # Tentar carregar imagem
        try:
            imagem = Image.open(dados[4]).resize((200, 200))
            imagem = ImageTk.PhotoImage(imagem)

            self.imagem.config(image=imagem)
            self.imagem.image = imagem  # Referência para evitar garbage collection
        except Exception as e:
            messagebox.showwarning("Erro",
                                   f"Não foi possível carregar a imagem\n{str(e)}")

        # Atualizando os textos
        self.titulo['text'] = f"{dados[0]}. {dados[1]}"
        self.tipo['text'] = f"Tipo(s): {dados[2]}" + (f" e {dados[3]}" if dados[3] != 'NULL' else '') + "."
        self.regiao['text'] = f"Região: {dados[8]}."
        self.atributos['text'] = f"Vida: {dados[5]}\nDefesa: {dados[6]}\nAtaque: {dados[7]}"
        self.descricao['text'] = "   " + (dados[9] if dados[9] != 'NULL' else "Não há descrição.")

        self.pokemon_atual = numero  # Atualiza o Pokémon atual

    def trocar_pokemon(self, proximo: int):
        self.colocar_dados(proximo)
