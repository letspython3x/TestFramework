import json

from app.utils import get_browser


class LoginPage:
    def __init__(self, url, username=None, password=None):
        self.url = url
        self.username = username
        self.password = password
        self._browser = None
        self.locators = 'locators/loginPage.json'
        self.usernameXPath = None
        self.passwordXPath = None
        self.loginXPath = None
        self.set_xpath()

    @property
    def browser(self):
        """

        :return: Browser object
        """
        if self._browser is None:
            self._browser = get_browser()
        return self._browser

    def fill_username(self, xpath=None, username=None):
        """
        fills the username on the login page
        :param xpath: xpath for username field
        :param username: username to be filled in
        :return: None
        """
        username = username or self.username
        xpath = xpath or self.usernameXPath
        self.browser.find_element_by_xpath(xpath).send_keys(username)

    def fill_password(self, xpath=None, password=None):
        """
        fills the password on the login page
        :param xpath: xpath for password field
        :param password: password to be filled in
        :return: None
        """
        password = password or self.password
        xpath = xpath or self.passwordXPath
        self.browser.find_element_by_xpath(xpath).send_keys(password)

    def click_login_button(self, xpath=None):
        """
        fills the password on the login page
        :param xpath: xpath for password field
        :param password: password to be filled in
        :return: None
        """
        xpath = xpath or self.loginXPath
        self.browser.find_element_by_xpath(xpath).click()

    def set_xpath(self):
        with open(self.locators) as fin:
            config = json.load(fin)
            for item in config:
                if item["field"].lower() == "username":
                    self.usernameXPath = item["xpath"]
                elif item["field"].lower() == "password":
                    self.passwordXPath = item["xpath"]
                elif item["field"].lower() == "loginButton":
                    self.loginXPath = item["xpath"]

    def execute(self):
        self.fill_username()
        self.fill_password()
        self.click_login_button()
