from src.users.domain.ports.users_port import UsersPort, User
import bcrypt

class CreateUserUseCase:
  def __init__(self, users_port: UsersPort):
    self.users_port = users_port

  def execute(self, first_name, last_name, email, password, cellphone):
    user = User(first_name, last_name, email, self.encrypt_password(password), cellphone)

    return self.users_port.create_user(user)
  
  def encrypt_password(self, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8') 