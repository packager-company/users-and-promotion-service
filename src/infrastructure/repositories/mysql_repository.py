from src.database.mysql import Base, engine, session_local
from src.database.models.user import User as UserModel
from src.domain.entities.user import User
from src.domain.ports.users_port import UsersPort

class UsersRepository(UsersPort):
  def __init__(self):
    Base.metadata.create_all(bind=engine)
    self.db = session_local()
  
  def create_user(self, user: User):
    user_model = UserModel(**user.to_dict())
    self.db.add(user_model)
    self.db.commit()
    self.db.refresh(user_model)
    return user_model.to_dict()