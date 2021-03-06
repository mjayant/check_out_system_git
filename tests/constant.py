#!/usr/bin/python
# -*- coding: utf-8 -*-
PROMO_FUNCT_MAP = {'BOGO': 'check_bogo_cd', 'APPL':'check_appl_cd', 'CHMK': 'check_cmnk_cd', 'APOM': 'check_apom_cd'}
PRICE_PRODUCT_MAP = {'CH1':3.11 , 'AP1': 6.00 , 'CF1': 11.23, 'MK1':4.75, 'OM1':3.69}

DATA_FOR_FIRST_TEST_CASE = {'CH1':['CH1', '3.11', 1], 'MK1':['MK1', '4.75', 1], 'AP1':['AP1','6.00', 3]} #CH1, AP1, AP1, AP1, MK1
EXPECTING_OP_FIRST_TEST_CASE = 16.61

DATA_FOR_SECOND_TEST_CASE = {'CH1':['CH1', '3.11', 1], 'MK1':['MK1', '4.75', 1], 'AP1':['AP1','6.00', 1], 'CF1':['CF1','11.23', 1]} #CH1, AP1, CF1, MK1
EXPECTING_OP_SECOND_TEST_CASE = 20.34

DATA_FOR_THIRD_TEST_CASE = {'MK1':['MK1', '4.75', 1], 'AP1':['AP1','6.00', 1]} #MK1, AP1
EXPECTING_OP_THIRD_TEST_CASE = 10.75

DATA_FOR_FOURTH_TEST_CASE = {'CF1':['CF1', '11.23', 2]} #CF1, CF1
EXPECTING_OP_FOURTH_TEST_CASE = 11.23

DATA_FOR_FIFTH_TEST_CASE = {'CH1':['CH1', '3.11', 1], 'AP1':['AP1','6.00', 3]} #AP1, AP1, CH1, AP1
EXPECTING_OP_FIFTH_TEST_CASE = 16.61



