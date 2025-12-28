from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.correios.com.br")

driver.find_element(By.PARTIAL_LINK_TEXT, "Busca CEP ou Endereço").click()
driver.switch_to.window(driver.window_handles[1])

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "endereco"))
)

input_element= driver.find_element(By.ID, "endereco")
input_element.send_keys("80700000")
print("Por favor digite o Captcha")

time.sleep(15)

input_element.send_keys(Keys.ENTER)

time.sleep(1)

if len(driver.find_elements(By.CSS_SELECTOR, "div#alerta.aberto div.msg")) > 0:
    print("Por favor digite o Captcha corretamente para continuar o teste")
    time.sleep(15)
    input_element.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Não há dados a serem exibidos']"))
)

print('O CEP não existe na base de dados dos correios.')

driver.find_element(By.ID, "btn_nbusca").click()

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.ID, "endereco"))
)

input_element= driver.find_element(By.ID, "endereco")
input_element.send_keys("01013-001")
print("Por favor digite o Captcha")

time.sleep(15)

input_element.send_keys(Keys.ENTER)

time.sleep(1)

if len(driver.find_elements(By.CSS_SELECTOR, "div#alerta.aberto div.msg")) > 0:
    print("Por favor digite o Captcha corretamente para continuar o teste")
    time.sleep(15)
    input_element.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Rua Quinze de Novembro')]"))
)
driver.find_element(By.XPATH, "//*[contains(text(), 'São Paulo/SP')]")
print('O CEP pertence à rua 15 de novembro, São Paulo/SP')

driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.CSS_SELECTOR, ".ic-busca-out").click()

driver.switch_to.window(driver.window_handles[1])

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='objeto']"))
)

input_element = driver.find_element(By.XPATH, "//input[@id='objeto']")
input_element.send_keys("SS987654321BR")
print("Por favor digite o Captcha")

time.sleep(15)

input_element.send_keys(Keys.ENTER)

if len(driver.find_element(By.CSS_SELECTOR, "div.campos.captcha div.campo div.mensagem").text) > 0:
    print("Por favor digite o Captcha corretamente para continuar o teste")
    time.sleep(15)
    input_element.send_keys(Keys.ENTER)


WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Objeto não encontrado na base de dados dos Correios.']"))
)
print('O codigo não está correto. Não há nenhum objeto na base de dados dos correios com esse código.')


driver.quit()