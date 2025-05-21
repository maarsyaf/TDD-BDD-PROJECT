from behave import when, then

@when('I search for products with name "{name}"')
def step_impl(context, name):
    context.browser.get(f"http://localhost:5000/products?name={name}")

@when('I search for products with category "{category}"')
def step_impl(context, category):
    context.browser.get(f"http://localhost:5000/products?category={category}")

@when('I search for products that are not available')
def step_impl(context):
    context.browser.get("http://localhost:5000/products?available=false")

@when('I visit the "Home Page"')
def step_impl(context):
    context.browser.get("http://localhost:5000/products")

@then('I should see "{name}"')
def step_impl(context, name):
    assert name in context.browser.page_source