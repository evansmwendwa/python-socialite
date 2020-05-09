# python-socialite
<p align="center">

<a href="https://pypi.python.org/pypi/python_socialite">
<img src="https://img.shields.io/pypi/v/python_socialite.svg" /></a>
<a href="https://travis-ci.org/evansmwendwa/python_socialite"><img src="https://travis-ci.org/evansmwendwa/python_socialite.svg?branch=master" /></a>
</p>
Simple and convenient oAuth Login user provider for Facebook, Twitter, LinkedIn, Google, GitHub, GitLab and Bitbucket. Inspired by [Laravel Socialite](https://laravel.com/docs/master/socialite)

## Features
-   Supports multiple common providers
-   Supports any oAuth 2 compliant providers
-   Straighforward unopinionated authentication
-   Can be implemented in any python framework

# Usage

## Generate redirect url
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

## Retrieving Access Token and User

```python
code = "" # read code from GET variables
provider = AuthProvider("google", config)

try:
    access_token = provider.get_access_token(code)
    user = provider.get_user(access_token)
except:
    pass
```

Hook the returned user profile to your apps authentication.

## User Template

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

### Config Options

The config must be a dict containing keys of any of the supported providers

```python
# each provider config must have at least the following three options
options = {
    "client_id": "",
    "client_secret": "",
    "redirect_uri": ""
}

config = {
    "google": {
        "client_id": "",
        "client_secret": "",
        "redirect_uri": ""
    },
    "facebook": {},
    "twitter": {},
    "linkedin": {},
    "github": {},
    "gitlab": {},
    "bitbucket": {}
}

```
