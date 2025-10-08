@smoke
Feature: Smoke test and sign off
  @smoke1
  Scenario: To conduct a quick smoke run
    Given User inside Automation Practise website
    When User expands the Forms tab
    Then User clicks on Components and verify the url
      | component     | url_contains                              |
      | Practice Form | practice/selenium_automation_practice.php |
      | Login         | practice/login.php                        |
      | Register      | practice/register.php                     |
    When User expands the Widgets tab
    Then User clicks on Components and verify the url
      | component   | url_contains    |
      | Accordion   | accordion.php   |
      | Date Picker | date-picker.php |
      | Slider      | slider.php      |
    When User expands the Elements tab
    Then User clicks on Components and verify the url
      | component | url_contains  |
      | Text Box  | text-box.php  |
      | Check Box | check-box.php |
      | Buttons   | buttons.php   |