from sqlalchemy import Column, String, DateTime, func
from src.database.mysql import Base

class User(Base):
  __tablename__ = 'users'

  id = Column(String(36), primary_key=True, index=True)
  first_name = Column(String(255), nullable=False)
  last_name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  password = Column(String(255), nullable=False)
  cellphone = Column(String(255), nullable=True)
  registration_date = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
  def to_dict(self):
    return {
      'id': self.id,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'email': self.email,
      'password': self.password,
      'registration_date': self.registration_date
    }
