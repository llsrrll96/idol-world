from reposiories.comment_repository import CommentRepository

class CommentService:
    def __init__(self):
        self.comment_repository = CommentRepository()

    def get_all_comments(self):
        return self.comment_repository.get_all_comments()

    def add_comment(self, username, password, content, ip_address):
        self.comment_repository.add_comment(username,password,content,ip_address)
