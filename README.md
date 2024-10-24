# Gerador e Leitor de QR Code Customizável

Este é um programa simples para gerar e ler QR Codes, desenvolvido em Python com uma interface gráfica (GUI) utilizando o `tkinter`. O programa permite que o usuário insira um texto ou URL, que será convertido em um QR Code e salvo como uma imagem `.png`. O QR Code pode ser lido posteriormente para recuperar o texto ou URL.

## Funcionalidades

- **Gerar QR Code**: Insira um texto ou URL e gere um QR Code correspondente.
- **Ler QR Code**: Abra uma imagem de QR Code e decodifique-a para recuperar o conteúdo.
- **Interface Gráfica**: Interface simples e intuitiva, construída com `tkinter` e estilizada com o tema `clam`.
- **Explorar Local de Salvamento**: Abra o explorador de arquivos diretamente na pasta onde o QR Code foi salvo.

## Tecnologias Utilizadas

- **Python 3.12**
- **Tkinter**: Para a interface gráfica.
- **qrcode**: Biblioteca para a geração de QR Codes.
- **pyzbar**: Biblioteca para leitura e decodificação de QR Codes.
- **OpenCV (cv2)**: Para processamento de imagens e leitura de QR Codes.

## Requisitos do Sistema

- Windows 10 ou superior.

## Instruções de Instalação

Se você deseja apenas usar o programa, basta baixar o executável disponível no repositório e executá-lo diretamente. Não é necessário instalar nenhuma biblioteca ou dependência, pois todas estão incluídas no executável.

### Instruções de Uso

 - Versão Google Colab (Jupyter) disponível [AQUI](https://colab.research.google.com/github/LeoMSgit/Extrator-de-Parametros-Analise-Hemograma-e-Bioquimico/blob/main/Google%20Colab%20(Cloud)%20Extrator_de_Par%C3%A2metros_An%C3%A1lise_de_Hemograma_e_Bioqu%C3%ADmico.ipynb).

   <br />
   <br />


1. Baixe o arquivo executável do software via Repositório GitHub [AQUI](https://github.com/LeoMSgit/Gerador-de-QR-Code/releases/tag/release_2) ou o arquivo compactado via Google Drive [AQUI](https://drive.google.com/file/d/1WWjTwp622IpxmoITRkyvgdv1_H4z-G_N/view?usp=sharing).

2. Execute o arquivo 'GeradorQRCode.exe'.

3. O programa abrirá uma interface gráfica com as seguintes opções:
   - **Digite o site ou texto**: Insira o texto ou URL que você deseja converter em QR Code.
   - **Gerar QR Code**: Clique neste botão para gerar e salvar o QR Code como `meu_qrcode.png`.
   - **Mostrar local do arquivo**: Abre o explorador de arquivos na pasta onde o QR Code foi salvo.

## Possíveis Problemas de Execução

- **Bloqueio em Computadores Corporativos**: Em ambientes corporativos, o programa pode ser bloqueado por políticas de segurança, como o Windows Defender SmartScreen ou antivírus. Se isso acontecer:
  - Entre em contato com o administrador de TI para verificar a execução do programa.
  - Considere assinar digitalmente o executável para evitar bloqueios por segurança.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* e enviar *pull requests* para melhorar este projeto.

1. Fork o repositório.
2. Crie uma *branch* (`git checkout -b feature/nova-feature`).
3. Faça suas modificações e *commits* (`git commit -m 'Adiciona nova feature'`).
4. Envie o *pull request*.

## **Apoio Técnico**
Se houver qualquer dúvida ou problema com o programa, entre em contato com o suporte técnico através do e-mail **leoms-98@hotmail.com** ou no GitHub em **@leomsgit**.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
