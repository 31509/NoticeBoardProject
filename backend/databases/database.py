from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = None
Session = None

def get_session():
    return Session()

def init_db(config):
    db_info = config.get('database')
    engine = create_engine(f"oracle://{db_info.get('id')}:{db_info.get('password')}@{db_info.get('host')}:{db_info.get('port')}/{db_info.get('sid')}", echo=False)
    global Session
    Session = sessionmaker(bind=engine)
    # session = Session()

@contextmanager
def session_scope():
    session = get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()