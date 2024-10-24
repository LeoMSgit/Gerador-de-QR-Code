import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import os

# Função para criar o QR Code
def criar_qrcode(dados, nome_arquivo="myqrcode.png"):
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
    print(f"QR Code salvo como {nome_arquivo}")
    
    # Exibir QR Code no notebook
    return Image.open(nome_arquivo)

# Função para ler QR Code a partir de uma imagem
def ler_qrcode(nome_arquivo):
    img = cv2.imread(nome_arquivo)
    qr_codes = decode(img)
    return [qr_code.data.decode('utf-8') for qr_code in qr_codes]

# Solicitando os dados do usuário
dados = input("Digite o site ou texto para gerar o QR Code: ")

# Solicitando o nome do arquivo (padrão é myqrcode.png)
nome_arquivo = input("Digite o nome do arquivo (ou deixe em branco para usar 'myqrcode.png'): ")
if not nome_arquivo:
    nome_arquivo = "myqrcode.png"
elif not nome_arquivo.lower().endswith(".png"):
    nome_arquivo += ".png"

# Criar o QR Code e exibir no notebook
imagem_qr = criar_qrcode(dados, nome_arquivo)

# Exibir a imagem gerada no notebook
imagem_qr.show()

# Função opcional para mostrar a leitura do QR Code gerado
def testar_leitura_qrcode(nome_arquivo):
    print("Lendo QR Code gerado...")
    resultado = ler_qrcode(nome_arquivo)
    if resultado:
        print(f"Dados lidos do QR Code: {resultado}")
    else:
        print("Nenhum QR Code encontrado.")
