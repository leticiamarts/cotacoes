from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")


navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dólar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoDolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') #ao inspecionar elemento, tem como ver o atributo q qr pegar, nesse caso, o data-value

navegador.get("https://www.google.com.br/")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoEuro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacaoOuro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
cotacaoOuro = cotacaoOuro.replace(",", ".")

navegador.quit()

df = pd.read_excel("produtos.xlsx")
print(df)

df.loc[df['Moeda'] == 'Dólar', 'Cotação'] = float(cotacaoDolar)
df.loc[df['Moeda'] == 'Euro', 'Cotação'] = float(cotacaoEuro)
df.loc[df['Moeda'] == 'Ouro', 'Cotação'] = float(cotacaoOuro)

df['Preço de Compra'] = df['Preço Original'] * df['Cotação']

df['Preço de Venda'] = df['Preço de Compra'] * df['Margem']

df.to_excel("produtos.xlsx", index=False)

print(df)