from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
import time
driver.get("http://practice.automationtesting.in/")
#myAccount = driver.find_element_by_css_selector("#menu-item-50>a")
#myAccount.click()
#username = driver.find_element_by_id("username")
#username.send_keys("OleOle_2000@mail.ru")
#password = driver.find_element_by_id("password")
#password.send_keys("Myravek_132")
#login_button = driver.find_element_by_name("login")
#login_button.click()
Shop = driver.find_element_by_css_selector("#menu-item-40>a")
Shop.click()

#тест на проверку текста

#HTML5_Forms = driver.find_element_by_css_selector("li.post-181>a.woocommerce-LoopProduct-link")
#HTML5_Forms.click()

#text_html5_forms  = driver.find_element_by_css_selector("h1.product_title.entry-title")
#get_text_html5_forms = text_html5_forms.text
#assert get_text_html5_forms == "HTML5 Forms"

#тест на количество товаров
#HTML_category = driver.find_element_by_css_selector(".cat-item.cat-item-19>a")
#HTML_category.click()
#kol_elem = driver.find_elements_by_css_selector(".products.masonry-done>li")
#if len(kol_elem) == 3:
#    print("В корзине 3 товара")
#else:
#    print("Ошибка. Количество товаров в корзине: " + str(len(kol_elem)))

#тест на сортировку
#Sort_order = driver.find_element_by_css_selector(".woocommerce-ordering>.orderby")
#Sort_order_value = Sort_order.get_attribute("value")
#if Sort_order_value == "price-desc":
#    print("Default sorting")
#else:
#    print("выбран другой пункт")

#select = Select(Sort_order)
#select.select_by_value("price-desc")
#Sort_order = driver.find_element_by_css_selector(".woocommerce-ordering>.orderby")
#Sort_order_value = Sort_order.get_attribute("value")
#if Sort_order_value == "price-desc":
#    print("От большего к меньшему")
#else:
#    print("выбран другой пункт")

#тест на книгу андроид
#Android_book = driver.find_element_by_css_selector(".post-169>a.woocommerce-LoopProduct-link")
#Android_book.click()
#last_money = driver.find_element_by_css_selector("del>span.woocommerce-Price-amount")
#last_money_text = last_money.text

#assert last_money_text == "₹600.00"
#new_money = driver.find_element_by_css_selector("ins>span.woocommerce-Price-amount")
#new_money_text = new_money.text
#assert new_money_text == "₹450.00"
#images_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                                                        ".woocommerce-main-image.zoom>img")))
#images_btn.click()
#btn_close = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close")))
#btn_close.click()

#тест на кол товаров
#add_to_basket = driver.find_element_by_css_selector(".post-160 .button.product_type_simple")
#add_to_basket.click()
#time.sleep(2)
#item_basket = driver.find_element_by_css_selector(".cartcontents")
#item_basket_text = item_basket.text
#print(item_basket_text)
#assert item_basket_text == "1 Item"
#summ_basket = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
#summ_basket_text = summ_basket.text
#print(summ_basket_text)
#assert summ_basket_text == "₹500.00"
#basket = driver.find_element_by_css_selector(".wpmenucart-contents")
#basket.click()
#wait = WebDriverWait(driver,10)
#subtotal = wait.until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal .woocommerce-Price-amount.amount"),"₹500.00"))
#total = wait.until(
 #   EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total .woocommerce-Price-amount.amount"),"₹525.00"))

#работа в корзине

#driver.execute_script("window.scrollBy(0,300);")
#add_to_basket = driver.find_element_by_css_selector(".post-160 .button.product_type_simple")
#add_to_basket.click()
#time.sleep(2)
#JS_Data_book = driver.find_element_by_css_selector(".post-165 .button.product_type_simple")
#JS_Data_book.click()
#basket = driver.find_element_by_css_selector(".wpmenucart-contents")
#basket.click()
#time.sleep(2)
#remove_book = driver.find_element_by_css_selector(".cart_item:nth-child(1) a.remove")
#remove_book.click()
#undo_remove = driver.find_element_by_css_selector(".woocommerce-message>a")
#undo_remove.click()
#kol_tovar = driver.find_element_by_css_selector(".cart_item:nth-child(1) input.input-text")
#kol_tovar.clear()
#kol_tovar.send_keys("3")
#update_tovar = driver.find_element_by_name("update_cart")
#Quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input.input-text")
#quantity_text = Quantity.get_attribute("value")
#assert quantity_text == "3"
#time.sleep(2)
#apply_coupon = driver.find_element_by_name("apply_coupon")
#apply_coupon.click()
#text_coupon = driver.find_element_by_css_selector(".woocommerce-error")
#get_text_coupon = text_coupon.text
#assert get_text_coupon == "Please enter a coupon code."

#тест на покупку товара
driver.execute_script("window.scrollBy(0,300);")
add_to_basket = driver.find_element_by_css_selector(".post-160 .button.product_type_simple")
add_to_basket.click()
time.sleep(2)
basket = driver.find_element_by_css_selector(".wpmenucart-contents")
basket.click()
procced_to_checkout = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button")))
procced_to_checkout.click()
first_name = WebDriverWait(driver,20).until(
    EC.visibility_of_element_located((By.NAME,"billing_first_name")))

first_name.send_keys("OleOle")
last_name = driver.find_element_by_name("billing_last_name")
last_name.send_keys("AleAleAle")
email = driver.find_element_by_name("billing_email")
email.send_keys("oleole@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89765432112")
select_adres = driver.find_element_by_css_selector(".select2-choice")
select_adres.click()
input_adress = driver.find_element_by_css_selector(".select2-input")
input_adress.send_keys("Romania")
select_adres_cheked = driver.find_element_by_css_selector(".select2-result")
select_adres_cheked.click()
adress = driver.find_element_by_name("billing_address_1")
adress.send_keys("QLDOWMFKG")
city = driver.find_element_by_name("billing_city")
city.send_keys("Radsawqdw")
state = driver.find_element_by_name("billing_state")
state.send_keys("USA")
postcode = driver.find_element_by_name("billing_postcode")
postcode.send_keys("46575345")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)
radiobutton = driver.find_element_by_id("payment_method_cheque")
radiobutton.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
text_pokup = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR,".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
text_payment = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR,".shop_table tr:nth-child(3)>td"),"Check Payments"))
driver.quit()