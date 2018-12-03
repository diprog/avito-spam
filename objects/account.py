from objects.proxy import Proxy
from objects import Object
class Account(Object):
    def __init__(self, json):
        super().__init__(json)
        self.username = json["username"]
        self.password = json["password"]
        self.proxy = Proxy(json["proxy"]) if json["proxy"] else None
