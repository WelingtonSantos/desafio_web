# Features 
Feature: Open a new browser window
  As a user
  I want to open a new browser window
  So that I can verify the "This is a sample page" message

  Scenario1: Open new window and validate message
    Given I am on the home page of "https://demoqa.com"
    When I click on "Alerts, Frame & Windows"
    And I navigate to "Browser Windows"
    And I click on "New Window" button
    Then I should see a new window with the message "This is a sample page"


