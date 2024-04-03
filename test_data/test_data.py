from selenium.webdriver.common.by import By
login = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/div[1]/div/div[1]/div/input")
login_btn = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/input")
code = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/div[1]/div[1]/span/div/input")
code_btn = (By.XPATH,"//*[@id='root']/div[1]/div[2]/div/span/form/input")
phone = "9721320207423"
coupons = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[4]')
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
export_btn = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[2]')
search_bar = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/span/span/div/input')
elements = By.CSS_SELECTOR,'#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > div.table_tableScroll > div.table_table > table > tbody > tr:nth-child'
count_findings = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]')
coupon_name =(By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[1]/span/div/input')
coupon_code = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input')
min_cart_value = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[3]/span/div/input')
starting_date = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div[1]/span/div/input')
ending_date = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div[2]/span/div/input')
discount_value = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[6]/div[1]/div[1]/span/div/input')
edit_submit_btn = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/form/input')
edit_success_message = (By.XPATH,'//*[@id="8tnth7yg7j"]/div[1]')
##################################################################################
etrade = (By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[17]')
etrade_ammount = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div/span/div/input')

next_btn = (By.XPATH,'//input[@value="Next"]')
submit_etrade_update_btn = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/input')
etrade_id = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[1]/span/div/input')
payment_duration = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[1]/span/div/input')
account_number = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[3]/span/div/input')
bank_name = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[4]/div[1]/span[1]/div/input')
bank_code = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[5]/span/div/input')
branch = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[6]/span/div/input')
remarks = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[7]/span/div/input')
branch = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[7]/span/div/input')
payment_date = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[3]/div[8]/span/div/input')
next_first_btn_etrade = (By.XPATH,'//*[@id="root"]/div[1]/div[4]/div/div/div/form/div[5]/input')
















