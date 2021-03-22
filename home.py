from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
book_ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 h3")
book_ruby.click()
rewiews = driver.find_element_by_css_selector("li.reviews_tab>a")
rewiews.click()
stars = driver.find_element_by_css_selector("a.star-5")
stars.click()
comments = driver.find_element_by_id("comment")
comments.send_keys("Nice book!")
author = driver.find_element_by_id("author")
author.send_keys("OleOle")
email = driver.find_element_by_id("email")
email.send_keys("OleOle_2000@mail.ru")
submit = driver.find_element_by_id("submit")
submit.click()
driver.quit()