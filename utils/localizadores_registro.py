from selenium.webdriver.common.by import By

class RegistrationLocators:
    # Locators for the registration page
    GENDER_RADIO_BUTTON = "gender-male"
    GENDER_RADIO_BUTTON_FEMALE = "gender-female"
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "result")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message")