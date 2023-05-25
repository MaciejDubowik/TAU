from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('the user is on the Saucedemo homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('the user enters "{username}" as username')
def step_impl(context, username):
    username_field = context.driver.find_element(By.NAME, "user-name")
    username_field.clear()
    username_field.send_keys(username)

@when('the user enters "{password}" as password')
def step_impl(context, password):
    password_field = context.driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(password)

@when('the user clicks the submit button')
def step_impl(context):
    submit_button = context.driver.find_element(By.NAME, "login-button")
    submit_button.click()

@then('the user should be on the "{url}" page')
def step_impl(context, url):
    assert context.driver.current_url == url

@then('the user should see a list of products')
def step_impl(context):
    product_list = context.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(product_list) > 0

@then('the user should see "{product_name}" as the first product')
def step_impl(context, product_name):
    product_list = context.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    first_product = product_list[0]
    assert first_product.text == product_name

@then('the user should see the description "{description}"')
def step_impl(context, description):
    description_field = context.driver.find_element(By.CLASS_NAME, "inventory_details_desc")
    assert description_field.text == description

@then('the description should not contain "{text}"')
def step_impl(context, text):
    description_field = context.driver.find_element(By.CLASS_NAME, "inventory_details_desc")
    assert text not in description_field.text

@when('the user clicks on the add to cart button')
def step_impl(context):
    add_to_cart_button = context.driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

@then('the user should see "{quantity}" in the cart quantity')
def step_impl(context, quantity):
    cart_quantity = context.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_quantity.text == quantity

@then('the user clicks on the first product')
def step_impl(context):
    product_list = context.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    first_product = product_list[0]
    first_product.click()

@given('the user is logged in as "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.execute_steps(f"""
        When the user enters "{username}" as username
        And the user enters "{password}" as password
        And the user clicks the submit button
    """)

@when('the user is on the first product\'s details page')
def step_impl(context):
    context.execute_steps(f"""
        Then the user clicks on the first product
    """)