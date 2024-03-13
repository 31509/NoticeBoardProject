from databases.database import session_scope
from models.model import *

class EventService:
    def get_events(self):
        with session_scope() as session:
            query = session.query(BOARD)
            board_posts = []

            for post in query:
                board_posts.append(dict(
                    board_id=post.board_id,
                    title=post.title,
                    writer=post.writer,
                    content=post.content,
                    regdate=post.regdate,
                ))
        return board_posts