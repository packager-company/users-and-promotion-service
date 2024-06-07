import uuid

class User:
  def __init__(self, first_name: str, last_name: str, email: str, password: str, registration_date: str = None):
    self.id = uuid.uuid4()
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.registration_date = registration_date

  def to_dict(self):
    return {
      'id': self.id,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'email': self.email,
      'password': self.password,
      'registration_date': self.registration_date
    }