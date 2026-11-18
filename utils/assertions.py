from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def validar_texto_elemento(
    driver, localizador, texto_esperado, timeout=10, coincidencia_exacta=True
):
    """Valida que un elemento sea visible y contenga o coincida con el texto esperado."""
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(localizador)
        )
        texto_actual = elemento.text.strip()

        if coincidencia_exacta:
            assert (
                texto_esperado == texto_actual
            ), f"Error de texto: se esperaba '{texto_esperado}', pero apareció '{texto_actual}'"
        else:
            assert (
                texto_esperado in texto_actual
            ), f"Error de texto: no se encontró '{texto_esperado}' dentro de '{texto_actual}'"

    except TimeoutException:
        raise AssertionError(
            f"No se encontró el elemento {localizador} tras {timeout} segundos."
        )