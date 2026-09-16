from pages.page_saucedemoLogin import LogInPage
from playwright.sync_api import expect
import pytest



# def test_saucelogin(page):
#     login = LogInPage(page)
#     login.enterUsername("standard_user")
#     login.enterPassword("secret_sauce")
#     login.clickLogIn()
#     login.ProductsText_visibile()


@pytest.mark.order(1)
@pytest.mark.parametrize("username, password, expected",[
("locked_out_user", "secret_sauce", "error"),
("problem_user", "secret_sauc", "error"),
("performance_glitch_user", "secret_sauc", "error"),
("error_user", "secret_sa", "error"),
# ("visual_user", "secret_sauce", "error"),
("standard_user", "secret_sauce", "success"),
])
def test_parametrizelogin(page, username, password, expected):
    login = LogInPage(page)
    login.enterUsername(username)
    login.enterPassword(password)
    login.clickLogIn()
    # login.ProductsText_visibile()

    if expected == "success":
        assert "inventory" in page.url
    else:
        expect(page.locator(".error-message-container.error")).to_be_visible()
        # assert login.get_error_msg()