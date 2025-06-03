import pyautogui  # Automação da interface gráfica
import time      # Controle de pausas e delays
import pandas    # Manipulação de dados em tabelas

pyautogui.PAUSE = 1  # Tempo de pausa entre cada comando do PyAutoGUI

# Passo 1: Abrir o navegador e acessar o sistema da empresa

pyautogui.press("win")  # Abre o menu iniciar
pyautogui.write("chrome")  # Digita "chrome"
pyautogui.press("enter")  # Abre o navegador

# Acessa a URL do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)  # Aguarda o carregamento do site

# Passo 2: Fazer login 

pyautogui.click(x=760, y=506)  # Clica no campo de email
pyautogui.write("lucas.andrade932@gmail.com")  # Digita o email

pyautogui.press("tab")  # Vai para o campo de senha
pyautogui.write("Andrade@2025!")  # Digita a senha

pyautogui.press("tab")  # Vai para o botão de login
pyautogui.press("enter")  # Clica no botão de login

time.sleep(3)  # Espera o sistema carregar após login

# Passo 3: Importar a base de dados

tabela = pandas.read_csv("produtos.csv")  # Lê os dados do CSV

# Passo 4: Cadastrar os produtos no sistema

for linha in tabela.index:
    pyautogui.click(x=648, y=364)  # Clica no primeiro campo do formulário

    # Preenche os campos do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Só preenche o campo de observações se houver algo
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")  # Envia o formulário

    pyautogui.scroll(10000)  # Rola a página pra cima antes do próximo cadastro
