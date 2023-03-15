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

    def tearDown(self):
        self.driver.quit()

    def test_empty_username(self):

        self.password_field.send_keys("anypassword")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(password_error_msg.text, "Epic sadface: Username is required")

    def test_invalid_user(self):

        self.username_field.send_keys("invaliduser")
        self.password_field.send_keys("wrongpassword")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(password_error_msg.text, "Epic sadface: Username and password do not match any user in this service")

    def test_invalid_password(self):

        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("wrongpassword")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(password_error_msg.text, "Epic sadface: Username and password do not match any user in this service")

    def test_empty_password(self):

        self.username_field.send_keys("exampleuser")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertIn("Epic sadface: Password is required", self.driver.page_source)

    def test_whitespace_username(self):

        self.username_field.send_keys("  standard_user  ")
        self.password_field.send_keys("secret_sauce")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(password_error_msg.text, "Epic sadface: Username and password do not match any user in this service")

    def test_whitespace_password(self):

        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("  secret_sauce ")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(password_error_msg.text, "Epic sadface: Username and password do not match any user in this service")

    def test_whitespace_username(self):

        self.username_field.send_keys(" stan\u200bdard_user  ")
        self.password_field.send_keys("secret_sauce")
        self.submit_button.click()

        password_error_msg = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(password_error_msg.text, "Epic sadface: Username and password do not match any user in this service")


    def test_successful_login(self):
        self.username_field.send_keys("standard_user")
        self.password_field.send_keys("secret_sauce")
        self.submit_button.click()
        self.assertNotEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_invalid_credentials(self):
        self.username_field.send_keys("invalidusername")
        self.password_field.send_keys("invalidpassword")
        self.submit_button.click()

        error_msg = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/")
        self.assertEqual(error_msg.text, "Epic sadface: Username and password do not match any user in this service")
