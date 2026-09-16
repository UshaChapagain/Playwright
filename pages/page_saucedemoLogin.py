from playwright.sync_api import Page, expect

class LogInPage:
    def __init__(self, page:Page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.Title = page.get_by_text("Products")
        self.error_msg =page.locator(".error-message-container.error")

    def enterUsername(self, username:str):
        self.username_input.fill(username)
    def enterPassword(self, password:str):
        self.password_input.fill(password)
    def clickLogIn(self):
        self.login_button.click()


    def login(self, username:str, password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def ProductsText_visibile(self):
        self.Title.is_visible()

    # def get_error_msg(self):
    #     self.error_msg.is_visible()

