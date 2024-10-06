# Features 
Feature: Open a new browser window
  As a user
  I want to open a Widgets window
  So that I can verify the progress bar at 25%
  And I can verity the progress bar at 100%
  
  Scenario: Open new windown and validate a progress bar
    Given I am on the home page of "https://demoqa.com"
    When I click on "Widgets" button
    And I navigate to "Progress Bar"
    And I validate the progress bar at 25%

