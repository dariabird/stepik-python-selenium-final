from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.contains("/login"), "No 'login' in url of the Login page"

    def should_be_login_form(self):
        assert self.is_element_present(self, *LoginPage.LOGIN_FORM), "No login form present on the Login page"

    def should_be_register_form(self):
        assert self.is_element_present(self, *LoginPage.REGISTER_FORM), "No register form present on the Login page"
