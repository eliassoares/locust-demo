from flask import jsonify

from api.models.access import Access
from api.access import access


@access.route('/access')
def get_all_access():
    all_access = Access.query.all()
    all_access = [{
        'id': a.id, 'path': a.path
    } for a in all_access]

    return jsonify(all_access)
