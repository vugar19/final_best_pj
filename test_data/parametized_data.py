test_4_4_search_by = [
                    ("jopo",'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[1]/span/div/input','defaultValue'),
    ("אללין",'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[1]/span/div/input','defaultValue'),
                    ("@",'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[1]/span/div/input','defaultValue'),
                    (36,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input','defaultValue'),
                    (12,'//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[3]/span/div/input','defaultValue'),
                    ('2024-12-01','//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[5]/div[1]/div[1]/span/div/input','defaultValue'),
                    (3,'//tr/td[1]','defaultValue')
]

test_4_2_add_invalid = [
                             (TD.add_form_name,"",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_name),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_code),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_min_cart_val),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel,TD.add_form_start_date),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'',TD.add_form_discount_ammount,'30',TD.add_form_types_precen,TD.add_form_end_date),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'',TD.add_form_types_precen,TD.add_form_discount_ammount),
                             (TD.add_form_name,"hello_world",TD.add_form_code,'12345',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/24',TD.add_form_discount_ammount,'30','',TD.add_form_types_precen),
                                     ]



test_4_2_add_valid = [
                             (TD.add_form_name,"hello_workd",TD.add_form_code,'123453',TD.add_form_min_cart_val,'100',TD.add_form_start_date,'15/01/2024',TD.add_form_end_date,'26/08/2024',TD.add_form_discount_ammount,'30',TD.add_form_types_shekel)]