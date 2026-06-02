# 🧑‍💻 Contributor Guidelines

Thank you for your efforts and being a part of the community. All contributions are appreciated no matter how small or big. Once you contribute to the code base, your work will be remembered forever.

NOTE: Only Pull request to `community-version` branch will be accepted. Any other requests will be declined by default, especially to main branch.
Once your code is tested, your changes will be merged to the `main` branch in next cycle.

### Code Guidelines
#### Functions:
1. All functions or methods are named lower case and snake case
2. Must have explanation of their purpose. Write explanation surrounded in `''' Explanation '''` under the definition `def function() -> None:`. Example:
    ```python
    def function() -> None:
      '''
      This function does nothing, it's just an example for explanation placement!
      '''
    ```
3. The Types `(str, list, int, list[str], int | float)` for the parameters and returns must be given. Example:
    ```python
    def function(param1: str, param2: list[str], param3: int) -> str:
    ```
4. Putting all that together some valid examples for function or method declarations would be as follows.
    ```python
    def function_name_in_camel_case(parameter1: driver, parameter2: str) -> list[str] | ValueError:
      '''
      This function is an example for code guidelines
      '''
      return [parameter2, parameter2.lower()]
    ```
5. The hashtag comments on top of functions are optional, which are intended for developers `# Comments for developers`.
    ```python
    # Enter input text function
    def text_input_by_ID(driver: WebDriver, id: str, value: str, time: float=5.0) -> None | Exception:
        '''
        Enters `value` into the input field with the given `id` if found, else throws NotFoundException.
        - `time` is the max time to wait for the element to be found.
        '''
        username_field = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.ID, id)))
        username_field.send_keys(Keys.CONTROL + "a")
        username_field.send_keys(value)
    ```
  
#### Variables
1. All variables must start with lower case, must be in explainable full words. If someone reads the variable name, it should be easy to understand what the variable stores.
2. All local variables are camel case. Examples:
    ```python
    jobListingsElement = None
    ```
    ```python
    localBufferTime = 5.5
    ```
3. All global variables are snake case. Example:
    ```
    total_runs = 1
    ```
4. Mentioning types are optional.
    ```python
    localBufferTime: float | int = 5.5
    ```

#### Configuration variables
1. All config variables are treated as global variables. They have some extra guidelines.
2. Must have variable setting explanation, and examples of valid values. Examples:
    ```python
    # Explanation of what this setting will do, and instructions to enter it correctly
    config_variable = "value1"    #  <Valid values examples, and NOTES> "value1", "value2", etc. Don't forget quotes ("")
    ```
    ```python
    # Do you want to randomize the search order for search_terms?
    randomize_search_order = False     # True of False, Note: True or False are case-sensitive
    ```
    ```python
    # Avoid applying to jobs if their required experience is above your current_experience. (Set value as -1 if you want to apply to all ignoring their required experience...)
    current_experience = 5             # Integers > -2 (Ex: -1, 0, 1, 2, 3, 4...)
    ```
    ```python
    # Search location, this will be filled in "City, state, or zip code" search box. If left empty as "", tool will not fill it.
    search_location = "United States"               # Some valid examples: "", "United States", "India", "Chicago, Illinois, United States", "90001, Los Angeles, California, United States", "Bengaluru, Karnataka, India", etc.
    ```
3. Add the config variable in appropriate `/config/file`.
4. Every config variable must be validated. Go to `/modules/validator.py` and add it over there. Example:
    For config variable `search_location = ""` found in `/config/search.py`, string validation is added in file `/modules/validator.py` under the method `def validate_search()`.
    ```python
    def validate_search() -> None | ValueError | TypeError:
        '''
        Validates all variables in the `/config/search.py` file.
        '''
        check_string(search_location, "search_location")
    ```

### Attestation
1. All contributions require proper attestion. Format for attestation:
```python
##> ------ <Your full name> : <github id> OR <email> - <Type of change> ------
    print("My contributions 😍") # Your code
##<
```
2. Examples for proper attestation:
New feature example
```python
##> ------ Sai Vignesh Golla : godsscion - Feature ------
def alert_box(title: str, message: str) -> None:
  '''
  Shows an alert box with the given `title` and `message`.
  '''
  from pyautogui import alert
  return alert(title, message)
##<
```

Bug fix example
```python
def alert_box(title: str, message: str) -> None:
  '''
  Shows an alert box with the given `title` and `message`.
  '''
  from pyautogui import alert

##> ------ Sai Vignesh Golla : saivigneshgolla@outlook.com - Bug fix ------
  return alert(message, title)
##<
```
