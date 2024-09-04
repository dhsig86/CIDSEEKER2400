from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Configura o caminho para o ChromeDriver (substitua pelo caminho correto)
CHROME_DRIVER_PATH = r'C:\caminho\para\chromedriver.exe'

# Inicializa o serviço do ChromeDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Acessa a página inicial dos procedimentos
url = "URL_DA_TABELA"
driver.get(url)

# Espera carregar a página
time.sleep(2)

# Função para coletar informações de cada procedimento
def coletar_dados_procedimento(link):
    driver.get(link)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Coleta o código do procedimento
    codigo_procedimento = soup.find('span', {'id': 'codigo_procedimento'}).text
    # Coleta o nome do procedimento
    nome_procedimento = soup.find('span', {'id': 'nome_procedimento'}).text
    # Coleta os CIDs relacionados
    cids_relacionados = soup.find_all('tr', {'class': 'cid_relacionados'})
    for cid in cids_relacionados:
        codigo_cid = cid.find('td', {'class': 'codigo_cid'}).text
        nome_cid = cid.find('td', {'class': 'nome_cid'}).text
        print(f"{codigo_procedimento}: {nome_procedimento} - CID: {codigo_cid} - {nome_cid}")

# Pega todos os links de procedimentos na página inicial
links_procedimentos = driver.find_elements(By.CSS_SELECTOR, 'table a')

# Itera pelos links de procedimentos e coleta os dados
for link in links_procedimentos:
    href = link.get_attribute('href')
    coletar_dados_procedimento(href)

# Paginação (simulando clique no botão de próxima página)
proxima_pagina = driver.find_element(By.CSS_SELECTOR, 'a[rel="next"]')
proxima_pagina.click()

# Fechar o navegador após a coleta
driver.quit()
