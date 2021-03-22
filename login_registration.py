from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
myAccount = driver.find_element_by_css_selector("#menu-item-50>a")
myAccount.click()
#регистрация
#reg_email = driver.find_element_by_id("reg_email")
#reg_email.send_keys("OleOle_2000@mail.ru")
#reg_password = driver.find_element_by_id("reg_password")
#reg_password.send_keys("Myravek_132")
#reg_button = driver.find_element_by_name("register")
#reg_button.click()

#авторизация
username = driver.find_element_by_id("username")
username.send_keys("OleOle_2000@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Myravek_132")
login_button = driver.find_element_by_name("login")
login_button.click()
Logout = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                "li.woocommerce-MyAccount-navigation-link--customer-logout>a")))


driver.quit()