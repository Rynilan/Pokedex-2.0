from tkinter import Frame, Label, Entry, Button, Text, Toplevel, messagebox
from tkinter import ttk, Scrollbar
from control.validadores.validacao_numero import validar_numero
from control.formatadores.formatador_nome import formatar_nome
from model.banco_dados import conectar, select_join, insert, update, delete
from model.regioes_tipos import regioes, tipos, campos


class Managment(Tela):
    def _html(self: object, master: Tk | Toplevel) -> None:
        top = Toplevel(master)
        top.resizable(False, False)
        top.geometry('1300x700')
        top.title('Gerenciamento de Pokemons')
        self.top = top
        
        self.sair = Button(top, command=top.destroy, text='Sair')
        self.sair.pack(side='bottom', fill='x')

        # Testa a conexão com o banco
        self._testar_conexao_banco()

        # Criação dos campos para inserção de dados do usuário
        self._criar_campos(top)

        # Criação dos botões para as ações
        self._criar_botoes(top)

        # Criação da tabela e suas barras de rolagem
        self._criar_tabela()

    def _testar_conexao_banco(self):
        try:
            tuple(elemento.close() for elemento in conectar())
        except Exception as e:
            messagebox.showerror('ERROR', f'ServerError: Algum problema ocorreu com a conexão com o banco de dados - {e}')
            return

    def _criar_campos(self, top):
        """Criação dos campos para inserir dados"""
        frame_campos = Frame(top)
        frame_campos.place(x=10, y=10, relwidth=0.45, relheight=0.9)

        self.texto_numero = Label(frame_campos, text='Número')
        self.campo_numero = Entry(frame_campos)
        self.texto_numero.pack(pady=(2, 5))
        self.campo_numero.pack(pady=(1, 2))

        self.texto_nome = Label(frame_campos, text='Nome')
        self.campo_nome = Entry(frame_campos)
        self.texto_nome.pack(pady=(2, 5))
        self.campo_nome.pack(pady=(1, 2))

        self.texto_regiao = Label(frame_campos, text='Região')
        self.campo_regiao = ttk.Combobox(frame_campos, state='readonly', values=regioes())
        self.texto_regiao.pack(pady=(2, 5))
        self.campo_regiao.pack(pady=(1, 2))

        self.texto_tipo1 = Label(frame_campos, text='Tipo1')
        tipos_without_null = [tipo for tipo in tipos() if tipo != 'NULL']
        self.campo_tipo1 = ttk.Combobox(frame_campos, state='readonly', values=tipos_without_null)
        self.texto_tipo1.pack(pady=(2, 5))
        self.campo_tipo1.pack(pady=(1, 2))

        self.texto_tipo2 = Label(frame_campos, text='Tipo2')
        self.campo_tipo2 = ttk.Combobox(frame_campos, state='readonly', values=tipos())
        self.texto_tipo2.pack(pady=(2, 5))
        self.campo_tipo2.pack(pady=(1, 2))

        self.texto_foto = Label(frame_campos, text='Foto')
        self.campo_foto = Entry(frame_campos)
        self.texto_foto.pack(pady=(2, 5))
        self.campo_foto.pack(pady=(1, 2))

        self.texto_vida = Label(frame_campos, text='Vida')
        self.campo_vida = Entry(frame_campos)
        self.texto_vida.pack(pady=(2, 5))
        self.campo_vida.pack(pady=(1, 2))

        self.texto_defesa = Label(frame_campos, text='Defesa')
        self.campo_defesa = Entry(frame_campos)
        self.texto_defesa.pack(pady=(2, 5))
        self.campo_defesa.pack(pady=(1, 2))

        self.texto_ataque = Label(frame_campos, text='Ataque')
        self.campo_ataque = Entry(frame_campos)
        self.texto_ataque.pack(pady=(2, 5))
        self.campo_ataque.pack(pady=(1, 2))

        self.texto_descricao = Label(frame_campos, text='Descrição')
        self.campo_descricao = Text(frame_campos)
        self.texto_descricao.pack(pady=(2, 5))
        self.campo_descricao.pack(pady=(4, 0))

    def _criar_botoes(self, top):
        """Criação dos botões para ações do usuário"""
        frame_acao = Frame(top, bg='white')
        frame_acao.place(relx=0.55, y=10, relwidth=0.45, relheight=0.2)

        self.registrar = Button(frame_acao, text='Registrar', command=self.insert)
        self.registrar.pack(fill='x')

        self.atualizar = Button(frame_acao, text='Atualizar', command=self.update)
        self.atualizar.pack(fill='x')

        self.excluir = Button(frame_acao, text='Excluir', command=self.delete)
        self.excluir.pack(fill='x')

        self.pesquisa = Button(frame_acao, text='Pesquisar', command=self.pesquisar)
        self.pesquisa.pack(fill='x')

    def _criar_tabela(self):
        """Criação da tabela de visualização de dados"""
        self.frame_tabela = Frame(self.top)
        self.frame_tabela.place(relx=0.55, rely=0.25, relheight=0.7, relwidth=0.45)

        self.tabela = ttk.Treeview(self.frame_tabela, show='headings', selectmode='browse', columns=campos())
        self.tabela.place(relx=0, rely=0, relheight=0.92, relwidth=0.9)

        self.yscroll = Scrollbar(self.frame_tabela, orient='vertical', command=self.tabela.yview)
        self.yscroll.place(relx=0.9, rely=0, relwidth=0.05, relheight=0.9)

        self.xscroll = Scrollbar(self.frame_tabela, orient='horizontal', command=self.tabela.xview)
        self.xscroll.place(relx=0, rely=0.95, relwidth=0.9, relheight=0.04)

        self.tabela.configure(yscrollcommand=self.yscroll.set, xscrollcommand=self.xscroll.set)
        self.por_colunas()

    def pegar_dados(self: object) -> tuple:
        """Pega os dados inseridos pelo usuário"""
        from tkinter import messagebox

        try:
            return (
                self.campo_numero.custom_get(validar_numero),
                self.campo_nome.custom_get(validar_nome, formatar_nome),
                self.campo_descricao.get('1.0', 'end-1c'),
                self.campo_vida.custom_get(validar_numero),
                self.campo_ataque.custom_get(validar_numero),
                self.campo_defesa.custom_get(validar_numero),
                self.campo_tipo1.get(),
                self.campo_tipo2.get(),
                self.campo_foto.get(),
                self.campo_regiao.get()
            )
        except ValueError as error:
            messagebox.showerror('ERRO', f'Erro de valor: {error}')

    def insert(self: object) -> None:
        """Inserir dados no banco de dados"""
        insert(self.pegar_dados(), ('numero', 'nome', 'descrição', 'vida', 'ataque', 'defesa', 'tipo1', 'tipo2', 'foto', 'região'))

    def update(self: object) -> None:
        """Atualizar dados no banco de dados"""
        update(self.tabela.selection(), self.pegar_dados(), ('numero', 'nome', 'descrição', 'vida', 'ataque', 'defesa', 'tipo1', 'tipo2', 'foto', 'região'))
        self.atualizar_tabela()

    def delete(self: object) -> None:
        """Excluir dados do banco de dados"""
        delete(self.tabela.selection())
        self.atualizar_tabela()

    def _desenhar(self: object) -> None:
        pass

    def pesquisar(self: object) -> None:
        """Pesquisar dados no banco de dados"""
        colunas = []
        valores = []
        for key, widget in self.campos.items():
            if key.startswith('campo '):
                colunas.append(key.split(' ')[1])
                valores.append(self.campos[key].get('1.0', 'end-1c') if isinstance(widget, Text) else self.campos[key].get())

        self.atualizar_tabela()
        for campo in campos():
            self.tabela.heading(campo.lower(), text=campo.capitalize())

        for elemento in select_join(True, tuple(colunas), tuple(valores)):
            self.tabela.insert('', 'end', values=elemento)

    def por_colunas(self: object) -> None:
        """Adicionar os dados na tabela"""
        for campo in campos():
            self.tabela.heading(campo.lower(), text=campo.capitalize())

        for elemento in select_join():
            self.tabela.insert('', 'end', values=elemento)

    def atualizar_tabela(self: object) -> None:
        """Atualiza a tabela"""
        self.tabela.destroy()
        self._criar_tabela()
