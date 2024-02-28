from flask import Blueprint, jsonify,request
from ..Model.User_model import UserSchema
from ..DB.Db_config import collection
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.json
        user_schema = UserSchema()
        result = user_schema.load(user_data)
        inserted_user = collection.insert_one(result).inserted_id
        return jsonify({'status': 'success', 'message': 'User added successfully', 'user_id': str(inserted_user)})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Route to get all users
@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = list(collection.find({}, {'_id': False}))
    return jsonify(users)

# Route to get a specific user by user_id
@user_bp.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({'_id': user_id}, {'_id': False})
    if user:
        return jsonify(user)
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

# Route to update a user by user_id
@user_bp.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.json
        user_schema = UserSchema()
        updated_user = collection.find_one_and_update(
            {'_id': user_id},
            {'$set': user_schema.load(user_data)},
            return_document=True
        )
        if updated_user:
            return jsonify({'status': 'success', 'message': 'User updated successfully', 'user': updated_user})
        else:
            return jsonify({'status': 'error', 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Route to delete a user by user_id
@user_bp.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = collection.delete_one({'_id': user_id})
    if result.deleted_count > 0:
        return jsonify({'status': 'success', 'message': 'User deleted successfully'})
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404
