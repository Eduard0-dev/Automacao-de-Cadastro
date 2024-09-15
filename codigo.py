# Passo a passo;

# 1. abrir o sistema da empresa;
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
        # abrir o navegador
        # entrar no site do sistema

# 2. Fazer login no site;
# 3. Abrir a base de dados dos produtos;
# 4. Cadastrar um produto;
# 5. Repetir ate o final da lista;

import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("Enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")

time.sleep(3)
pyautogui.click(x=914, y=357)
pyautogui.write("eduardo@gmail.com.br")
pyautogui.press("tab")
pyautogui.write("SENHA")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=902, y=235)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(int(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(float(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
