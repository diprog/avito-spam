import constants
import errors
from objects.settings import Settings
import json as _json

#Чтоб не читать файл каждый раз при получении настройки.
global_settings = None
def init_json():
    empty_data = _json.dumps(constants.default_settings, indent=4, sort_keys=True)
    open(constants.settings_path, "w").write(empty_data)

def get():
    try:
        if (global_settings):
            return global_settings
        else:
            settings_raw = open(constants.settings_path, "r").read()
            global_settings = Settings(_json.loads(settings_raw))
            return global_settings
    except (FileNotFoundError, _json.decoder.JSONDecodeError):
        init_json()
        return []
