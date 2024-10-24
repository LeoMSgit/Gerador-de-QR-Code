Manual de Usuário - Gerador QR Code Customizável (Versão Executável)
Índice:
Introdução
Requisitos do Sistema
Instalação
Como Usar
Geração de QR Code
Exibição do Local do Arquivo
Funcionamento
Solução de Problemas
Créditos
Introdução
O Gerador QR Code Customizável é uma ferramenta simples e fácil de usar que permite a criação de QR Codes personalizados a partir de textos ou URLs inseridos pelo usuário. Ele também oferece a opção de visualizar a localização do arquivo gerado diretamente no explorador de arquivos.

Este manual tem como objetivo orientar os usuários a utilizar a versão executável do programa, que já inclui todas as bibliotecas necessárias.

Requisitos do Sistema
Sistema Operacional: Windows 7 ou superior
Memória RAM: 2 GB (recomendado)
Armazenamento: 50 MB de espaço livre
Resolução de Tela: 1024x768 ou superior
Instalação
Baixe o arquivo executável do programa (GeradorQRCode.exe) do repositório ou site onde está hospedado.
Não há necessidade de instalar pacotes adicionais ou bibliotecas, pois todas as dependências estão incluídas no executável.
Simplesmente execute o arquivo baixado para iniciar o programa.
Como Usar
Geração de QR Code
Abra o programa clicando no arquivo executável (GeradorQRCode.exe).
Digite o texto ou URL que deseja converter em um QR Code na caixa de entrada principal.
Exemplo: https://github.com/LeoMSgit ou qualquer outro texto.
Clique no botão "Gerar QR Code".
Uma janela de confirmação será exibida informando que o QR Code foi gerado com sucesso e salvo como meu_qrcode.png no diretório atual do programa.
Exibição do Local do Arquivo
Para verificar onde o QR Code foi salvo no seu computador, clique no botão "Mostrar local do arquivo".
O explorador de arquivos será aberto diretamente na pasta onde o arquivo meu_qrcode.png está salvo.
Você pode então visualizar, mover ou compartilhar o arquivo.
Funcionamento
Geração de QR Code: O programa usa a biblioteca qrcode para gerar a imagem do QR Code com base no texto inserido pelo usuário.
Exibição de Arquivo: Usa comandos do sistema operacional para abrir a pasta onde o QR Code foi salvo.
O QR Code gerado é salvo com o nome meu_qrcode.png na pasta onde o programa está sendo executado.

Solução de Problemas
O arquivo meu_qrcode.png não foi encontrado:

Verifique se você realmente gerou o QR Code clicando no botão "Gerar QR Code".
Caso o arquivo tenha sido removido ou movido, gere um novo QR Code.
Erro ao abrir o explorador de arquivos:

Verifique se o arquivo meu_qrcode.png ainda está no diretório original.
Certifique-se de que seu sistema operacional está funcionando corretamente.
O programa não abre:

Certifique-se de que o arquivo executável foi baixado corretamente.
Verifique se você possui os requisitos mínimos de sistema.
Créditos
Desenvolvido por: Leonardo Miguel dos Santos
Bibliotecas utilizadas:
qrcode para geração de QR Codes
pyzbar e cv2 para leitura de QR Codes (caso adicione uma funcionalidade futura)
Tkinter para a interface gráfica do usuário (GUI)
Para mais informações ou relatórios de bugs, visite o repositório oficial: GitHub.
