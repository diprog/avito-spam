accounts_path = "data/accounts.json"
urls_path = "data/urls.json"
settings_path = "data/settings.json"

default_settings = {
    #Сколько объявлений обрабатывать
    "limit":1,
    #Фильтр по объявлениям, размещённых между какими-то датами
    "date_filter":False,
    "date_from":None,
    "date_to":None,
    #Пауза после каждого отправленного сообщения
    "pause_secs":5,
    #Сколько можно отправлять сообщений с одного аккаунта
    "messages_per_account":25,
    #Сколько нужно ждать после смены аккаунта
    "pause_account_switch_secs":10
}
