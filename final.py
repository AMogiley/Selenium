#!/usr/bin/python3
		
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
		
		
class Search(unittest.TestCase):
	
	def setUp(self):			
		self.driver = webdriver.Chrome()
		
	def test(self):
		self.driver.get("https://www.google.com/")	# открыть google и проверить валидность 
		assert 'Google' in self.driver.title		
		elem = self.driver.find_element_by_name("q")	# найти строку поиска для ввода
		elem.send_keys("selenide")
		elem.send_keys(Keys.RETURN)	# послать клавиши на ввод в строку elem
		s_find = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a/div/cite')	# найти и определить первый результат через assert
		assert 'ru.selenide.org/' in s_find.text 
		
		self.driver.find_element_by_xpath('//*[@id="ow15"]/a').click()
		self.driver.find_element_by_xpath('//*[@id="lb"]/div/a[1]').click()	# зайти во вкладку картинки через кнопку ещё (почему то версия страницы google переодически менялась, но потом стал выходить только один тип страницы где вкладка "картинки" открывается через кнопку Ещё)

		s_img = self.driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a[2]/div[2]')
		print(s_img.text)
		assert 'selenide.org' in s_img.text # определить отношение первой картинки к сайту selenide

		self.driver.back()	# перейти на предыдущую страницу
		s_find = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a/div/cite')
		assert 'ru.selenide.org/' in s_find.text	# проверить не изменился ли результат
		
	def tearDown(self):
		self.driver.close()	# закрыть браузер

if __name__ == '__main__': unittest.main();
