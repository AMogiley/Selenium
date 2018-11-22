#!/usr/bin/python3
		
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
		
		
class Search(unittest.TestCase):
	
	def setUp(self):			
		self.driver = webdriver.Chrome()


	def test(self):
		self.driver.get("https://www.google.com/")
		assert 'Google' in self.driver.title		
		elem = self.driver.find_element_by_name("q")
		elem.send_keys("selenide")
		elem.send_keys(Keys.RETURN)
		s_find = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a/div/cite')
#		assert s_finde.text == 'ru.selenide.org'
		if 'ru.selenide.org/' in s_find.text:
			print("OK!!")
			
		self.driver.find_element_by_xpath('//*[@id="ow15"]/a').click()
		self.driver.find_element_by_xpath('//*[@id="lb"]/div/a[1]').click()
		
		s_img = driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a[2]/div[1]')
		#print(s_img)
		#print(s_img.text)
		assert s_finde.text == 'ru.selenide.org/'		
#		if 'Selenide' or 'selenide' in s_img.text:
#		    print('OK')
		
		self.driver.back()
		s_find = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a/div/cite')
		assert s_finde.text == 'ru.selenide.org/'
#		if 'ru.selenide.org/' in s_find.text:
#			print("OK!!")
		
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__': unittest.main();
		
