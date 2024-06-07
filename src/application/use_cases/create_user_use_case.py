from src.domain.ports.users_port import UsersPort, User

class CreateUserUseCase:
  def __init__(self, users_port: UsersPort):
    self.users_port = users_port

  def execute(self, data):
    return self.users_port.create_user(User(**data))