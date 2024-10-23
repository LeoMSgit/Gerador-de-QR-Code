import qrcode
import cv2
from pyzbar.pyzbar import decode

# Função para criar QR Code
def criar_qrcode(dados, nome_arquivo):
    # Gerar o QR Code com os dados
    qr = qrcode.QRCode(
        version=1,  # Tamanho do QR Code (quanto maior o valor, mais informação cabe)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=10,  # Tamanho de cada quadrado do código
        border=4,  # Tamanho da borda
    )
    qr.add_data(dados)
    qr.make(fit=True)

    # Criar a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')
    img.save(nome_arquivo)
    print(f"QR Code salvo como {nome_arquivo}")

# Função para ler QR Code a partir de uma imagem
def ler_qrcode(nome_arquivo):
    # Carregar a imagem do QR Code
    img = cv2.imread(nome_arquivo)

    # Usar pyzbar para decodificar o QR Code
    qr_codes = decode(img)
    
    for qr_code in qr_codes:
        dados = qr_code.data.decode('utf-8')
        print(f"Dados do QR Code: {dados}")

# Exemplo de uso:
nome_arquivo_qrcode = "meu_qrcode.png"

# Solicitar que o usuário insira o site ou texto a ser transformado em QR Code
dados_para_qrcode = input("Digite o site ou texto que deseja transformar em QR Code: ")

# Criar o QR Code com os dados fornecidos pelo usuário
criar_qrcode(dados_para_qrcode, nome_arquivo_qrcode)

# Ler o QR Code criado
ler_qrcode(nome_arquivo_qrcode)
