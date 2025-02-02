from tkinter import messagebox, Frame, Label, Button, CENTER
from model.crud import select_join
from view.mainframe import MainFrame
from PIL import Image, ImageTk


class Biografia(MainFrame):
    def _create_things(self, **kwargs) -> None:
        ''' Parâmetro de número é necessário, numero=int'''

        # Preparando e adicionando imagem de fundo.
        self._image('background')

        # Botões de navegação entre os Pokémon
        self.ultimo = Button(self._mainframe, text='▾', name='botoesl_ultimo',
                             command=lambda: self.trocar_pokemon(151))
        self.ultimo.place(relx=0.59, rely=0.74, relwidth=0.12, relheight=0.075)

        self.primeiro = Button(self._mainframe, text='▴',
                               name='botoesl_primeiro',
                               command=lambda: self.trocar_pokemon(1))
        self.primeiro.place(relx=0.797, rely=0.74,
                            relwidth=0.12, relheight=0.075)

        self.proximo = Button(self._mainframe, text='▸',
                              name='botoesr_proximo',
                              command=lambda: self.trocar_pokemon(
                                self.pokemon_atual + 1
                              ))
        self.proximo.place(relx=0.753, rely=0.89, relwidth=0.06,
                           relheight=0.075)

        self.anterior = Button(self._mainframe, text='◂',
                               name='botoesr_anterior',
                               command=lambda: self.trocar_pokemon(
                                self.pokemon_atual - 1
                               ))
        self.anterior.place(relheight=0.075, relx=0.69, rely=0.89,
                            relwidth=0.06)

        # Criando os elementos visuais
        self.imagem = Label(self._mainframe)
        self.imagem.place(relx=0.15, rely=0.4)

        self.titulo = Label(self._mainframe, name='nome')
        self.titulo.place(relx=0.085, rely=0.9)

        self.dados = Frame(self._mainframe, name='dados_frame')
        self.dados.place(relx=0.57, rely=0.4, relwidth=0.17, relheight=0.20)

        self.tipo = Label(self.dados, name='dados_tipo')
        self.tipo.pack(anchor='w')

        self.regiao = Label(self.dados, name='dados_regiao')
        self.regiao.pack(anchor='w')

        self.atributos = Label(self.dados, name='dados_atributos')
        self.atributos.pack(anchor='w')

        self.dados_2 = Frame(self._mainframe, name='dados_frame2')
        self.dados_2.place(relx=0.765, rely=0.4, relwidth=0.17, relheight=0.20)

        self.descricao = Label(self.dados_2, text='', justify='center',
                               name='dados_descricao', wraplength=160)
        self.descricao.place(relx=0.5, rely=0.5, relwidth=1, relheight=1,
                             anchor=CENTER)

        self.colocar_dados(kwargs.get('numero'))

    def colocar_dados(self, numero: int) -> None:
        try:
            dados = tuple(str(dado) for dado in select_join(
                True, ('numero_geral',), (str(numero),)
            )[0])
        except Exception as error:
            messagebox.showwarning('ERRO', str(error))
            return

        # Tentar carregar imagem
        try:
            imagem = Image.open(dados[4]).resize((200, 200))
            imagem = ImageTk.PhotoImage(imagem)

            self.imagem.config(image=imagem)
            self.imagem.image = imagem
        except Exception as e:
            messagebox.showwarning("Erro",
                                   "Não foi possível carregar a imagem" +
                                   f"\n{str(e)}")

        # Atualizando os textos
        self.titulo['text'] = f"{dados[0]}. {dados[1]}"
        self.tipo['text'] = f" Tipo(s): {dados[2]}" + (
            f" e {dados[3]}" if dados[3] != 'NULL' else ''
        ) + "."
        self.regiao['text'] = f" Região: {dados[8]}."
        self.atributos['text'] = str(f"Vida: {dados[5]}\nDefesa: {dados[6]}" +
                                     f"\nAtaque: {dados[7]}")
        self.descricao['text'] = "   " + (dados[9] if dados[9] != 'NULL' else
                                          "Não há descrição.")

        self.pokemon_atual = numero  # Atualiza o Pokémon atual

    def trocar_pokemon(self, proximo: int):
       self.colocar_dados(proximo)
