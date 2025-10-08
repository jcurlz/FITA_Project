BASE_URL = 'https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php'
Headless = False
if Headless:
    ModeOfExecution = 'Headed(UI)'
else:
    ModeOfExecution = "Headless(CLI)"