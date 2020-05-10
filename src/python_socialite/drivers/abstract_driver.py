import requests
from abc import ABCMeta, abstractmethod
from urllib import parse


class AbstractDriver(metaclass=ABCMeta):
    def __init__(self, config):
        """Initialize default attributes."""
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.redirect_url = config.get("redirect_url")
        self.config = config
        self.scope_separator = " "

    @abstractmethod
    def get_auth_url(self):
        raise NotImplementedError

    @abstractmethod
    def get_token_url(self):
        raise NotImplementedError

    def set_scopes(self, scopes):
        self.scopes = scopes

    def build_scope(self):
        delimeter = self.scope_separator
        return delimeter.join(self.scopes)

    def get_code_fields(self, state=None):
        fields = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_url,
            "scope": self.build_scope(),
            "response_type": "code",
            "response_mode": "query",
        }

        if state is not None:
            fields["state"] = state

        return fields

    def get_token_fields(self, code):
        fields = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_url,
            "code": code,
        }

        return fields

    def build_url(self, url, state=None):
        fields = self.get_code_fields(state)
        parts = list(parse.urlparse(url))
        query = dict(parse.parse_qsl(parts[4]))
        query.update(fields)
        parts[4] = parse.urlencode(query, quote_via=parse.quote)

        return parse.urlunparse(parts)

    def get_token(self, code):
        url = self.get_token_url()
        data = self.get_token_fields(code)
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    @abstractmethod
    def get_user_by_token(self, access_token):
        raise NotImplementedError

    @abstractmethod
    def map_user_to_dict(self, raw_user):
        raise NotImplementedError

    def get_user(self, access_token):
        raw_user = self.get_user_by_token(access_token)
        user = self.map_user_to_dict(raw_user)
        return user
