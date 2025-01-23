from view.tela import Tela
from tkinter import Toplevel, Tk, Button, Frame, Scrollbar, END
from tkinter import ttk
from model.crud import campos, select_join


class View(Tela):
    def _html(self: object, master: Tk | Toplevel) -> None:
        top = Toplevel(master)
        top.resizable(False, False)
        top.geometry('768x432')
        top.title('Pokemons')
        self.top = top
        self.sair = Button(top, command=top.destroy, text='Sair')
        self.sair.pack(side='bottom', fill='x')

        self.frame_tabela = Frame(self.top)
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
        for campo in campos():
            self.tabela.heading(campo.lower(), text=campo.capitalize())

        for elemento in select_join():
            self.tabela.insert('', END, values=elemento)

    def _desenhar(self: object) -> None:
        pass
