"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Provider, Branch, Assets, UserMB, Migration
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.order_by(User.id.asc()).all()
    if not users:
        return jsonify({"error": "Users not found"}), 404
    users_data = [user.serialize() for user in users]
    return jsonify({"users": users_data}), 200
