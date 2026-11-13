from selenium import webdriver

def before_all(context):
    context.base_url = "https://demowebshop.tricentis.com/login"
    
    context.browser = context.config.userdata.get("browser", "chrome").lower()

def before_scenario(context, scenario):
    if context.browser == "chrome":
        context.driver = webdriver.Chrome()
    elif context.browser == "firefox":
        context.driver = webdriver.Firefox()
    elif context.browser == "edge":
        context.driver = webdriver.Edge()
    else:
        raise ValueError(f"Navegador no soportado: '{context.browser}'. Usa chrome, firefox o edge.")

    context.driver.maximize_window()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
