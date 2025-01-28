from tkinter import Button, Frame, Scrollbar, Entry, END
from tkinter import ttk
from model.crud import campos, select_join
from view.mainframe import MainFrame


class View(MainFrame):
    def _create_things(self: object) -> None:

        self.pesquisa_campo = Entry(self._mainframe)
        self.pesquisa_campo.place(relx=0.1, rely=0.1, relwidth=0.5)
        self.pesquisa_opcao = ttk.Combobox(self._mainframe, state='readonly',
                                           values=campos())
        self.pesquisa_opcao.place(relx=0.6, rely=0.1, relwidth=0.3)
        self.pesquisa_botao = Button(self._mainframe, text='Pesquisar',
                                     command=self.pesquisar)
        self.pesquisa_botao.place(relx=0.1, rely=0.15, relwidth=0.8)

        self.biografia = Button(self._mainframe, text='Detalhes',
                                command=lambda:
                                    self._tela._load(
                                        self._mainframe,
                                        None,
                                        None,
                                        numero=int(self.tabela.selection()[1:])
                                    ))
        self.biografia.place(relx=0.2, rely=0.25, relwidth=0.6)

        self.parametros = None
        self.criar_tabela()

    def criar_tabela(self: object) -> None:
        self.frame_tabela = Frame(self._mainframe)
        self.frame_tabela.place(relx=0.15,
                                rely=0.35,
                                relheight=0.6,
                                relwidth=0.7)
        self.tabela = ttk.Treeview()
        self.yscroll: Scrollbar = Scrollbar(self.frame_tabela,
                                            orient='vertical')
        self.yscroll.place(relx=0.9, rely=0, relwidth=0.03, relheight=0.9)
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
        self.tabela.place(relx=0, rely=0, relheight=0.92, relwidth=0.88)
        self.yscroll.configure(command=self.tabela.yview)
        self.xscroll.configure(command=self.tabela.xview)
        for campo in campos():
            self.tabela.heading(campo.lower(), text=campo.capitalize())

        if not self.parametros:
            for elemento in select_join():
                self.tabela.insert('', END, values=elemento)
        else:
            for elemento in select_join(*self.parametros):
                self.tabela.insert('', END, values=elemento)
            self.parametros = None

    def pesquisar(self: object) -> None:
        self.parametros = (
            True,
            (self.pesquisa_opcao.get(), ),
            (self.pesquisa_campo.get(), )
        )
        self.frame_tabela.destroy()
        self.criar_tabela()
