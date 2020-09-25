from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/windows')
#elemento encontrado pelo texto do link
driver.find_element_by_link_text('Click Here').click()
#variável com a aba que será utilizada para o teste (parent - [0] / child - [1])
child = driver.window_handles[1]
#troca para a aba desejada (child)
driver.switch_to.window(child)
#printa o texto da aba selecionada
print(driver.find_element_by_tag_name('h3').text)
#fecha a aba atual
driver.close()
#troca para a aba anterior (parent)
driver.switch_to.window(driver.window_handles[0])
#confirma o texto apresentado na aba
assert 'Opening a new window' == driver.find_element_by_tag_name('h3').text

