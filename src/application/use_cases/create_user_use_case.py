from src.domain.ports.users_port import UsersPort, User
import bcrypt


class CreateUserUseCase:
    def __init__(self, users_port: UsersPort):
        self.users_port = users_port

    def execute(self, first_name, last_name, email, password, cellphone):
        hashed_password = self.hash_password(password)
        user = User(first_name, last_name, email, hashed_password, cellphone)

        return self.users_port.create_user(user)

    def hash_password(self, password: str) -> str:
        bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(bytes, salt)

        return hashed.decode("utf-8")
