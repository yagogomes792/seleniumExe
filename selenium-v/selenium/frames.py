from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/iframe')
#muda para fazer interação com frames
driver.switch_to_frame('mce_0_ifr')
#limpa o que está escrito no frame
driver.find_element_by_id('tinymce').clear()
#Digita no frame
driver.find_element_by_id('tinymce').send_keys('Funcionou!!!')
#muda novamente para o conteúdo anterior (HTML)
driver.switch_to_default_content()
#printa o texto do HTML
print(driver.find_element_by_tag_name('h3').text)