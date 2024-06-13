from src.domain.ports.users_port import UsersPort
from src.application.use_cases.create_user_use_case import CreateUserUseCase
from src.application.use_cases.generate_token_use_case import GenerateTokenUseCase

class UsersController:
  def __init__(self, users_port: UsersPort):
    self.users_port = users_port
    self.create_user_use_case = CreateUserUseCase(users_port)
    self.generate_token_use_case = GenerateTokenUseCase(users_port)

  def create_user(self, data: dict):
    return self.create_user_use_case.execute(data.get('first_name'), data.get('last_name'), data.get('email'), data.get('password'), data.get('cellphone'))


  def generate_token(self, data: dict):
    return self.generate_token_use_case.execute(data.get('email'), data.get('password'))