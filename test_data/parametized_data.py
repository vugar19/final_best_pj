from test_data import test_data as TD

###################################################################################
# COUPONS
###################################################################################
test_4_4_search_by_keys = "search_value,xpath"
test_4_4_search_by_values = [
                    ("hello",TD.coupon_name),
                    ("אללין אצנף",TD.coupon_name),
                    ("@",TD.coupon_name),
                    ('12345',TD.coupon_code),
                    ('100',TD.min_cart_value),
                    ('2024-12-01',TD.starting_date),
                    ('30',TD.discount_value)]
test_test_4_2_add_invalid_keys = "name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id,validation_message"

test_4_2_add_invalid_values = [
                             (TD.add_form_name,"",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_name),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_code),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_min_cart_val),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_start_date),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'',TD.add_form_discount_ammount,'30',TD.add_form_types_precen,TD.add_form_end_date),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'',TD.add_form_types_precen,TD.add_form_discount_ammount),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30','',TD.add_form_types_precen)]

test_4_2_add_valid_keys = "name_id,name_value,code_id,code_value,min_cart_id,min_cart_value,start_date_id ,start_date_value, end_date_id,end_date_value, discount_amount_id,discount_amount_value,discount_type_id"

test_4_2_add_valid_values = [
                             (TD.add_form_name,"hello_workd",TD.add_form_code,'123453',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/2024',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel)]


edit_test_4_5_keys = "edit_id, edit_value"

edit_test_4_5_values = [
    (TD.coupon_name, 'not hello'),
    (TD.coupon_code, '156456'),
    (TD.min_cart_value, '200'),
    (TD.discount_value, '666')]


###################################################################################
#ETRADE
###################################################################################
test_11_3_search_by_keys = "search_value,xpath"
test_11_3_search_etrade_by_values = [
                    ("300",TD.etrade_ammount),
                    ('123456',TD.account_number),
                    ('1111-11-11',TD.payment_date),
                    ('6',TD.payment_duration)]

edit_test_etrade_11_5_keys = "edit_id, edit_value"

edit_test_etrade_11_5_values = [
    (TD.payment_date, '1111-11-11'),
    (TD.account_number, '156456'),
    (TD.bank_code, '200'),
    (TD.payment_duration, '666')]

###################################################################################
# CATEGORY
###################################################################################
test_14_3_search_category_keys = "search_value,xpath"

test_14_3_search_category_values = [
                    ("300",TD.etrade_ammount),
                    ('123456',TD.account_number),
                    ('1111-11-11',TD.payment_date),
                    ('6',TD.payment_duration)]