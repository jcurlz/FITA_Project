@scenario @tab
Feature:Inside Demo website
    Background:
    Given User inside Automation Practise website

    @form
Scenario:Test Login Page for Automation Testing Practice
      When User expands the Form tab
      Then User clicks on Practice Form and executes cases in TC_01 from TestCases.xlsx file

  @element
Scenario:Test Login Page for Automation Testing Practice
      When User expands the Elements tab
      Then User clicks on TextBox and executes cases in TC_02 from TestCases.xlsx file


  @widget
Scenario:Test Login Page for Automation Testing Practice
      When User expands the Widget tab
      Then User clicks on Accordions and executes cases in TC_03 from TestCases.xlsx file



