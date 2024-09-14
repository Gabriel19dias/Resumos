Resumidor de Texto com Google Gemini AI
Este projeto é uma aplicação de desktop que utiliza a API do Google Gemini para resumir textos e gerar perguntas relacionadas, facilitando o processo de estudo. A aplicação foi desenvolvida em Python, utilizando a biblioteca ttkbootstrap para a interface gráfica e google.generativeai para a integração com a API do Google Gemini.

Funcionalidades
Geração de Resumos: Insira um texto e obtenha um resumo detalhado.
Criação de Perguntas: O sistema gera perguntas com base no texto resumido, ajudando na revisão e estudo.
Tecnologias Utilizadas
Python: Linguagem de programação usada para o desenvolvimento.
ttkbootstrap: Biblioteca para criar uma interface gráfica moderna e com tema escuro.
google.generativeai: API do Google Gemini para geração de conteúdo e resumos.
Requisitos
Antes de executar o projeto, você precisa ter o Python instalado em sua máquina. Além disso, instale as seguintes dependências:

bash
Copiar código
pip install ttkbootstrap google-generativeai
Configuração da API
Para usar a API do Google Gemini, você precisa de uma chave de API. Substitua.

Como Executar
Clone este repositório para o seu ambiente local:

bash
Copiar código
git clone <URL_DO_REPOSITORIO>
Navegue para o diretório do projeto:

bash
Copiar código
cd <DIRETORIO_DO_PROJETO>
Execute o script Python:

bash
Copiar código
python <NOME_DO_ARQUIVO>.py
Isso abrirá a janela da aplicação onde você poderá inserir o texto para resumir e gerar perguntas.

Estrutura do Código
gerar_resumo(): Função que lida com a geração de resumos e perguntas utilizando a API do Google Gemini.
main(): Função que configura e executa a interface gráfica usando ttkbootstrap.
