from models.model import User

class UserRepository:
    def get_all_users(self):
        return User.query.all()

    def get_user(self, nickname):
        return User.query.filter_by(username=nickname).first()