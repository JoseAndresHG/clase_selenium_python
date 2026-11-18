from asyncio import wait
from multiprocessing import context
from random import random
from selenium.common.exceptions import TimeoutException
from behave import given, step, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from utils.localizadores_registro import RegistrationLocators
from utils.assertions import validar_texto_elemento
from selenium.webdriver.support.ui import WebDriverWait
import time


@given('que la pagina abre el registro')
def step_impl(context):
    context.driver.get("https://demowebshop.tricentis.com/register")

@when('el usuario se registra')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)    
    random = int(time.time())
    # Completar el formulario de registro
    wait.until(EC.element_to_be_clickable((By.ID, RegistrationLocators.GENDER_RADIO_BUTTON))).click()
    wait.until(EC.presence_of_element_located(RegistrationLocators.FIRST_NAME_INPUT)).send_keys("Andres")
    wait.until(EC.presence_of_element_located((RegistrationLocators.LAST_NAME_INPUT))).send_keys("Hernandez")
    wait.until(EC.presence_of_element_located((RegistrationLocators.EMAIL_INPUT))).send_keys(f"jose.hernandez+{random}@gmail.com")
    wait.until(EC.presence_of_element_located((RegistrationLocators.PASSWORD_INPUT))).send_keys("Password123!")
    wait.until(EC.presence_of_element_located((RegistrationLocators.CONFIRM_PASSWORD_INPUT))).send_keys("Password123!")
    wait.until(EC.element_to_be_clickable((RegistrationLocators.REGISTER_BUTTON))).click()


@step('el usuario ve el mensaje "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    validar_texto_elemento(
        driver=context.driver,
        localizador=RegistrationLocators.SUCCESS_MESSAGE,
        texto_esperado=mensaje_esperado,
)