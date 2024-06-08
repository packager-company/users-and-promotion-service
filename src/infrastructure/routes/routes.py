from flask import Blueprint, request

from src.infrastructure.controllers.users_controller import UsersController
from src.infrastructure.repositories.mysql_repository import UsersRepository

repository = UsersRepository()
controller = UsersController(repository)

users_routes = Blueprint('users', import_name=__name__)

@users_routes.route('/users', methods=['POST'])
def create_user():
  return controller.create_user(request)