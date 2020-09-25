from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#criação de lista para armazenar os produtos selecionados
list1 = []
#criação de lista para confirmar se os produtos selecionados são os mesmos da primeira lista
list2 = []

#localizar a barra de pesquisa e digitar "ber"
driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/form/input').send_keys('ber')
#aguardar 3 segundos
sleep(3)
#contar a quantidade de produtos
count = len(driver.find_elements_by_xpath('//*[@class="products"]/div'))
#confirmar se aparecem 3 produtos
assert count == 3
#guardar o botão de adicionar ao carrinho a uma variável
buttons = driver.find_elements_by_xpath('//*[@class="product-action"]/button')
#fazer iteração para selecionar os 3 botões
for button in buttons:
    #adicionar a uma lista os produtos selecionados
    list1.append(button.find_element_by_xpath('parent::div/parent::div/h4').text)
    #clicar nos 3 botões
    button.click()
#printar os produtos da lista 
print(list1)
#clicar no botão de carrinho
driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[3]/a[4]').click()
#clicar para fazer o checkout
driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
#adicionar espera explícita (aguarda o carregamendo de um determinado elemento do DOM)
wait = WebDriverWait(driver, 5)
#espera até que o elemento seja localizado pelo nome da classe
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
#adicionar a uma variável os produtos que foram selecionados
veggies = driver.find_elements_by_css_selector('p.product-name')
#iteração para adicionar a uma lista a confirmação dos produtos selecionados
for veg in veggies:
    list2.append(veg.text)
#printar os produtos da segunda lista
print(list2)
#confirmar se a lista 1 é igual a lista 2
assert list1 == list2
#adicionar a uma variável o valor total original dos produtos
originalAmount = driver.find_element_by_css_selector('span.discountAmt').text
#digita o código promocional
driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
#clica para aplicar o código promocional
driver.find_element_by_css_selector('#root > div > div > div > div > div > button').click()
#adicionar espera explícita (aguarda o carregamendo de um determinado elemento do DOM)
wait = WebDriverWait(driver, 7)
#espera até que o elemento seja localizado pelo css selector
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'span.promoInfo')))
#printar o valor
print(driver.find_element_by_css_selector('span.promoInfo').text)
#adicionar a uma variável o total dos produtos com desconto
discountAmount = driver.find_element_by_css_selector('span.discountAmt').text
#confirmar se o valor com desconto é inferior ao valor original
assert float(discountAmount) < float(originalAmount)
#adicionar a uma variável o total dos produtos
amounts = driver.find_elements_by_xpath('//tr/td[5]/p')
#variável para auxiliar na soma
sum = 0
#iteração para somar todos os produtos
for amount in amounts:
    sum += float(amount.text)
print(sum)
#variável para guardar o total somado dos produtos
totalAmount = driver.find_element_by_css_selector('span.totAmt')
#confirma se a soma dos produtos é igual ao total dos produtos somados
assert sum == float(totalAmount.text)