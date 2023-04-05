import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.NAME, "user-name")
        self.password_field = (By.NAME, "password")
        self.submit_button = (By.NAME, "login-button")

    def login(self, username, password):
        self.find_element(self.username_field).clear()
        self.find_element(self.password_field).clear()
        self.find_element(self.username_field).send_keys(username)
        self.find_element(self.password_field).send_keys(password)
        self.find_element(self.submit_button).click()


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_list = (By.CLASS_NAME, "inventory_item_name")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_quantity = (By.CLASS_NAME, "shopping_cart_badge")

    def add_to_cart(self, index=0):
        products = self.find_elements(self.product_list)
        products[index].click()
        self.find_element(self.add_to_cart_button).click()

    def get_cart_quantity(self):
        return self.find_element(self.cart_quantity).text

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = None

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_scenario_1(self):
        for browser in ["Chrome", "Firefox", "Safari"]:
            with self.subTest(browser=browser):
                if browser == "Chrome":
                    self.driver = webdriver.Chrome()
                elif browser == "Firefox":
                    self.driver = webdriver.Firefox()
                elif browser == "Safari":
                    self.driver = webdriver.Safari()
                else:
                    self.fail(f"{browser} is not a valid browser name.")

                self.driver.get("https://www.saucedemo.com/")
                self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
                self.driver.quit()

    def test_scenario_2(self):
        for browser in ["Chrome", "Firefox", "Safari"]:
            with self.subTest(browser=browser):
                self.driver = self.create_driver(browser)
                login_page = LoginPage(self.driver)
                inventory_page = InventoryPage(self.driver)

                self.driver.get("https://www.saucedemo.com/")
                self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")

                login_page.login("standard_user", "secret_sauce")

                self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")
                self.assertTrue(inventory_page.find_element(inventory_page.product_list).is_displayed())

    def test_scenario_3(self):
        for browser in ["Chrome", "Firefox", "Safari"]:
            with self.subTest(browser=browser):
                self.driver = self.create_driver(browser)
                login_page = LoginPage(self.driver)
                inventory_page = InventoryPage(self.driver)

                self.driver.get("https://www.saucedemo.com/")
                self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")

                login_page.login("standard_user", "secret_sauce")

                self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")
                self.assertTrue(inventory_page.find_element(inventory_page.product_list).is_displayed())

                inventory_page.add_to_cart(index=0)

                self.assertEqual(inventory_page.get_cart_quantity(), "1")
                self.assertTrue("Sauce Labs Backpack" in self.driver.page_source)

                self.driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()
                description = self.driver.find_element(By.CLASS_NAME, "inventory_details_desc")
                self.assertTrue("sleek, streamlined" in description.text)
                self.assertFalse("waterproof" in description.text)

                self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

                self.assertEqual(inventory_page.get_cart_quantity(), "2")

    def create_driver(self, browser):
        if browser == "Chrome":
            return webdriver.Chrome()
        elif browser == "Firefox":
            return webdriver.Firefox()
        elif browser == "Safari":
            return webdriver.Safari()
        else:
            self.fail(f"{browser} is not a valid browser name.")