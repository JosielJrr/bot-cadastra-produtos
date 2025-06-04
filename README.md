# ⚙️ Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em um sistema web usando a lib PyAutoGUI. A ideia é facilitar tarefas repetitivas, preenchendo formulários com base em uma planilha CSV, sem precisar inserir dados manualmente.

## 🚀 Como funciona

1. Abre o navegador (Google Chrome) pelo menu iniciar
2. Acessa o site do sistema da empresa
3. Faz login com email e senha
4. Lê os dados do arquivo `produtos.csv`
5. Preenche e envia o formulário para cada produto da planilha

## 📋 Requisitos

- Python 3
- `pyautogui`
- `pandas`

Instala as libs com:

```bash
pip install pyautogui pandas
```

## ▶️ Como usar

1. Certifique-se que o arquivo `produtos.csv` está no mesmo diretório do script, com as colunas: `codigo, marca, tipo, categoria, preco_unitario, custo, obs`.

2. Execute o script. Ele vai abrir o navegador, logar e cadastrar tudo automaticamente.

3. Ajuste as coordenadas dos cliques conforme a resolução e o layout do seu sistema — isso é fundamental para funcionar.

## ⚠️ Atenção

- A automação depende das posições exatas dos elementos na tela. Qualquer mudança no layout do sistema ou resolução do monitor pode exigir ajustes no script.

- Os dados de login usados são fictícios.

> Projeto criado na **Jornada Python** da [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao).
