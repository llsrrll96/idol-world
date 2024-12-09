from models.model import Comment  # Comment 모델 임포트

from extensions import db

class CommentRepository:
    def add_comment(self, username, password, content, ip_address):
        new_comment = Comment(
            username=username,
            password=password,
            content=content,
            ip_address=ip_address
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    def get_all_comments(self):
        return Comment.query.all()