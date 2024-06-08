from abc import ABC, abstractmethod
from src.users.domain.entities.user import User

class UsersPort(ABC):
  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def create_user(self, user: User) -> User:
    pass