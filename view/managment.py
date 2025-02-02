from view.mainframe import MainFrame
from tkinter import (Label, Button, Frame, Text,
                     Scrollbar, ttk, messagebox, END)
from model.crud import (
        campos, conectar, tipos, regioes, select_join, insert, update, delete
)
from assets.classes.Custom_Entry import Entry
from control.validadores.validacao_nome import validar_nome
from control.validadores.validacao_numero import validar_numero


class Managment(MainFrame):
    def _create_things(self: object, **kwargs) -> None:

        try:
            tuple(elemento.close() for elemento in conectar())
        except Exception as e:  # Detecta qualquer erro
            from tkinter import messagebox
            messagebox.showerror('ERROR', 'ServerError: algum problema ocorr' +
                                 'eu com a\nconexão com o banco de dados - ' +
                                 e)
            return

        # Criação dos campos para inserção de dados do usuário.
        frame_campos = Frame(self._mainframe)
        frame_campos.place(x=10, y=10, relwidth=0.45, relheight=0.9)
        self.texto_numero = Label(frame_campos, text='Numero')
        self.campo_numero = Entry(frame_campos)
        self.texto_numero.pack(pady=(1, 3))
        self.campo_numero.pack(pady=(0, 1))
        self.texto_nome = Label(frame_campos, text='Nome')
        self.campo_nome = Entry(frame_campos)
        self.texto_nome.pack(pady=(1, 3))
        self.campo_nome.pack(pady=(0, 1))
        self.texto_regiao = Label(frame_campos, text='Regiao')
        self.campo_regiao = ttk.Combobox(frame_campos, state='readonly',
                                         values=regioes())
        self.texto_regiao.pack(pady=(1, 3))
        self.campo_regiao.pack(pady=(0, 1))
        self.texto_tipo1 = Label(frame_campos, text='Tipo1')
        tipos_without_null = tipos()
        tipos_without_null.remove('NULL')
        self.campo_tipo1 = ttk.Combobox(frame_campos, state='readonly',
                                        values=tipos_without_null)
        self.texto_tipo1.pack(pady=(1, 3))
        self.campo_tipo1.pack(pady=(0, 1))
        self.texto_tipo2 = Label(frame_campos, text='Tipo2')
        self.campo_tipo2 = ttk.Combobox(frame_campos, state='readonly',
                                        values=tipos())
        self.texto_tipo2.pack(pady=(1, 3))
        self.campo_tipo2.pack(pady=(0, 1))
        self.texto_foto = Label(frame_campos, text='Foto')
        self.campo_foto = Entry(frame_campos)
        self.texto_foto.pack(pady=(1, 3))
        self.campo_foto.pack(pady=(0, 1))
        self.texto_vida = Label(frame_campos, text='Vida')
        self.campo_vida = Entry(frame_campos)
        self.texto_vida.pack(pady=(1, 3))
        self.campo_vida.pack(pady=(0, 1))
        self.texto_defesa = Label(frame_campos, text='Defesa')
        self.campo_defesa = Entry(frame_campos)
        self.texto_defesa.pack(pady=(1, 3))
        self.campo_defesa.pack(pady=(0, 1))
        self.texto_ataque = Label(frame_campos, text='Ataque')
        self.campo_ataque = Entry(frame_campos)
        self.texto_ataque.pack(pady=(1, 3))
        self.campo_ataque.pack(pady=(0, 1))
        self.texto_descricao = Label(frame_campos, text='Descricao')
        self.campo_descricao = Text(frame_campos)
        self.texto_descricao.pack(pady=(1, 3))
        self.campo_descricao.pack(pady=(0, 1))

        # Criação dos botões parqa as ações especificadas.
        frame_acao = Frame(self._mainframe, bg='white')
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
        self.pesquisa = Button(frame_acao, text='Pesquisar',
                               command=self.pesquisar)
        self.pesquisa.pack(fill='x')

        # Criação da tabela e suas barras de rolagem.
        self.frame_tabela = Frame(self._mainframe)
        self.frame_tabela.place(relx=0.55,
                                rely=0.25,
                                relheight=0.7,
                                relwidth=0.45)
        self.tabela = ttk.Treeview()
        self.yscroll: Scrollbar = Scrollbar(self.frame_tabela,
                                            orient='vertical')
        self.yscroll.place(relx=0.9, rely=0, relwidth=0.05, relheight=0.9)
        self.xscroll: Scrollbar = Scrollbar(self.frame_tabela,
                                            orient='horizontal')
        self.xscroll.place(relx=0, rely=0.95, relwidth=0.9, relheight=0.04)
        self.tabela: ttk.Treeview = ttk.Treeview(
            self.frame_tabela,
            show='headings',
            selectmode='browse',
            yscrollcommand=self.yscroll.set,
            xscrollcommand=self.xscroll.set,
            columns=campos())
        self.tabela.place(relx=0, rely=0, relheight=0.92, relwidth=0.9)
        self.yscroll.configure(command=self.tabela.yview)
        self.xscroll.configure(command=self.tabela.xview)
        self.por_colunas()

    def pegar_dados(self: object) -> tuple[any]:
        from tkinter import messagebox

        try:
            if self.campo_tipo2.get() == self.campo_tipo1.get():
                raise ValueError("Tipo primário e secundário iguais.")
            if self.campo_tipo1.get() == '':
                raise ValueError("Tipo1 não pode ser nulo.")
            return (self.campo_numero.custom_get(validar_numero),
                    self.campo_nome.custom_get(validar_nome),
                    self.campo_descricao.get('1.0', 'end-1c').strip(),
                    self.campo_vida.custom_get(validar_numero),
                    self.campo_ataque.custom_get(validar_numero),
                    self.campo_defesa.custom_get(validar_numero),
                    self.campo_tipo1.get(),
                    self.campo_tipo2.get() if self.campo_tipo2.get() != '' else
                    'NULL',
                    self.campo_foto.get().strip(),
                    self.campo_regiao.get())
        except ValueError as error:
            messagebox.showerror('ERRO', error)

    def insert(self: object) -> None:
        try:
            insert(self.pegar_dados(),
                   (
                   'numero_geral', 'nome', 'descricao', 'vida', 'ataque', 'defesa',
                   'tipo1', 'tipo2', 'foto', 'regiao'
                   )
                   )
            self.atualizar_tabela()
        except Exception as erro:
            messagebox.showerror('ERRO', erro)

    def update(self: object) -> None:
        update(self.tabela.selection(), self.pegar_dados(), (
               'numero', 'nome', 'descrição', 'vida', 'ataque', 'defesa',
               'tipo1', 'tipo2', 'foto', 'região'
               ))
        self.atualizar_tabela()

    def delete(self: object) -> None:
        delete(int(self.tabela.selection()[0][1:], 16))
        self.atualizar_tabela()

    def _desenhar(self: object) -> None:
        pass

    def pesquisar(self: object) -> None:
        colunas = list()
        valores = list()
        for key, widget in self.campos.items():
            key: str
            if key.startswith('campo '):
                colunas.append(key[key.find(' ') + 1:])
                if type(widget) is Text:
                    valores.append(self.campos.get(key).get(1.0, END))
                else:
                    valores.append(self.campos.get(key).get())
                valores[-1]: str
                if (not valores[-1] or valores[-1] is None or
                        valores[-1] == '\n'):
                    valores.pop()
                    colunas.pop()
        self.atualizar_tabela()
        for campo in campos():
            self.tabela.heading(campo.lower(), text=campo.capitalize())
        for elemento in select_join(True, tuple(colunas), tuple(valores)):
            self.tabela.insert('', END, values=elemento)

    def por_colunas(self: object) -> None:
        ''' Método que irá por na tabela os mesmos registros existentes
            no banco de dados nesse GUI. '''
        tabela = self.tabela
        for campo in campos():
            tabela.heading(campo.lower(), text=campo.capitalize())

        for elemento in select_join():
            tabela.insert('', END, values=elemento)

    def atualizar_tabela(self: object) -> None:
        ''' Método que recriará a tabela sempre que houver atualização. '''
        self.frame_tabela.destroy()
        self.frame_tabela = Frame(self._mainframe)
        self.frame_tabela.place(relx=0.55,
                                rely=0.25,
                                relheight=0.7,
                                relwidth=0.45)
        self.tabela = ttk.Treeview()
        self.yscroll: Scrollbar = Scrollbar(self.frame_tabela,
                                            orient='vertical')
        self.yscroll.place(relx=0.9, rely=0, relwidth=0.05, relheight=0.9)
        self.xscroll: Scrollbar = Scrollbar(self.frame_tabela,
                                            orient='horizontal')
        self.xscroll.place(relx=0, rely=0.95, relwidth=0.9, relheight=0.04)
        self.tabela: ttk.Treeview = ttk.Treeview(
            self.frame_tabela,
            show='headings',
            selectmode='browse',
            yscrollcommand=self.yscroll.set,
            xscrollcommand=self.xscroll.set,
            columns=campos())
        self.tabela.place(relx=0, rely=0, relheight=0.92, relwidth=0.9)
        self.yscroll.configure(command=self.tabela.yview)
        self.xscroll.configure(command=self.tabela.xview)
        self.por_colunas()
