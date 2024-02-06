class User:
    def __init__(self, name, role, username, password, email) -> None:
        self._name = name
        self._role = role
        self._username = username
        self._password = password
        self._email = email
        

class Staff(User):
    def __init__(self, name, role, username, password, email, title) -> None:
        super().__init__(name, role, username, password, email)
        self.title = title