from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, by, locator, condition="clickable", timeout=10):
    conditions = {
        "clickable": EC.element_to_be_clickable,
        "visible": EC.visibility_of_element_located,
        "present": EC.presence_of_element_located,
    }
    return WebDriverWait(driver, timeout).until(conditions[condition]((by, locator)))
