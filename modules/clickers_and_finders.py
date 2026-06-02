'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''

from config.settings import click_gap, smooth_scroll
from modules.helpers import buffer, print_lg, sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

# Helper to get the actual WebDriver instance if a WebElement was passed as the context
def _get_driver(driver: WebDriver | WebElement) -> WebDriver:
    return driver.parent if isinstance(driver, WebElement) else driver

# Click Functions
def wait_span_click(driver: WebDriver, text: str, time: float=5.0, click: bool=True, scroll: bool=True, scrollTop: bool=False) -> WebElement | bool:
    '''
    Finds the filter option (checkbox or radio) element with the given `text`.
    - Returns `WebElement` if found, else `False` if not found.
    '''
    if text:
        try:
            # Robust locator for classic filter options (label containing the exact text inside a span)
            xpath = f'.//label[.//span[normalize-space(.)="{text}"] or normalize-space(.)="{text}"]'
            button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, xpath)))
            if scroll:  scroll_to_view(driver, button, scrollTop)
            if click:
                try:
                    button.click()
                except Exception as click_err:
                    print_lg(f"Normal click failed for '{text}', attempting JS click... Error: {click_err}")
                    _get_driver(driver).execute_script("arguments[0].click();", button)
                buffer(click_gap)
            return button
        except Exception as e:
            try:
                # Fallback to standard span click
                button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, f'.//span[normalize-space(.)="{text}"]')))
                if scroll:  scroll_to_view(driver, button, scrollTop)
                if click:
                    try:
                        button.click()
                    except Exception as click_err:
                        print_lg(f"Normal fallback click failed for '{text}', attempting JS click... Error: {click_err}")
                        _get_driver(driver).execute_script("arguments[0].click();", button)
                    buffer(click_gap)
                return button
            except Exception as fallback_err:
                print_lg(f"Click Failed! Didn't find '{text}'. Error: {e} | Fallback Error: {fallback_err}")
                return False

def multi_sel(driver: WebDriver, texts: list, time: float=5.0) -> None:
    '''
    - For each text in the `texts`, tries to find and click `span` element with that text.
    - Will spend a max of `time` seconds in searching for each element.
    '''
    for text in texts:
        wait_span_click(driver, text, time, click=True)

def multi_sel_noWait(driver: WebDriver, texts: list, actions: ActionChains = None) -> None:
    '''
    - For each text in the `texts`, tries to find and click `span` element with that class.
    - If `actions` is provided, bot tries to search and Add the `text` to this filters list section.
    - Won't wait to search for each element, assumes that element is rendered.
    '''
    for text in texts:
        if not wait_span_click(driver, text, click_gap, click=True):
            if actions: company_search_click(driver, actions, text)

def boolean_button_click(driver: WebDriver, actions: ActionChains, text: str) -> None:
    '''
    Tries to click on the boolean toggle button with the given `text` text based on Playwright verified DOM structure.
    '''
    try:
        # Robust locator for Playwright verified toggle switch inside a fieldset
        xpath = f'.//fieldset[.//h3[normalize-space(.)="{text}"]]//input[@type="checkbox" or @role="switch"]'
        button = driver.find_element(By.XPATH, xpath)
        scroll_to_view(driver, button)
        try:
            actions.move_to_element(button).click().perform()
        except Exception as act_err:
            print_lg(f"ActionChains click failed for toggle '{text}', attempting JS click... Error: {act_err}")
            _get_driver(driver).execute_script("arguments[0].click();", button)
        buffer(click_gap)
    except Exception as e:
        try:
            # Fallback to standard aria-label toggle
            button = driver.find_element(By.XPATH, f'.//button[contains(@aria-label, "{text}")]')
            scroll_to_view(driver, button)
            try:
                button.click()
            except Exception as click_err:
                print_lg(f"Fallback click failed for toggle '{text}', attempting JS click... Error: {click_err}")
                _get_driver(driver).execute_script("arguments[0].click();", button)
            buffer(click_gap)
            return
        except Exception as fallback_err:
            print_lg(f"Click Failed! Didn't find toggle '{text}'. Error: {e} | Fallback Error: {fallback_err}")

def add_dynamic_filter(driver: WebDriver, actions: ActionChains, category_name: str, items: list) -> None:
    '''
    Clicks "Add a {category_name}", types the item, and selects it from the dropdown.
    '''
    for item in items:
        try:
            add_button = driver.find_element(By.XPATH, f'.//button[contains(., "Add a {category_name}")]')
            scroll_to_view(driver, add_button)
            add_button.click()
            buffer(1)
            
            search_input = driver.find_element(By.XPATH, f'(.//input[contains(@placeholder, "Add a {category_name}")])[1]')
            search_input.send_keys(Keys.CONTROL + "a")
            search_input.send_keys(item)
            buffer(3)
            actions.send_keys(Keys.DOWN).perform()
            actions.send_keys(Keys.ENTER).perform()
            print_lg(f'Successfully added {category_name}: "{item}"')
            buffer(click_gap)
        except Exception as e:
            print_lg(f'Failed to add dynamic filter {category_name}: "{item}"')

# Find functions
def find_by_class(driver: WebDriver, class_name: str, time: float=5.0) -> WebElement | Exception:
    '''
    Waits for a max of `time` seconds for element to be found, and returns `WebElement` if found, else `Exception` if not found.
    '''
    return WebDriverWait(driver, time).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

# Scroll functions
def scroll_to_view(driver: WebDriver, element: WebElement, top: bool = False, smooth_scroll: bool = smooth_scroll) -> None:
    '''
    Scrolls the `element` to view.
    - `smooth_scroll` will scroll with smooth behavior.
    - `top` will scroll to the `element` to top of the view.
    '''
    if top:
        return _get_driver(driver).execute_script('arguments[0].scrollIntoView();', element)
    behavior = "smooth" if smooth_scroll else "instant"
    return _get_driver(driver).execute_script('arguments[0].scrollIntoView({block: "center", behavior: "'+behavior+'" });', element)

# Enter input text functions
def text_input_by_ID(driver: WebDriver, id: str, value: str, time: float=5.0) -> None | Exception:
    '''
    Enters `value` into the input field with the given `id` if found, else throws NotFoundException.
    - `time` is the max time to wait for the element to be found.
    '''
    username_field = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.ID, id)))
    username_field.send_keys(Keys.CONTROL + "a")
    username_field.send_keys(value)

def try_xp(driver: WebDriver, xpath: str, click: bool=True) -> WebElement | bool:
    try:
        element = driver.find_element(By.XPATH, xpath)
        if click:
            try:
                element.click()
            except Exception as click_err:
                print_lg(f"try_xp normal click failed, attempting JS click... Error: {click_err}")
                _get_driver(driver).execute_script("arguments[0].click();", element)
            return True
        else:
            return element
    except: return False

def try_linkText(driver: WebDriver, linkText: str) -> WebElement | bool:
    try:    return driver.find_element(By.LINK_TEXT, linkText)
    except:  return False

def try_find_by_classes(driver: WebDriver, classes: list[str]) -> WebElement | ValueError:
    for cla in classes:
        try:    return driver.find_element(By.CLASS_NAME, cla)
        except: pass
    raise ValueError("Failed to find an element with given classes")

def company_search_click(driver: WebDriver, actions: ActionChains, companyName: str) -> None:
    '''
    Tries to search and Add the company to company filters list.
    '''
    wait_span_click(driver,"Add a company",1)
    search = driver.find_element(By.XPATH,"(.//input[@placeholder='Add a company'])[1]")
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(companyName)
    buffer(3)
    actions.send_keys(Keys.DOWN).perform()
    actions.send_keys(Keys.ENTER).perform()
    print_lg(f'Tried searching and adding "{companyName}"')

def text_input(actions: ActionChains, textInputEle: WebElement | bool, value: str, textFieldName: str = "Text") -> None | Exception:
    if textInputEle:
        sleep(1)
        # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        textInputEle.clear()
        textInputEle.send_keys(value.strip())
        sleep(2)
        actions.send_keys(Keys.ENTER).perform()
    else:
        print_lg(f'{textFieldName} input was not given!')

def is_filter_selected(driver: WebDriver, text: str) -> bool:
    '''
    Checks if a filter with the given text is selected in the UI by examining the associated <input> element.
    '''
    try:
        # Check standard checkbox/radio
        xpath = f'.//label[.//span[normalize-space(.)="{text}"] or normalize-space(.)="{text}"]'
        label = driver.find_element(By.XPATH, xpath)
        for_attr = label.get_attribute("for")
        if for_attr:
            input_el = driver.find_element(By.ID, for_attr)
            return input_el.is_selected()
        else:
            input_el = driver.find_element(By.XPATH, f'{xpath}/preceding-sibling::input | {xpath}//input')
            return input_el.is_selected()
    except:
        pass
    
    try:
        # Check toggle switches inside fieldsets
        xpath = f'.//fieldset[.//h3[normalize-space(.)="{text}"]]//input[@type="checkbox" or @role="switch"]'
        input_el = driver.find_element(By.XPATH, xpath)
        return input_el.is_selected()
    except:
        pass

    try:
        # Check aria-checked attribute on buttons (fallback)
        xpath = f'.//button[contains(@aria-label, "{text}")]'
        button = driver.find_element(By.XPATH, xpath)
        aria_checked = button.get_attribute("aria-checked")
        return aria_checked == "true"
    except:
        return False