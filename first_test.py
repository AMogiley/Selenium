from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#
driver.get("https://www.google.com/")
#assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenide")
elem.send_keys(Keys.RETURN)
s_find = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/a/div/cite")
print("-----------------------------------")
print(s_find)
print("-----------------------------------")
#if "selenide.org" in s_finde:
#	print("selenide.org на месте : )")
#assert "No results found." not in driver.page_source
#driver.close()


#
