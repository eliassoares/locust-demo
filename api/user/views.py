from flask import jsonify

from api.models.user import User
from api.user import user


@user.route('/user')
def get_all_users():
    all_users = User.query.all()
    all_users = [{'id': u.id, 'name': u.name} for u in all_users]

    return jsonify(all_users)
