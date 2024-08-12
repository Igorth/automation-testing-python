from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


@given('I open the Todo App page')
def open_todo_app_page(context):
    username = os.getenv('LT_USERNAME')
    access_token = os.getenv('LT_ACCESS_TOKEN')
    grid_url = "hub.lambdatest.com/wd/hub"

    options = webdriver.ChromeOptions()
    options.browser_version = "113.0"
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = username
    lt_options["accessKey"] = access_token
    lt_options["build"] = "Todo App Test"
    lt_options["project"] = "Todo App"
    lt_options["name"] = "QA"
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{access_token}@{grid_url}"

    context.driver = webdriver.Remote(
        command_executor=url,
        options=options,
    )

    context.driver.get("https://lambdatest.github.io/sample-todo-app/")
    context.driver.maximize_window()


@when('I check the first todo item')
def check_first_todo_checked(context):
    checkbox = context.driver.find_element(By.NAME, "li1")
    checkbox.click()


@then('the first todo item should be checked')
def check_first_todo_done(context):
    checkbox = context.driver.find_element(By.NAME, "li1")
    assert checkbox.is_selected()


@then('a new todo can be added')
def add_new_todo(context):
    text_field = context.driver.find_element(By.ID, "sampletodotext")
    text_field.send_keys("New Item")
    add_button = context.driver.find_element(By.ID, "addbutton")
    add_button.click()


@then('the total number of todos should be {count:d}')
def check_total_todos_count(context, count):
    todos = context.driver.find_elements(By.CSS_SELECTOR, 'ul.list-unstyled li')
    assert len(todos) == count


@then('the browser should be closed')
def close_browser(context):
    context.driver.quit()
