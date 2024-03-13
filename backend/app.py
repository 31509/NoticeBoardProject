import yaml
from databases.database import init_db
from flask import Flask, request, jsonify, render_template, session, url_for, redirect
from services.notice_service import get_all_notice, get_notice, insert_notice, update_notice, delete_notice
from services.user_service import get_all_user, get_user, insert_user, update_user, delete_user, login123
from common import convert_to_json
from flask_cors import CORS

app = Flask (__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
app.secret_key = "My_Key"

config = None
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

init_db(config)

@app.route('/')
def root():
    print(session)
    return 'welcome to flask'

# notice
@app.route('/notices', methods=['GET'])
def get_notices():
    result = get_all_notice()
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/notice/<board_id>', methods=['GET'])
def notice(board_id):
    result = get_notice(board_id)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/notice', methods=['POST'])
def noticeAdd():
    params = request.get_json()
    board_id = params['board_id']
    title = params['title']
    writer = params['writer']
    content = params['content']
    result = insert_notice(board_id, title, writer, content)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/notice', methods=['PUT'])
def noticeUpdate():
    params = request.get_json()
    board_id = params['board_id']
    title = params['title']
    writer = params['writer']
    content = params['content']
    result = update_notice(board_id, title, writer, content)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/notice/<id>', methods=['DELETE'])
def noticeDel(board_id):
    result = delete_notice(board_id)
    rtn_obj = convert_to_json(result)
    return rtn_obj

# user
@app.route('/users', methods=['GET'])
def get_users():
    result = get_all_user()
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/user/<user_id>', methods=['GET'])
def user(user_id):
    result = get_user(user_id)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/user', methods=['POST'])
def userAdd():
    params = request.get_json()
    user_id = params['user_id']
    password = params['password']
    username = params['username']
    result = insert_user(user_id, password, username)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/user', methods=['PUT'])
def userUpdate():
    params = request.get_json()
    user_id = params['user_id']
    password = params['password']
    username = params['username']
    result = update_user(user_id, password, username)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/user/<user_id>', methods=['DELETE'])
def userDel(user_id):
    result = delete_user(user_id)
    rtn_obj = convert_to_json(result)
    return rtn_obj

@app.route('/login', methods=('GET', 'POST'))
def login():
    params = request.get_json()
    user_id = params['user_id']
    if request.method == 'POST':
        session.permanent = True
        session['user_id'] = login123(user_id)
        print(session)
        return params

@app.route('/logout')
def logout():
    print(session)
    session.clear()
    print(session)
    return 'logout'

@app.route('/getcookie/<key>', methods=['POST'])
def get_cookie(key):
    res = request.cookies.get(key)
    return res

if __name__ == "__main__":
    app.run()