from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.helper import *


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.helper = GroupHelper()
        self.helper = ContactHelper()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()