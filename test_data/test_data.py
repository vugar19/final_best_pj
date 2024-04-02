from selenium.webdriver.common.by import By
login = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/div[1]/div/div[1]/div/input")
login_btn = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/input")
code = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/div[1]/div[1]/span/div/input")
code_btn = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/input")
phone = "9721320207423"

xpath = (By.XPATH,"//*[@id='root']")
logout = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/nav/div[1]/div/span[2]/a')
coupon_btn = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[4]')
drop_down_manu = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div')
add_btn = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[1]')
add_form_name = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[1]/span/div/input')
add_form_code = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input')
add_form_min_cart_val = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[3]/span/div/input')
add_form_start_date = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div[1]/span/div/input')
add_form_end_date = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div[2]/span/div/input')
add_form_discount_ammount = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[6]/div[1]/div[1]/span/div/input')
add_form_type = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[6]/div[1]/div[2]/div[1]/span[1]/div/input')
add_form_types_shekel = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[6]/div[1]/div[2]/div[1]/span[1]/div[2]/div/div[1]')
add_form_types_precen = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[6]/div[1]/div[2]/div[1]/span[1]/div[2]/div/div[2]')

final_add_btn = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/input')

error_message = (By.XPATH,'//*[@class="form_note"]')
sucsess_mess = (By.XPATH,'//div[@alert=role]')