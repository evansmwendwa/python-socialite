"""Main module."""
from python_socialite.drivers.google import GoogleProvider


class OAuthProvider:
    def __init__(self, driver, config):
        credentials = config.get(driver)
        if driver == "google":
            self.provider = GoogleProvider(credentials)
        else:
            raise ValueError("Invalid socialite driver")

    def set_scopes(self, scopes):
        self.provider.set_scopes(scopes)
        return self

    def get_auth_url(self):
        return self.provider.get_auth_url()

    def get_token(self, code):
        return self.provider.get_token(code)

    def get_user(self, access_token):
        return self.provider.get_user(access_token)
