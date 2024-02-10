import time

from selene import browser, be, have


class LoginPage:
    def __init__(self):
        pass

    def open_page(self):
        browser.open('https://2gis.ru/novosibirsk')
        browser.element('._h3r6b0').click()
        # browser.element("//div[@role='button'][4]").click()
        # browser.element("//div[contains(text(),'Войти через Google')]").click()
        browser.all('._s8opx9').element_by_its('div', have.exact_text('Войти через Google')).click()
        time.sleep(3)
        return self


login_page = LoginPage()
