from operator import contains
import time
from sys import flags

from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CommonMethods():
    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def locatePresenceOfElement(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elementClick(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
        except StaleElementReferenceException:
            element = self.locatePresenceOfElement(locator)
            element.click()
        except Exception:
            print(Exception)

    def clearAndEnter(self, locator, data):
        element = self.locatePresenceOfElement(locator)
        self.elementClick(element)
        try:
            element.clear()
        except:
            self.driver.execute_script("arguments[0].value = '';", element)
        try:
            element.send_keys(data)
        except:
            self.driver.execute_script("arguments[0].value = arguments[1];", element, data)

    def verify_text(self, locator, exp):
        time.sleep(2)
        act = self.locatePresenceOfElement(locator).text.strip()
        # act_list = [a for a in act.split(" ")]
        # exp_list = [e for e in exp.split(" ")]
        # for a, e in zip(act_list, exp_list):
        #     print(a, e)
        assert exp in act, f"Actual {act}"

    def verify_url_contains(self, exp_endpoint):
        time.sleep(2)
        assert exp_endpoint in self.driver.current_url, f"Actual url {self.driver.current_url} does not contain expected {exp_endpoint}"
        print(f"{exp_endpoint} asserted")

    def dropdownSelector(self, locator, value):
        element = self.locatePresenceOfElement(locator)
        select = Select(element)
        select.select_by_value(value=value)

    def print_text(self, locator):
        time.sleep(1.5)
        element = self.locatePresenceOfElement(locator=locator)
        print(element.text)


