
from ..user import user
from victoria.models.models import User

from sqlalchemy import inspect


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@user.route('/all')
def user_all():
    result = User.query.all()

    return {
        'data': [object_as_dict(r) for r in result]
    }