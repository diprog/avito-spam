import constants
import errors
import json as _json

def init_json():
    empty_data = _json.dumps([], indent=4, sort_keys=True)
    open(constants.urls_path, "w").write(empty_data)

def get():
    try:
        urls_raw = open(constants.urls_path, "r").read()
        return _json.loads(urls_raw)
    except (FileNotFoundError, _json.decoder.JSONDecodeError):
        init_json()
        return []

def is_valid_url(url):
    if ((url.startswith("https://") or url.startswith("http://")) and "avito.ru" in url):
        return True
    return False

def add(url):
    if (is_valid_url(url)):
        urls = get()
        urls.append(url)
        data = _json.dumps(urls, indent=4, sort_keys=True)
        open(constants.urls_path, "w").write(data)
    else:
        raise errors.NotValidURL(url)
