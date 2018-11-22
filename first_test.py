from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
elem = driver.find_element_by_name("q")
elem.send_keys("selenide")
elem.send_keys(Keys.RETURN)
s_find = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a/div/cite')
if 'ru.selenide.org/' in s_find.text:
	print("OK!!")
	
mor = driver.find_element_by_xpath('//*[@id="ow15"]/a')
mor.send_keys(Keys.RETURN)
s_img = driver.find_element_by_xpath('//*[@id="lb"]/div/a[1]')
s_img.send_keys(Keys.RETURN)
