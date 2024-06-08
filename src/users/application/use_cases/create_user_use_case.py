from src.users.domain.ports.users_port import UsersPort, User

class CreateUserUseCase:
  def __init__(self, users_port: UsersPort):
    self.users_port = users_port

  def execute(self, first_name, last_name, email, hashed_password, cellphone):
    user = User(first_name, last_name, email, hashed_password, cellphone)

    return self.users_port.create_user(user)