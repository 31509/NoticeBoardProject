from databases.database import session_scope
from models.model import *

# db select
def get_all_user():
    with session_scope() as session:
        select_query = session.scalars(select(USER).order_by(USER.user_id)).all()
        user_posts = []

        for post in select_query:
            user_posts.append(dict(
                user_id=post.user_id,
                password=post.password,
                username=post.username,
            ))
    return user_posts

def get_user(user_id):
    with session_scope() as session:
        select_query = session.scalars(select(USER).where(USER.user_id == user_id))
        user_posts = []

        for post in select_query:
            user_posts.append(dict(
                user_id=post.user_id,
                password=post.password,
                username=post.username,
            ))
    return user_posts

def insert_user(user_id, password, username):
    with session_scope() as session:
        print(f"user_id: {user_id}, password: {password}, username: {username}")
        new_notice = USER(user_id=user_id, password=password, username=username)
        session.add(new_notice)

def update_user(user_id, password, username):
    with session_scope() as session:
        print(f"user_id: {user_id}, password: {password}, username: {username}")
        user = session.get(USER, user_id)
        user.password = password
        user.username = username

def delete_user(user_id):
    with session_scope() as session:
        # session.query(USER).filter(USER.user_id == user_id).delete()
        session.delete(session.get(USER, user_id))

def login123(user_id):
    with session_scope() as session:
        user = session.get(USER, user_id)
        return user.user_id