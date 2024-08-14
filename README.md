# Automação de Mensagens no WhatsApp com Python

Este projeto automatiza o envio de mensagens pelo WhatsApp Web usando Python, OpenPyXL para leitura de dados de um arquivo Excel, e PyAutoGUI para automação da interface do navegador.

## Funcionalidades
- ### Leitura de Dados de Clientes: O script lê um arquivo Excel (Exemplo.xlsx) que contém os nomes e números de telefone dos clientes.
- ### Envio Automático de Mensagens: Com base nas informações lidas, ele abre o WhatsApp Web, insere o número de telefone e a mensagem personalizada, e envia automaticamente.
- ### Tratamento de Erros: Nomes e números de telefone ausentes são ignorados, e erros durante o envio das mensagens são registrados em um arquivo erros.csv.
- ### Automação da Interface Gráfica:PyAutoGUI é usado para clicar em botões e interagir com a interface do WhatsApp Web automaticamente.
## Pré-requisitos
- Python 3.x: Certifique-se de ter Python instalado.

- Pacotes Necessários:

    - openpyxl: Para manipulação do arquivo Excel.
    - pyautogui: Para automação da interface gráfica.
    - webbrowser: Para abrir o WhatsApp Web no navegador.
Você pode instalar os pacotes necessários usando:
```
bash
pip install openpyxl pyautogui
```
 ## Arquivo Excel: O arquivo Exemplo.xlsx deve conter uma planilha com pelo menos as seguintes colunas:

- Coluna 3: Nome do cliente.
- Coluna 4: Número de telefone (somente números, sem formatação).
## Como Usar
* Configuração Inicial:

Certifique-se de ter o arquivo Exemplo.xlsx na mesma pasta do script Python.
Inclua uma imagem da seta usada para envio da mensagem (chamada seta.jpg), capturada da interface do WhatsApp Web.
Executar o Script:

* Execute o script no terminal com:
```
bash
python seu_script.py
```
* Envio das Mensagens:

O WhatsApp Web será aberto, e o script enviará uma mensagem para cada número de telefone encontrado no arquivo Excel.
Caso o script não consiga enviar a mensagem, ele registrará o erro no arquivo erros.csv.
## Personalização
* Mensagem: A mensagem enviada é personalizada para cada cliente usando o nome extraído do arquivo Excel. Você pode editar a mensagem diretamente no script para se adequar às suas necessidades.

* Tempo de Espera: Ajuste o tempo de espera (sleep) se a execução for muito rápida ou muito lenta, dependendo da velocidade da sua conexão ou da resposta do WhatsApp Web.

## Tratamento de Erros
* Se o script não conseguir localizar a imagem da seta, ele tenta clicar em uma coordenada fixa.
* Telefones inválidos ou que não possuem WhatsApp serão registrados no arquivo erros.csv.
## Avisos
* Automação: Este script depende da interface do WhatsApp Web e da automação de cliques com o PyAutoGUI. Mudanças na interface do WhatsApp Web podem quebrar o funcionamento do script.
* Uso Ético: Certifique-se de usar este script de acordo com as políticas do WhatsApp e com o consentimento dos destinatários.
 Esse README ajuda a documentar o propósito, funcionamento, e detalhes de configuração do seu script. Se precisar de mais ajustes, estou à disposição!
