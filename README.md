# python-socialite
<p align="center">

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/277f72118617436291eced30bac036a8)](https://www.codacy.com/manual/evans.mwendwa/python-socialite?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=evansmwendwa/python-socialite&amp;utm_campaign=Badge_Grade)
<a href="https://pypi.python.org/pypi/python_socialite">
<img src="https://img.shields.io/pypi/v/python_socialite.svg" /></a>
<a href=""><img src="https://github.com/evansmwendwa/python-socialite/workflows/build/badge.svg" /></a> [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/277f72118617436291eced30bac036a8)](https://www.codacy.com/manual/evans.mwendwa/python-socialite?utm_source=github.com&utm_medium=referral&utm_content=evansmwendwa/python-socialite&utm_campaign=Badge_Coverage)

</p>

Simple and convenient oAuth Login user provider for Facebook, Twitter, LinkedIn, Google, GitHub, GitLab and Bitbucket. Inspired by [Laravel Socialite](https://laravel.com/docs/master/socialite)

## Features
-   Supports multiple common providers
-   Supports any oAuth 2 compliant providers
-   Straighforward unopinionated authentication
-   Can be implemented in any python framework

## Usage

### Generate redirect uri
```python
from python_socialite import AuthProvider

config = {
    "google": {
        "client_id": "",
        "client_secret": "",
        "redirect_uri": ""
    }
}
provider = AuthProvider("google", config)
redirect_url = provider.get_auth_url()

# redirect user to the redirect_url using your frameworks supported redirect
```

### Retrieving Access Token and User

```python
code = "" # read code from GET variables
provider = AuthProvider("google", config)

try:
    token = provider.get_token(code)
    user = provider.get_user(token["access_token"])
except:
    pass
```

Hook the returned user profile to your apps authentication.

### Token Template

**NB:** Token attributes might vary between providers. Here's a sample returned by Google

```json
{
   "access_token":"ya29.***",
   "expires_in":3599,
   "scope":"https://www.googleapis.com/auth/userinfo.profile openid",
   "token_type":"Bearer",
   "id_token":"***jwt***"
}
```

### User Template

```python
user = {
    "id": "",
    "name": "",
    "email": "",
    "avatar": "",
    "raw": "",
    "provider": ""
}
```

The `raw` attribute contains all user data as returned by the oAuth provider. Fields in this attribute can be different across different oAuth providers

### Requesting Scopes

By default the following scopes are requested

```shell
openid, email, profile
```

You can override requested scopes by adding them to the provider config or using `set_scopes` method

```python
provider = OAuthProvider("google", config)
auth_url = provider.set_scopes(["openid", "email", "profile"]).get_auth_url()
```
**NB:** *If no scopes are set in the config or in code the default scopes will be used*

### Config Options

The config must be a dict containing keys of any of the supported providers

```python
# each provider key must have client_id, client_secret and redirect_url

config = {
    "google": {
        "client_id": "",
        "client_secret": "",
        "redirect_url": "",
        "scopes": [] # optional
    },
    "facebook": {},
    "twitter": {},
    "linkedin": {},
    "github": {},
    "gitlab": {},
    "bitbucket": {}
}

```
