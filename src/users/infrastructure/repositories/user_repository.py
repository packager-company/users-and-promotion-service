from src.users.infrastructure.database.mysql import Base, engine, session_local
from src.users.infrastructure.database.models.user import User as UserModel
from src.users.domain.entities.user import User
from src.users.domain.ports.users_port import UsersPort

class UsersRepository(UsersPort):
  def __init__(self):
    Base.metadata.create_all(bind=engine)
    self.db = session_local()

  def create_user(self, user: User) -> User:
    user_model = UserModel(**user.to_dict())
    self.db.add(user_model)
    self.db.commit()
    self.db.refresh(user_model)
    return user_model

  def get_user_by_email(self, email: str) -> User | None:
    user = self.db.query(UserModel).filter(UserModel.email == email).first()
    return user