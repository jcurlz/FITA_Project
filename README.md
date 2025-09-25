# Automation Practise Website #
https://practice.expandtesting.com/



## Behave Project Structure ##
ProjRootFolder
|_features
    |_file.feature
    |_steps
      |_ file_steps.py
    |_ environment.py
|_utility
    |_ excel.xslx
|_runner.py
|_requirements.txt
|_README.md

## Virtual Env setup ##
Create an interpreter or python -m venv .venv
.venv\Scripts\activate

## Requirement installation ##
pip install behave, selenium, openpyxl
pip list
Pick out the required libs from the list and add to your requirements.txt
pip install -r requirements.txt
