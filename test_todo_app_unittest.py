import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


# Load environment variables from.env file
load_dotenv()


# Test class to verify the Todo App functionality
class TodoAppTest(unittest.TestCase):
    def test_verify_todo_app_functionality(self):
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

        driver = webdriver.Remote(
            command_executor=url,
            options=options,
        )

        driver.get("https://lambdatest.github.io/sample-todo-app/")
        driver.maximize_window()

        checkbox = driver.find_element(By.NAME, "li1")
        checkbox.click()
        assert checkbox.is_selected()

        text_field = driver.find_element(By.ID, 'sampletodotext')
        text_field.send_keys("Test Todo new item")

        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()

        todos = driver.find_elements(By.CSS_SELECTOR, 'ul.list-unstyled li')
        assert len(todos) == 6


# Run the test class using unittest
if __name__ == '__main__':
    unittest.main()
