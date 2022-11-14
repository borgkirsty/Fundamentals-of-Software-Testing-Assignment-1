Feature: Login

#Test 1
Scenario: Valid Login
    Given I am a user of marketalertum
    When I login with valid credentials
    Then I should see my alerts

#Test 2
Scenario: Invalid Login
    Given I am a user of marketalertum
    When I login with invalid credentials
    Then I should see the login screen again