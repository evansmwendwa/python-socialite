import requests
from python_socialite.drivers.abstract_driver import AbstractDriver
from python_socialite.drivers.abstract_user import abstract_user


class GoogleProvider(AbstractDriver):
    def __init__(self, config):
        super().__init__(config)
        self.scopes = config.get("scopes", ["openid", "email", "profile"])

    def get_auth_url(self):
        url = "https://accounts.google.com/o/oauth2/v2/auth"
        return self.build_url(url)

    def get_token_url(self):
        return "https://www.googleapis.com/oauth2/v4/token"

    def get_token_fields(self, code):
        fields = super().get_token_fields(code)
        fields["grant_type"] = "authorization_code"
        return fields

    def get_user_by_token(self, token):
        url = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def map_user_to_dict(self, raw_user):
        user = dict(abstract_user)
        user["id"] = raw_user.get("sub")
        user["name"] = raw_user.get("name")
        user["email"] = raw_user.get("email")
        user["avatar"] = raw_user.get("picture")
        user["provider"] = "google"
        user["raw"] = raw_user
        return user
