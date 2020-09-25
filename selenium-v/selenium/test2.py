from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\Yago\\Desktop\\chromedriver.exe')

driver.get('http://www.google.com')
driver.maximize_window()
#Digitar "Selenium" no buscador do google
driver.find_element_by_name('q').send_keys('Selenium webdriver')

sleep(2)
#guardar em uma variável as opções que aparecem
options = driver.find_elements_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]/div[1]')
#verificar a quantidade de opções
len(options)
#iterar as opções e clicar na opção desejada (selenium webdriver)
for option in options:
    option.click()
    break

sleep(2)
#tratamento de exceção
try:
    #confirmar se o valor que aparece na barra de pesquisa é selenium webdriver, caso não seja subir exceção
    assert driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input').get_attribute('value') == 'selenium webdriver'
except:
    raise Exception('Valor não encontrado')

#clicar na opção desejada (site selenium projects)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3').click()

sleep(2)
#printar no terminal o nome do site
print(driver.find_element_by_css_selector('body > section > h1').text)

#confirmar se no título tem selenium, caso não tenha subir exceção
try:
    assert 'Selenium' in driver.title
except:
    raise Exception('Título incorreto')
