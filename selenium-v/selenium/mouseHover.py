from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.carrefour.com.br/')
#guarda em uma variável os métodos de action chains
action = ActionChains(driver)
#guarda em uma variável o elemento para ficar mais fácil a interação com as ações
mercado = driver.find_element_by_link_text('Mercado')
#utiliza actions para realizar a ação de "hover" ao passar o mouse por cima do elemento
action.move_to_element(mercado).perform()
#guarda em uma variável outro elemento
subMenu = driver.find_element_by_link_text('Alimentos básicos')
#realiza a mesma ação de hover agora em outro menu
action.move_to_element(subMenu).perform()
#guarda em uma variável otro elemento
option = driver.find_element_by_link_text('Arroz e grãos')
#realiza a ação de clicar no elemento utilizando actions
action.move_to_element(option).click().perform()