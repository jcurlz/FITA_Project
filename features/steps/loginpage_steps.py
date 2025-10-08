from lib2to3.pgen2 import driver
from behave import given, when, then, parser
from utility.CustomContext import CustomContext


@given('User inside Automation Practise website')
def step_impl(context):
    assert "Selenium Practice" in context.driver.title, f"Expected {context.driver.title}"
    print("Selenium Practice Assertion")

@when('User expands the {tab_specification} tab')
def step_impl(context : CustomContext, tab_specification):
    tab_locator, tab_status = context.login.specification_tab(tab_specification)
    context.login.expand_or_collapse_it(tab_status = tab_status, locator=tab_locator, element_to_ExpandOrCollapse = tab_specification)


@then('User clicks on {components} and executes cases in {testcase} from {TestCaseFile} file')
def step_impl(context : CustomContext, testcase : str, components, TestCaseFile: str) :
    print(f"{components} cases Verification in progress...")
    context.excel.read_my_excel(testcase, TestCaseFile)

@then('User clicks on Components and verify the url')
def step_impl(context: CustomContext):
    for row in context.table:
        component = row['component']
        url_contains = row['url_contains']
        context.comm.elementClick(context.login.component_path(component))
        context.comm.verify_url_contains(url_contains)
    context.driver.refresh()
 
    