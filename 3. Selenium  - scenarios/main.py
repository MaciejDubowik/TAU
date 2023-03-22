import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.username_field = self.driver.find_element(By.NAME, "user-name")
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.submit_button = self.driver.find_element(By.NAME, "login-button")
        self.username_field.clear()
        self.password_field.clear()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_scenario_1(self):
        self.driver.get("https://www.saucedemo.com/")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")

    def test_scenario_2(self):
        self.driver.get("https://www.saucedemo.com/")
        self.username_field = self.driver.find_element(By.NAME, "user-name")
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.submit_button = self.driver.find_element(By.NAME, "login-button")
        self.username_field.clear()
        self.password_field.clear()

        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("secret_sauce")
        self.submit_button.click()

        self.assertNotEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

        product_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assertTrue(len(product_list) > 0)

    def test_scenario_3(self):
        self.driver.get("https://www.saucedemo.com/")
        self.username_field = self.driver.find_element(By.NAME, "user-name")
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.submit_button = self.driver.find_element(By.NAME, "login-button")
        self.username_field.clear()
        self.password_field.clear()

        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("secret_sauce")
        self.submit_button.click()

        self.assertNotEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

        product_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assertTrue(len(product_list) > 0)

        first_product = product_list[0]
        self.assertEqual(first_product.text, "Sauce Labs Backpack")
        first_product.click()

        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory-item.html?id=4")
        description = self.driver.find_element(By.CLASS_NAME, "inventory_details_desc")
        self.assertEqual(description.text, "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
        self.assertTrue("sleek, streamlined" in description.text)
        self.assertFalse("waterproof" in description.text)

        add_to_cart_button = self.driver.find_element(By.CLASS_NAME, "btn_inventory")
        self.assertTrue(add_to_cart_button.is_enabled())
        add_to_cart_button.click()

        cart_quantity = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_quantity.text, "1")
