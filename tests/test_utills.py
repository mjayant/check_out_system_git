"""
Unit tests for job api
"""

from unittest import TestCase, mock
import unittest
import requests
from src.main import create_app
from tests import constant
from src  import utills


class TestJobs(TestCase):
    """
    This test cases for check functionality of utility module .
    Here already we have customized input and respective output
    """

    def setUp(self):
        """Setting up pre-requisite"""
        self.app = create_app()
        self.client = self.app.test_client

    def test_job_api_add_product_in_cart_first(self):
        """
        This test case for check first given test case i.e
        Basket: CH1, AP1, AP1, AP1, MK1
        Total price expected: 16.61
        :return:
        """
        final_dict = {}
        total_item_dict = {}
        quant_cd_map = constant.DATA_FOR_FIRST_TEST_CASE
        disc_price , final_dict = utills.apply_code(quant_cd_map)
        total_price, total_item_dict = utills.calculate_price(quant_cd_map)
        final_price = disc_price + total_price
        final_price = float("{:.2f}".format(final_price))
        self.assertEqual(final_price, constant.EXPECTING_OP_FIRST_TEST_CASE)

    def test_job_api_add_product_in_cart_second(self):
        """
        This test case for check second given test case i.e
        Basket: CH1, AP1, CF1, MK1
        Total price expected: 20.34
        :return:
        """

        quant_cd_map = constant.DATA_FOR_SECOND_TEST_CASE
        disc_price, final_dict = utills.apply_code(quant_cd_map)
        total_price, total_item_dict = utills.calculate_price(quant_cd_map)
        final_price = disc_price + total_price
        final_price = float("{:.2f}".format(final_price))
        self.assertEqual(final_price, constant.EXPECTING_OP_SECOND_TEST_CASE)

    def test_job_api_add_product_in_cart_third(self):
        """
        This test case for check third given test case i.e
        Basket: MK1, AP1
        Total price expected: $10.75
        :return:
        """

        quant_cd_map = constant.DATA_FOR_THIRD_TEST_CASE
        disc_price, final_dict = utills.apply_code(quant_cd_map)
        total_price, total_item_dict = utills.calculate_price(quant_cd_map)
        final_price = disc_price + total_price
        final_price = float("{:.2f}".format(final_price))
        self.assertEqual(final_price, constant.EXPECTING_OP_THIRD_TEST_CASE)

    def test_job_api_add_product_in_cart_fourth(self):
        """
        This test case for check fourth given test case i.e
        Basket: CF1, CF1
        Total price expected: $11.23
        :return:
        """
        quant_cd_map = constant.DATA_FOR_FOURTH_TEST_CASE
        disc_price, final_dict = utills.apply_code(quant_cd_map)
        total_price, total_item_dict = utills.calculate_price(quant_cd_map)
        final_price = disc_price + total_price
        final_price = float("{:.2f}".format(final_price))
        self.assertEqual(final_price, constant.EXPECTING_OP_FOURTH_TEST_CASE)

    def test_job_api_add_product_in_cart_fifth(self):
        """
        Basket: AP1, AP1, CH1, AP1
        Total price expected: $16.61
        :return:
        """
        quant_cd_map = constant.DATA_FOR_FIFTH_TEST_CASE
        disc_price, final_dict = utills.apply_code(quant_cd_map)
        total_price, total_item_dict = utills.calculate_price(quant_cd_map)
        final_price = disc_price + total_price
        final_price = float("{:.2f}".format(final_price))
        self.assertEqual(final_price, constant.EXPECTING_OP_FIFTH_TEST_CASE)

    def test_apply_code(self):
        """
        Here we are passing customized input and expecting pre defined value
        :return:
        """
        retrun_val, final_dict = utills.apply_code(constant.DATA_FOR_FIRST_TEST_CASE)
        val = -9.25
        self.assertEqual(retrun_val, val)


if __name__ == '__main__':
    unittest.main()
