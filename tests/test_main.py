"""
Unit tests for job api
"""

from unittest import TestCase, mock
import unittest
import requests
from http import HTTPStatus
from main import create_app
from tests import constant
from src import utills


class TestJobs(TestCase):
    """
    Unit tests for checkout system APi
    """

    def setUp(self):
        """Setting up pre-requisite"""
        self.app = create_app()
        self.client = self.app.test_client

    def test_get_bill_submit_bill(self):
        """
        It call get_bill api and api return template so test case check that particular field
        is exist or not , if exist then test case pass
        :return:
        """
        data = b'{"prd_quantity___MK1___4.75":"1","prd_quantity___OM1___3.69":"4"}'
        response = requests.post("http://127.0.0.1:5000/get_bill", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Total Bill without discount', response.text)

    def test_neg_get_bill_submit_bill(self):
        """
        This is negative test case for get_bill API
        Here we have corrupted input so AIP return template with 0.0 total bill
        It call get_bill api and api return template so test case check that particular field
        is exist or not , if exist then test case pass
        :return:
        """
        data = b'{"prd_quantity___MK4.75":"1","prd_quantity__3.69":"4sdjvksdj"}' # We have corrupted data
        response = requests.post("http://127.0.0.1:5000/get_bill", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Total Bill  0.0', response.text)

    def test_add_product_in_cart_post(self):
        """
        It call add_product_in_cart api and api return template so test case check that particular field
        is exist or not , if exist then test case pass
        :return:
        """

        data = dict([('prd_quantity___test3___20', ''), ('prd_quantity___CH1___3.11', ''),
                     ('prd_quantity___AP1___6', ''), ('prd_quantity___CF1___11.23', ''),
                     ('prd_quantity___MK1___4.75', '3'), ('prd_quantity___OM1___3.69', '4'),
                     ('prd_quantity___sdv___23', ''), ('prd_quantity___dd___23', '')])

        response = requests.post("http://127.0.0.1:5000/add_product_in_cart", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Total Bill without discount', response.text)

    def test_neg_add_product_in_cart_post(self):
        """
        This is negative test case for add_product_in_cart API
        Here we have corrupted input so AIP return template with 0.0 total bill
        It call get_bill api and api return template so test case check that particular field
        is exist or not , if exist then test case pass
        :return:
        """

        data = dict([('prd_quantity___', ''), ('prd_quantity___CH1___3.11', ''), # we have corrupted data
                     ('prd_quantity___AP1___6', ''), ('prd_quantity___CF1___11.23', ''),
                     ('prd_quantity___MK1___4.75', '3'), ('prd_quantity___OM1___3.69', '4'),
                     ('prd_quantity___sdv___23', ''), ('prd_quantity___dd___23', '')])

        response = requests.post("http://127.0.0.1:5000/add_product_in_cart", data=data)
        self.assertEqual(response.status_code, 500)
        self.assertNotIn('Total Bill without discount', response.text)

    def test_add_product(self):
        """
        It call add_product api and api return template so test case check that particular field
        is exist or not , if exist then test case pass
        :return:
        """

        data = dict([('prd_name', 'vv'), ('prd_code', 'vv'), ('prd_price', '12')])

        response = requests.post("http://127.0.0.1:5000/add_product", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '<Product vv> successfully created!')


    def test_delete_product(self):
        """
        It call delete api and api return template so test case check that particular field
        is exist or not , if exist then test case pass
        :return:
        """
        #prd_cd = 'v1'
        response = requests.post("http://127.0.0.1:5000/delete/vv")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '<Product vv> successfully deleted!')

    def test_neg_delete_product(self):
        """
        It call delete api with key which is not exist in db , so delete action should be fail
        :return:
        """
        #prd_cd = 'v1'
        response = requests.post("http://127.0.0.1:5000/delete/v1")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.text, 'Error deleting #v1')


if __name__ == '__main__':
    unittest.main()
