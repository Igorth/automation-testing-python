# Automation Testing Frameworks Python

This repository demonstrates how to use different testing frameworks in Python to automate the verification of a simple ToDo application.
The tests were executed on the [LambdaTest](https://www.lambdatest.com/) Automation platform, allowing them to run in different cloud environments.

## Sample

[LambdaTest Sample App](https://lambdatest.github.io/sample-todo-app/)

## Test Scenario

The test scenario for the 'LambdaTest Sample App' application is as follows:

1. **Open the ToDo App page.**
2. **Click to check the first ToDo item.**
3. **Verify that the item is marked as done.**
4. **Add a new ToDo item.**
5. **Check that the total number of ToDos is 6.**
6. **Close the browser.**

## Testing Tools Used

### 1. Unittest
`unittest` is the default testing framework in Python. It is inspired by the JUnit framework for Java and is used to write and run unit tests.

**Features:**
- Support for test case creation using test classes and methods.
- Assertions for verifying expected outcomes.
- Test fixture management for setup and teardown.
- Test discovery based on naming conventions and test suites.
- Integration with other testing tools and frameworks.

### 2. Pytest
`pytest` is a more advanced and popular testing framework in the Python ecosystem, used to write and run tests more flexibly and powerfully.

**Features:**
- Support for test discovery and execution based on naming conventions.
- Powerful test selection and filtering capabilities.
- pytest fixtures for managing test resources and dependencies.
- Ability to run parallel tests for faster execution.
- Seamless integration with other testing tools and frameworks.

### 3. Behave
`behave` is a tool for Behavior-Driven Development (BDD) that allows writing tests in a language closer to natural language, using Gherkin.

**Features:**
- Support for writing tests in a human-readable Gherkin syntax.
- Ability to define step definitions that map to test actions.
- Built-in support for data-driven testing.
- Rich reporting and visualization options.
- Integration with other testing tools and frameworks.
## How to Run the Tests

### Prerequisites
Before running the tests, ensure that you have the following installed:
- Python 3.x
- pip (Python package installer)
- Necessary dependencies (specified in `requirements.txt` or install as you go)

### Running unittest
To run the tests using `unittest`, navigate to the project directory and execute the following command:
```bash
python test_todo_app_unittest.py
```

### Running pytest
To run the tests using `pytest`, navigate to the project directory and execute the following command:
```bash
python test_todo_app_pytest.py
```

### Running behave
To run the tests using `behave`, navigate to the project directory and execute the following command:
```bash
cd behave_framework
behave
```

## Conclusion

Each of these testing tools offers unique advantages that cater to different needs in the automated testing process. 
`unittest` is ideal for simple and straightforward tests, 
`pytest` provides a richer and more flexible solution, 
while `behave` is excellent for scenarios where behavior and test clarity are crucial. 
Using the LambdaTest Automation platform, these tests can be run in various environments, 
ensuring the application functions as expected across different configurations.

## Resources
[LambdaTest](https://www.lambdatest.com/learning-hub/python-basics)