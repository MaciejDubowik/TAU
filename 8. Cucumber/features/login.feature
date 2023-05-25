Feature: Test Login
  As a user
  I want to be able to log into my account
  So I can access my personal details and make purchases

  Background:
    Given the user is on the Saucedemo homepage

  Scenario: Check if page loads correctly
    Then the user should be on the "https://www.saucedemo.com/" page

  Scenario: Successful Login
    When the user enters "standard_user" as username
    And the user enters "secret_sauce" as password
    And the user clicks the submit button
    Then the user should be on the "https://www.saucedemo.com/inventory.html" page
    And the user should see a list of products

  Scenario: Check First Product Details
    Given the user is logged in as "standard_user" with password "secret_sauce"
    Then the user should see "Sauce Labs Backpack" as the first product
    And the user clicks on the first product
    Then the user should be on the "https://www.saucedemo.com/inventory-item.html?id=4" page
    And the user should see the description "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    But the description should not contain "waterproof"

  Scenario: Add First Product to Cart
    Given the user is logged in as "standard_user" with password "secret_sauce"
    And the user is on the first product's details page
    When the user clicks on the add to cart button
    Then the user should see "1" in the cart quantity
