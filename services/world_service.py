from reposiories.user_repository import UserRepository

class WorldService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_data(self):
        return self.user_repository.get_all_users()

    # 로그인 디비랑 비교
    def signin(self, nickname, password):
        db_user_pass = self.user_repository.get_user(nickname)
        user = db_user_pass.to_dict()
        role = ''
        if (password == user['password']) :
            return user['role']
        return role