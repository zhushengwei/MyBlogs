from flask import Blueprint

self = Blueprint("self", __name__)

from . import views