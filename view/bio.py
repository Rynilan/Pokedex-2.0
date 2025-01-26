from tkinter import messagebox, Frame, Label, Button
from model.crud import select_join
from view.mainframe import MainFrame


# Função principal para criar a tela
class Biografia(MainFrame):
    def _create_things(
        self: object,
        **kwargs
    ) -> None:
        ''' Parâmetro de número é necessário, numero=int'''

        # Botões de navegação dentre os pokemons.
        self.botoes = Frame(self._mainframe)
        self.botoes.pack(side='bottom', fill='x')
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
        self.proximo.grid(row=1, column=0)
        self.anterior = Button(self.botoes, text='◂',
                               command=lambda: self.trocar_pokemon(
                                self.pokemon_atual - 1
                               ))
        self.anterior.grid(row=1, column=2)

        # Campos que virão a ter dados alterados
        self.imagem = Label(self._mainframe)
        self.imagem.place(relx=0.1, y=0.1)
        self.titulo = Label(self._mainframe, name='nome')
        self.titulo.pack(side='top', fill='x')

        self.dados = Frame(self._mainframe)
        self.dados.place(relx=0.35, rely=0.1, relwidth=0.65, relheight=0.8)
        self.tipo = Label(self.dados, text='Tipos: ', name='tipo')
        self.tipo.pack()
        self.regiao = Label(self.dados, text='Região: ', name='região')
        self.regiao.pack()
        self.atributos = Label(self.dados, name='atributos',
                               text='Vida: %s\nDefesa: %s\nAtaque: %s\n')
        self.atributos.pack()
        self.descricao = Label(self.dados, text='', justify='left',
                               wraplength=300)
        self.descricao.pack()

        self.colocar_dados(kwargs.get('numero'))

    def colocar_dados(self: object, numero: int) -> None:
        try:
            dados = tuple(str(dado) for dado in select_join(
                                True, ('numero_geral', ), (str(numero), )
            )[0])
        except Exception as error:
            messagebox.showwarning('ERRO', error)
            return

        # Tentar carregar imagem
        try:
            from PIL import Image, ImageTk

            imagem = ImageTk.PhotoImage(Image.open(dados[4]).resize(
                (300, 300)
            ))
            self.imagem.config(image=imagem)
            self.imagem.image = imagem
        except Exception as e:
            messagebox.showwarning("Erro",
                                   "Não foi possível carregar a imagem\n" +
                                   "{}".format(e.__str__()))

        self.titulo['text'] = dados[0] + '. ' + dados[1]
        self.tipo['text'] = str(
            self.tipo['text'] + dados[2] +
            (' e ' + dados[3] if dados[3] != 'NULL' else '') + '.'
        )
        self.regiao['text'] += dados[8]
        self.atributos['text'] = self.atributos['text'] % (dados[5:8])
        self.descricao['text'] = str(
                dados[9] if dados[9] != 'NULL' else 'Não há descrição.'
        )
        self.pokemon_atual = numero

    def trocar_pokemon(self: object, proximo: int):
        self.colocar_dados(proximo)
