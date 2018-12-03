from objects import Object

class Auth(Object):
    def __init__(self, json):
        super().__init__(json)
        self.username = json["username"]
        self.password = json["password"]

class Proxy(Object):
    def __init__(self, json):
        super().__init__(json)
        self.type = json["type"]
        self.ip = json["ip"]
        self.auth = Auth(json["auth"]) if json["auth"] else None
        self.port = json["port"]
