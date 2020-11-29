from selenium.webdriver.common.by import By

class LoginPage:
    """Класс описывающий страницу аутентификации"""

    login_locator =  (By.CSS_SELECTOR, '[name="mobile_phone"]')
    password_locator = (By.CSS_SELECTOR, '[name="password"]')
    enter_locator = (By.CSS_SELECTOR, '[name="commit"]')
    banner_locator = (By.CLASS_NAME, 'span')

    def __init__(self, driver):
        self.driver = driver

    def enter_button_click(self):
        """Нажимаем кнопку Войти"""

        enter_btn = self.driver.find_element(*self.enter_locator)
        assert enter_btn.is_enabled(), 'На экране не появилась кнопка Войти'
        enter_btn.click()

    def check_banner_text(self, banner_text):
        """Проверяем, что на странице есть информация о неудачной попытке аутентификации"""

        banner_text_elm = self.driver.find_element(*self.banner_locator)
        assert banner_text_elm.is_enabled(), 'Текст ошибки не появился после клика по кнопке Войти'
        assert banner_text_elm.text == banner_text, \
            'Текст ошибки при некорректной аутентификации отличен от {}'.format(banner_text)
