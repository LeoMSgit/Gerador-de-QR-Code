import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import qrcode
import cv2
from pyzbar.pyzbar import decode
import os
import subprocess


# Função para criar QR Code
def criar_qrcode(dados, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(nome_arquivo)


# Função para ler QR Code a partir de uma imagem
def ler_qrcode(nome_arquivo):
    img = cv2.imread(nome_arquivo)
    qr_codes = decode(img)
    return [qr_code.data.decode('utf-8') for qr_code in qr_codes]


# Função para gerar o QR Code a partir da entrada do usuário
def gerar_qrcode():
    dados = entrada_dados.get()
    nome_arquivo = entrada_nome_arquivo.get()

    if not dados:
        messagebox.showerror("Erro", "Por favor, insira um site ou texto.")
        return

    # Usar nome padrão caso o campo esteja em branco
    if not nome_arquivo:
        nome_arquivo = "myqrcode.png"
    else:
        # Adicionar a extensão .png se o nome do arquivo não terminar com .png
        if not nome_arquivo.lower().endswith(".png"):
            nome_arquivo += ".png"

    criar_qrcode(dados, nome_arquivo)
    messagebox.showinfo("Sucesso", f"QR Code criado e salvo como {nome_arquivo}.")


# Função para mostrar o local do arquivo
def mostrar_local_arquivo():
    nome_arquivo = entrada_nome_arquivo.get() or "myqrcode.png"  # Usar nome inserido ou padrão
    if os.path.exists(nome_arquivo):
        folder_path = os.path.dirname(os.path.abspath(nome_arquivo))
        subprocess.run(f'explorer "{folder_path}"')  # Abre o Windows Explorer na pasta
    else:
        messagebox.showwarning("Aviso", "O arquivo QR Code não foi encontrado.")


# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador e Leitor de QR Code")
janela.geometry("400x350")
janela.style = ttk.Style(janela)
janela.style.theme_use("clam")

# Criar um frame com fundo bege
frame_fundo = ttk.Frame(janela, padding=20)
frame_fundo.pack(expand=True, fill='both')
frame_fundo.configure(style="TFrame")

# Configurando a cor de fundo do frame
janela.tk_setPalette(background='beige')

# Criação dos widgets
label = ttk.Label(frame_fundo, text="Digite o site ou texto para gerar o QR Code:")
label.pack(pady=10)

entrada_dados = ttk.Entry(frame_fundo, width=40)
entrada_dados.pack(pady=10)

label_nome_arquivo = ttk.Label(frame_fundo, text="Digite o nome do arquivo (opcional):")
label_nome_arquivo.pack(pady=10)

entrada_nome_arquivo = ttk.Entry(frame_fundo, width=40)
entrada_nome_arquivo.pack(pady=10)

botao_gerar = ttk.Button(frame_fundo, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.pack(pady=5)

botao_mostrar_local = ttk.Button(frame_fundo, text="Mostrar local do arquivo", command=mostrar_local_arquivo)
botao_mostrar_local.pack(pady=5)

# Executar o loop principal
janela.mainloop()
