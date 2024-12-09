from extensions import db

class User(db.Model):
    __tablename__ = 'WAY_ADMIN_USER'  # 명시적으로 테이블 이름 설정

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(10))

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }


class Comment(db.Model):
    __tablename__ = 'WAY_COMMENTS'  # 명시적으로 테이블 이름 설정

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)  # 사용자 이름
    password = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text, nullable=False)  # 댓글 내용
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())  # 생성 시간
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  # 수정 시간
    ip_address = db.Column(db.String(45))  # IP 주소

    def __repr__(self):
        return f'<Comment {self.id} by {self.username}>'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'ip_address': self.ip_address
        }