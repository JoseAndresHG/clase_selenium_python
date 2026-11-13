import os

from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.localizadores_login import LoginLocators


@given("que el usuario abre la página de inicio de sesión")
def abrir_inicio_sesion(context):
    context.driver.get(context.base_url)


@when("inicia sesión con sus credenciales configuradas")
def iniciar_sesion_con_credenciales_configuradas(context):
    email = os.getenv("LOGIN_EMAIL")
    password = os.getenv("LOGIN_PASSWORD")
    if not email or not password:
        raise RuntimeError(
            "Configura las variables de entorno LOGIN_EMAIL y LOGIN_PASSWORD "
            "con una cuenta válida de Demo Web Shop."
        )

    context.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(email)
    context.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    context.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


@then("el inicio de sesión es exitoso")
def validar_inicio_sesion_exitoso(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(LoginLocators.LOGOUT_LINK)
    )


@when("intenta iniciar sesión con credenciales incorrectas")
def iniciar_sesion_con_credenciales_incorrectas(context):
    context.driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(
        "qa-invalid-login@example.invalid"
    )
    context.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(
        "InvalidPassword123!"
    )
    context.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


@then("se muestra un error de credenciales")
def validar_error_de_credenciales(context):
    message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE)
    )
    assert "Login was unsuccessful" in message.text, (
        f"Se esperaba el error de credenciales, pero se mostró: {message.text!r}"
    )
