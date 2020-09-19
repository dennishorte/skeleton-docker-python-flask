from flask_login import UserMixin


class User(object):
    def __init__(self, user_id):
        self.id = user_id

    @staticmethod
    def get(user_id):
        test_users = {
            'dennis': User('dennis'),
            'scottsh': User('scottsh'),
        }

    @staticmethod
    def validate_password(user_id, password_hash):
        password_map = {
            'dennis': '',
            'scottsh': '',
        }

        return password_map.get(user_id) == password_hash

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')    
