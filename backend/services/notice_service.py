from databases.database import session_scope
from models.model import *

# db select
def get_all_notice():
    with session_scope() as session:
        select_query = session.scalars(select(BOARD).order_by(BOARD.board_id)).all()
        board_posts = []

        for post in select_query:
            board_posts.append(dict(
                board_id=post.board_id,
                title=post.title,
                writer=post.writer,
                content=post.content,
            ))
    return board_posts

def get_notice(board_id):
    with session_scope() as session:
        select_query = session.scalars(select(BOARD).where(BOARD.board_id == board_id))
        board_posts = []

        for post in select_query:
            board_posts.append(dict(
                board_id=post.board_id,
                title=post.title,
                writer=post.writer,
                content=post.content,
            ))
    return board_posts

def insert_notice(board_id, title, writer, content):
    with session_scope() as session:
        print(f"id: {board_id}, title: {title}, writer: {writer}, content: {content}")
        new_notice = BOARD(board_id=board_id, title=title, writer=writer, content=content)
        session.add(new_notice)

def update_notice(board_id, title, writer, content):
    with session_scope() as session:
        print(f"id: {board_id}, title: {title}, writer: {writer}, content: {content}")
        notice = session.get(BOARD, board_id)
        notice.title = title
        notice.writer = writer
        notice.content = content

def delete_notice(board_id):
    with session_scope() as session:
        # session.query(BOARD).filter(BOARD.board_id == board_id).delete()
        session.delete(session.get(BOARD, board_id))
