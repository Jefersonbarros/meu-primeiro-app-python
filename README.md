# 🚀 Meu Primeiro App com Streamlit e Python

> 🔗 **Acesse o app online aqui:** [https://meu-primeiro-app-python-jcuhbvzzhgqzhxtixyappn7.streamlit.app/)

Este é um projeto de estudo desenvolvido para explorar as capacidades do framework **Streamlit**, que permite criar interfaces web interativas utilizando apenas a linguagem **Python**.

## 📝 Descrição
O aplicativo é uma interface web simples onde o usuário pode interagir com campos de texto, botões e visualizar gráficos gerados dinamicamente. O objetivo principal foi entender como funciona o deploy de aplicações Python e a integração com o GitHub.

## 🛠️ Tecnologias Utilizadas
* **Python 3.14**: Linguagem base.
* **Streamlit**: Framework para a interface web.
* **Chocolatey**: Gerenciador de pacotes para Windows.
* **Pandas/Numpy**: Para manipulação de dados e gráficos.

## 📦 Configuração do Ambiente (Windows)

Para preparar o computador para este projeto, utilizei o **Chocolatey** para instalar as ferramentas de forma automatizada via PowerShell:

1. **Instalação do Chocolatey** (Executado como Administrador):
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

2. **Instalação do Python e Git**
```bash
choco install python git -y
```
## ⚙️ Como rodar o projeto localmente
1. **Clone este repositório**
```bash
git clone https://github.com/Jefersonbarros/meu-primeiro-app-python.git
```
2. **Entre na pasta do projeto**
```bash
cd meu-primeiro-app-python
```
3. **Instale o Streamlit**
```bash
pip install streamlit
```
4. **Execute o comando para abrir no navegador**
```bash
python -m streamlit run app.py
```
## 🧠 O que eu aprendi

* **Automação com Chocolatey**: Aprendi a utilizar gerenciadores de pacotes para instalar ferramentas de desenvolvimento (como Python e Git) de forma rápida, limpa e padronizada via terminal no Windows.
* **Configuração de ambiente Python**: Pratiquei a preparação do ambiente de desenvolvimento, incluindo o uso do `pip` para gerenciamento de bibliotecas e pacotes.
* **Interface Web sem HTML/CSS**: Descobri o poder do framework **Streamlit**, criando elementos complexos de interface (botões, campos de texto e gráficos) utilizando exclusivamente a lógica de programação em Python.
* **Versionamento com Git**: Aprendi o fluxo de trabalho essencial com Git, desde a inicialização do repositório local até o commit e a publicação (push) para o GitHub.
* **Hospedagem na Nuvem**: Realizei o deploy de uma aplicação real através do **Streamlit Cloud**, garantindo que o projeto esteja acessível online via URL pública.

---
**Desenvolvido por Jeferson** — *Para fins de estudo e prática de desenvolvimento Python.*
