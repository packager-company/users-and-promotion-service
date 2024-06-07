from src.domain.ports.users_port import UsersPort
from src.application.use_cases.create_user_use_case import CreateUserUseCase

class UsersController:
  def __init__(self, users_port: UsersPort):
    self.users_port = users_port
    self.create_user_use_case = CreateUserUseCase(users_port)

  def create_user(self, request):
    return self.create_user_use_case.execute(request.get_json())