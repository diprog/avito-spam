import constants
import errors
from objects.account import Account
import json as _json

def init_json():
    empty_data = _json.dumps([], indent=4, sort_keys=True)
    open(constants.accounts_path, "w").write(empty_data)

def get():
    try:
        accounts_raw = open(constants.accounts_path, "r").read()
        accounts = []
        for account in _json.loads(accounts_raw):
            accounts.append(Account(account))
        return accounts
    except (FileNotFoundError, _json.decoder.JSONDecodeError):
        init_json()
        return []

def exists(accounts, username):
    for account in accounts:
        if (account.username == username):
            return True
    return False

def add(username, password, proxy=None):
    accounts = get()
    if (exists(accounts, username)):
        raise errors.AccountAlreadyExists(username)
    else:
        account = {"username":username, "password":password, "proxy":proxy}
        accounts.append(account)
        data = _json.dumps(accounts, indent=4, sort_keys=True)
        open(constants.accounts_path, "w").write(data)
