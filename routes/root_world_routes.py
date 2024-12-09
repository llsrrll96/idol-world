import json
import logging
from flask import Blueprint, render_template, jsonify, Response, request, session

from services.world_service import WorldService
from services.comment_service import CommentService

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

world_bp = Blueprint('world', __name__)
comment_bp = Blueprint('comment', __name__)

world_service = WorldService()
comment_service = CommentService()

@world_bp.route("/")
def index():
    return render_template('index.html')

@world_bp.route('/home')
def home():
    user_role = session.get('user_role')
    logger.info(f'user_role: {user_role}')
    comments = comment_service.get_all_comments()
    logger.info(f'comments: {comments}')
    return render_template('home.html', user_role=user_role, comments=comments)  # iframe으로 로드할 페이지

@world_bp.route("/getDbData")
def getDbData():
    users = world_service.get_all_data()
    user_list = [user.to_dict() for user in users]
    json_data = json.dumps(user_list, ensure_ascii=False)
    return Response(json_data, mimetype='application/json')

@world_bp.route("/login")
def login():
    return render_template('login.html')

@world_bp.route("/signin", methods=['POST'])
def signin():
    data = request.get_json()  # JSON 데이터 가져오기
    nickname = data.get('nickname')
    password = data.get('password')

    role = world_service.signin(nickname, password)
    logger.info("role: "+ role)
    # 성공시 세션에 넣기
    session['user_role'] = role

    return jsonify({'status': 'success'}), 200


############################

comments = []

@comment_bp.route('/submit-comment', methods=['POST'])
def submit_comment():
    data = request.get_json()  # JSON 데이터 가져오기
    comment = data.get('comment')
    nickname = data.get('nickname')
    password = data.get('password')
    ip_address = request.remote_addr

    logger.info("m-submit_comment")
    logger.info(data)
    logger.info(ip_address)

    comment_service.add_comment(username=nickname, password=password, content=comment, ip_address=ip_address)

    if comment:
        # 댓글을 리스트에 추가
        comments.append(comment)

        logger.info(f'comment: {comment}, nickname: {nickname}, password: {password}')
        return jsonify({'status': 'success', 'comment': comment, 'nickname': nickname}), 201
    else:
        logger.error('Comment submission failed: No comment provided.')
        return jsonify({'status': 'error', 'message': '댓글이 필요합니다.'}), 400
