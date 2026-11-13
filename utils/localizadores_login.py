from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a.ico-logout")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".validation-summary-errors")