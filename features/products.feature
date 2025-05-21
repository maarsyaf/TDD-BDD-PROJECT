Feature: Manage Products

  Scenario: List all products
    Given the following products
      | name       | category   | available | price |
      | Soap       | Hygiene    | true      | 1.50  |
      | Laptop     | Electronics| true      | 999.99|
    When I visit the "Home Page"
    Then I should see "Soap"
    And I should see "Laptop"

  Scenario: Search product by name
    Given the following products
      | name   | category | available | price |
      | Chair  | Furniture| true      | 49.99 |
    When I search for products with name "Chair"
    Then I should see "Chair"

  Scenario: Search product by category
    Given the following products
      | name     | category   | available | price |
      | Camera   | Electronics| true      | 150.00|
    When I search for products with category "Electronics"
    Then I should see "Camera"

  Scenario: Search product by availability
    Given the following products
      | name     | category | available | price |
      | Blender  | Kitchen  | false     | 35.00 |
    When I search for products that are not available
    Then I should see "Blender"