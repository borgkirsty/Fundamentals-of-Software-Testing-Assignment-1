Feature: Icons


#Test 5
Scenario Outline: Icon Check
    Given I am an administrator of the website and I upload an alert of type <alert_type>
    Given I am a user of marketalertum
    When I view a list of alerts
    Then I should see 1 alerts
    And the icon displayed should be <icon_file_name>

    Examples:
        | alert_type | icon_file_name           |
        | 1          | icon-car.png             |
        | 2          | icon-boat.png            |
        | 3          | icon-property-rent.jpg   |
        | 4          | icon-property-sale.jpg   |
        | 5          | icon-toys.png            |
        | 6          | icon-electronics.png     |