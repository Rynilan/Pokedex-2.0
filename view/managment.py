from view.tela import Tela
from tkinter import Toplevel, Tk, Label, Entry, Button, Frame, Text, ttk, END
from model.crud import campos, conectar, tipos, regioes, select_join


class Managment(Tela):
    def _html(self: object, master: Tk | Toplevel) -> None:
        top = Toplevel(master)
        top.resizable(False, False)
        top.geometry('720x680')
        top.title('Gerenciamento de pokemons')
        self.top = top

        # Testa a conexão com o banco.
        try:
            tuple(elemento.close() for elemento in conectar())
        except:  # Detecta qualquer erro
            from tkinter import messagebox
            messagebox.showerror('ERROR', 'ServerError: algum problema ocorr' +
                                 'eu com a\nconexão com o banco de dados.')
            return

        frame_campos = Frame(top)
        frame_campos.place(x=10, y=10, relwidth=0.45, relheight=0.9)
        self.frame_campos = frame_campos
        campos_widgets = dict()
        for coluna in tuple(campo.capitalize()for campo in campos()):
            campos_widgets['label ' + coluna.lower()] = Label(
                frame_campos, text=coluna + ':'
            )
            campos_widgets.get('label ' + coluna.lower()).pack(side='top')
            if coluna in ('Descrição', 'Tipo_1', 'Tipo_2', 'Região'):
                if coluna == 'Descrição':
                    continue
                else:
                    campos_widgets['campo ' + coluna.lower()] = ttk.Combobox(
                        frame_campos, state='readonly',
                        values=tipos() if coluna != 'Região' else regioes()
                    )
                    campos_widgets.get('campo ' + coluna.lower()).pack()
            else:
                campos_widgets['campo ' + coluna.lower()] = Entry(frame_campos)
                campos_widgets.get('campo ' + coluna.lower()).pack(side='top')
        campos_widgets['campo descrição'] = Text(frame_campos,
                                                 height=12,
                                                 width=40)
        campos_widgets.get('campo descrição').pack()
        self.campos = campos

        frame_acao = Frame(top, bg='white')
        frame_acao.place(relx=0.55, y=10, relwidth=0.45, relheight=0.2)
        self.registrar = Button(frame_acao, text='Registrar',
                                command=self.insert)
        self.registrar.pack(fill='x')
        self.atualizar = Button(frame_acao, text='Atualizar',
                                command=self.update)
        self.atualizar.pack(fill='x')
        self.excluir = Button(frame_acao, text='Excluir',
                              command=self.delete)
        self.excluir.pack(fill='x')

    def gerar_tabela(self: object) -> None:
        pass

    def css(self: object, widgets) -> None:
        for widget in widgets:
            tipo = type(widget)

    def _desenhar(self: object) -> None:
        pass

    def insert(self: object) -> None:
        pass

    def update(self: object) -> None:
        pass

    def delete(self: object) -> None:
        pass

    def por_colunas(self: object) -> None:
        ''' Método que irá por na tabela os mesmos registros existentes
            no banco de dados nesse GUI. '''
        tabela = self.tabela
        tabela.heading('id', text='Id')
        tabela.heading('personagem', text='Personagem')

        for elemento in select_join():
            tabela.insert('', END, values=elemento)

    def atualizar_tabela(self: object) -> None:
        ''' Método que recriará a tabela sempre que houver atualização. '''
        self.tabela.destroy()
        self.tabela: ttk.Treeview = ttk.Treeview(
            self.frame_tabela,
            show='headings',
            selectmode='browse',
            yscrollcommand=self.tabela_scroll.set,
            columns=campos())
        self.tabela.place(relx=0, rely=0, relheight=0.9, relwidth=0.95)
        self.por_colunas()
