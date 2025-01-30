from tkinter import messagebox
from view.tela import Master
from model.estruturação_do_banco import banco_de_dados

def main() -> None:
    try:
        banco_de_dados()
        
        # Verifica se a biblioteca PIL está instalada
        try:
            import PIL
            _ = PIL.__version__  # Apenas para garantir que a importação foi bem-sucedida
        except ModuleNotFoundError as import_erro:
            messagebox.showwarning('Aviso', 'Imagens não poderão ser carregadas;\n' + str(import_erro))

    except Exception as general_error:
        messagebox.showerror('ERRO', str(general_error))

    finally:
        Master()

if __name__ == "__main__":
    main()
