from flask import Blueprint

learnresource = Blueprint("learnresource", __name__)

from . import views