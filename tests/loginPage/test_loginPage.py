from pytest_bdd import given, when, then, scenario
from app.LoginPages.login import LoginPage

FEATURE_FILE = "tests/loginPage/loginPage.feature"
URL = "https://www.saucedemo.com/"


@scenario(FEATURE_FILE, "Outlined given, when & then")
def test_outlined():
    pass


@given("user provides <username> and <password>", target_fixture="data")
def data(username, password):
    return dict(username=username, password=password)


@when("user clicks on Login Button")
def login(data):
    pageObj = LoginPage(URL)
    pageObj.fill_username(username=data.get("username"))
    pageObj.fill_password(password=data.get("password"))
    pageObj.click_login_button()
    data["pageObj"] = pageObj


@then("result page should have <xpath> containing <text>")
def show_products(data, xpath, text):
    pageObj = data["pageObj"]
    elementText = pageObj.find_element_by_xpath(xpath).text
    assert text.strip() in elementText.strip()
