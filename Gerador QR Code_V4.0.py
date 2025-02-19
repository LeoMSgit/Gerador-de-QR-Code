import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import qrcode
import cv2
from pyzbar.pyzbar import decode
import os
import subprocess


def criar_qrcode(dados, nome_arquivo):
    try:
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
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criar QR Code: {e}")


def ler_qrcode(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        messagebox.showerror("Erro", "Arquivo não encontrado.")
        return []

    try:
        img = cv2.imread(nome_arquivo)
        qr_codes = decode(img)
        return [qr_code.data.decode('utf-8') for qr_code in qr_codes]
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler QR Code: {e}")
        return []


def gerar_qrcode():
    dados = entrada_dados.get().strip()
    nome_arquivo = entrada_nome_arquivo.get().strip()

    if not dados:
        messagebox.showerror("Erro", "Por favor, insira um site ou texto.")
        return

    if not nome_arquivo:
        nome_arquivo = "myqrcode.png"
    elif not nome_arquivo.lower().endswith(".png"):
        nome_arquivo += ".png"

    criar_qrcode(dados, nome_arquivo)
    messagebox.showinfo("Sucesso", f"QR Code criado e salvo como {nome_arquivo}.")


def mostrar_local_arquivo():
    nome_arquivo = entrada_nome_arquivo.get().strip() or "myqrcode.png"
    if os.path.exists(nome_arquivo):
        folder_path = os.path.realpath(os.path.dirname(nome_arquivo))
        subprocess.run(["explorer", folder_path])
    else:
        messagebox.showwarning("Aviso", "O arquivo QR Code não foi encontrado.")


root = tk.Tk()
root.title("Gerador e Leitor de QR Code")
root.geometry("390x360")
root.configure(bg='#f0f0f0')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 10), padding=6)

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, padx=20, pady=20)

ttk.Label(frame, text="Digite o site ou texto para gerar o QR Code:").grid(row=0, column=0, sticky="w")
entrada_dados = ttk.Entry(frame, width=40)
entrada_dados.grid(row=1, column=0, pady=10)

ttk.Label(frame, text="Digite o nome do arquivo (opcional):").grid(row=2, column=0, sticky="w")
entrada_nome_arquivo = ttk.Entry(frame, width=40)
entrada_nome_arquivo.grid(row=3, column=0, pady=10)

botao_gerar = ttk.Button(frame, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.grid(row=4, column=0, pady=5)

botao_mostrar_local = ttk.Button(frame, text="Mostrar local do arquivo", command=mostrar_local_arquivo)
botao_mostrar_local.grid(row=5, column=0, pady=5)


def abrir_linkedin(event):
    webbrowser.open("https://www.linkedin.com/in/leomsantos/")


def abrir_github(event):
    webbrowser.open("https://github.com/LeoMSgit")


# Marca d'água
tk.Label(root, text="Criado por Leonardo Miguel dos Santos", font=('Arial', 10), bg='#f0f0f0').grid(row=1, column=0, pady=(0, 1))

links_label = ttk.Label(root, text="LinkedIn: in/leomsantos | GitHub: @LeoMSgit",
                        foreground="blue", cursor="hand2", font=('Arial', 10, 'underline'), background="#f0f0f0")

links_label.bind("<Button-1>", lambda e: abrir_linkedin(e) if e.x < 140 else abrir_github(e))
links_label.grid(row=2, column=0, pady=(0, 2))


root.mainloop()