from objects import Object
import settings
class Settings(Object):
    def __init__(self, json):
        super().__init__(json)
        self.date_filter = json["date_filter"]
        self.date_from = json["date_from"]
        self.date_to = json["date_to"]
        self.limit = json["limit"]
        self.messages_per_account = json["messages_per_account"]
        self.pause_account_switch_secs = json["pause_account_switch_secs"]
        self.pause_secs = json["pause_secs"]
