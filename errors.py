class AccountAlreadyExists(Exception):
    def __init__(self, username):
        self.username = username

class NotValidURL(Exception):
    def __init__(self, url):
        self.url = url
