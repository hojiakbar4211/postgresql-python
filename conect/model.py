class User:
    def __init__(self, username: str,
                 password: str,
                 email: str,
                 phone_number: str,
                 _id: int = None) -> None:
        self._id = _id
        self.username = username
        self.password = password
        self.email = email
        self.phone_number = phone_number
