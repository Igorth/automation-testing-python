Feature: Automate Todo App

  Scenario: Verify Todo App functionality
    Given I open the Todo App page
    When I check the first todo item
    Then the first todo item should be checked
    And a new todo can be added
    And the total number of todos should be 6
    And the browser should be closed