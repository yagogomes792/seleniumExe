from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\Yago\\Desktop\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.espn.com.br/')


driver.find_element_by_css_selector('#leagues > li:nth-child(1) > div > div.scoreLabel.soccer.js-show > div').click()
sleep(5)

driver.find_element_by_css_selector('#fullbtn > a').click()
sleep(5)

driver.find_element_by_xpath('//*[@id="scoreboard-page"]/div[1]/div[2]/div/div/div[17]/a').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="569908"]/div/div/div[2]/header/div/div[3]/div/div[2]/div[2]/div/a/span[2]').click()
