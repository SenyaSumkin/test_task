from selenium import webdriver
import unittest
from login_page import LoginPage

class FailedLoginTest(unittest.TestCase):
    """В классе проверяются негативные сценарии аутентификации на https://partner-02.st.revoup.ru/"""

    site_url = 'https://partner-02.st.revoup.ru'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cls.site_url)

    def test_empty_login_banner(self):
        """Проверяем оповещение для пользователя при некорректном вводе логина/пароля"""

        # текст, который должен быть виден пользователю при некорректной аутентификации
        error_text = 'Неправильный логин или пароль'

        login_page = LoginPage(self.driver)
        login_page.enter_button_click()
        login_page.check_banner_text(error_text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
   unittest.main()
