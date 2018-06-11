# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
driver.quit()

