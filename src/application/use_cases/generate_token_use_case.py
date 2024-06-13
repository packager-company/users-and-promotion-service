from src.domain.ports.users_port import UsersPort
from src.infrastructure.middlewares.functionJWT import write_token
import bcrypt


class GenerateTokenUseCase:
    def __init__(self, user_repository: UsersPort):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> str | None:
        user = self.user_repository.get_user_by_email(email)

        if not user:
            return None

        if not self.unhash_password(password, user.password):
            return None

        user_id = user.id

        payload = {"user_id": user_id}

        token = write_token(payload)

        return token

    def unhash_password(self, password: str, hashed_password: str) -> bool:
        user_bytes = password.encode("utf-8")
        is_valid = bcrypt.checkpw(user_bytes, hashed_password.encode("utf-8"))

        return is_valid
