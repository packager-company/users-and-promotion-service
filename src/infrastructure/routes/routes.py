from flask import Blueprint, request

from src.infrastructure.controllers.users_controller import UsersController
from src.infrastructure.repositories.mysql_repository import UsersRepository

repository = UsersRepository()
controller = UsersController(repository)

users_routes = Blueprint('users', import_name=__name__)

@users_routes.route('/', methods=['POST'])
def create_user():
  data = request.get_json()
  data_request = {
    'first_name': data['first_name'],
    'last_name': data['last_name'],
    'email': data['email'],
    'password': data['password'],
    'cellphone': data['cellphone'],
  }
  user = controller.create_user(data_request)

  return user.to_dict(), 201


@users_routes.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  data_request = {
    'email': data['email'],
    'password': data['password'],
  }
  token = controller.generate_token(data_request)

  if not token:
    return {'message': 'Invalid credentials'}, 401

  return {'token': token}, 200