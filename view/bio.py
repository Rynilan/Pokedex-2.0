import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from mysql.connector import connect


# Função principal para criar a tela
def tela_de_biografia(numero: int):
    banco = connect(host='localhost', user='root', password='', database='Pokedex')
    cursor = banco.cursor()
    cursor.execute('select * from tb_pokemons where id = ' + str(numero))
    dados = cursor.fetchall()
    cursor.close()
    banco.close()
    del cursor, banco

    janela = tk.Tk()
    janela.title("𝚋𝚒𝚘𝚐𝚛𝚊𝚏𝚒𝚊")
    janela.geometry("1920x1080")
    tk.Frame(janela,bg='white').place(rely=0.10,relwidth=1,relheight=0.44)
    frame = tk.Frame(janela)
    frame.place(relx=0.1,rely=0.23,relheight=0.5)

    # Título centralizado
    
    titulo = tk.Label(janela, text="𝚋𝚒𝚘𝚐𝚛𝚊𝚏𝚒𝚊", font=("Helvetica",34), fg="black", bg="red")
    janela.config(bg="red")
    titulo.pack(pady=20)  # Adiciona título com margem

    # Tentar carregar imagem
    try:
        imagem = ImageTk.PhotoImage(Image.open(dados[0][4]))
        imagem_label = tk.Label(frame, image=imagem)
        imagem_label.image = imagem  # Manter referência à imagem
        imagem_label.pack(pady=10)  # Exibe imagem abaixo do título
    except Exception as e:
        messagebox.showwarning("Erro", "A imagem não pôde ser carregada!\n" +
                               "{}".format(e.__str__()))
        # Exibe um aviso se a imagem não for carregada

    # Texto da biografia alinhado à direita
    biografia_texto = list(dados[0])
    biografia_texto.pop(4)
    pp = tk.Label(janela,text=str(biografia_texto[0])+biografia_texto[1],fg='black',bg='white',font=("Consolas",30))
    pp.place(relx=0.38,rely=0.2)
    pp = tk.Label(janela,text="𝚃𝙸𝙿𝙾:"+str(biografia_texto[2])+biografia_texto[3],fg='black',bg='white',font=("Corbel",20))
    pp.place(relx=0.38,rely=0.3)
    pp = tk.Label(janela,text="𝙳𝙴𝙵𝙴𝚂𝙰:"+str(biografia_texto[4]),fg='black',bg='white',font=("Corbel",20))
    pp.place(relx=0.38,rely=0.4)
    pp = tk.Label(janela,text="𝙷𝙿:"+str(biografia_texto[5]),fg='black',bg='white',font=("Corbel",20))
    pp.place(relx=0.38,rely=0.5)
    pp = tk.Label(janela,text="𝙰𝚃𝙰𝚀𝚄𝙴:"+str(biografia_texto[6]),fg='black',bg='white',font=("Corbel",20))
    pp.place(relx=0.38,rely=0.6)
    pp = tk.Label(janela,text="𝙳𝙴𝚂𝙲𝚁𝙸𝙲𝙰𝙾:"+str(biografia_texto[7]),fg='black',bg='white',font=("Corbel",20))
    pp.place(relx=0.38,rely=0.7)
    # Frame para o botão de fechar
    fechar_frame = tk.Frame(janela, bg="black")  # Criar um frame com fundo preto
    fechar_frame.pack(side="bottom", pady=20, fill="x")  # Posicionar na parte inferior, ocupando toda a largura

    # Botão "Fechar" centralizado dentro do frame
    fechar_btn = tk.Button(fechar_frame, text="Fechar", command=janela.quit, font=("Helvetica", 14))
    fechar_btn.pack()  # Centraliza o botão dentro do frame
    ultima=tk.Button(janela,text='ultimo',command=ultimo)
    ultima.pack()

    primeiro= tk.Button(tela_biografia,text='primeiro',command=primeiro)
    primeiro.pack()
    def primeiro(tela_biografia,pokemon_atual):
        tela_biografia.destroy()
        tela_biografia(1)

    # Executar a janela
    janela.mainloop()

def ultimo (janela,pokemon_atual):
    janela.destroy()

    tela_biografia(151)

# Chama a função para mostrar a janela
if __name__ == '__main__':
    tela_biografia(1)
