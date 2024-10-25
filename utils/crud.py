from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import AdminLog

DATABASE_PATH = 'sqlite:///C:/Users/curseddd/space-station-14/bin/Content.Server/data/preferences.db'
engine = create_engine(DATABASE_PATH)
Session = sessionmaker(bind=engine)

def get_user_messages():
    session = Session()
    result = session.query(AdminLog).filter(
        AdminLog.type == 61,
        (AdminLog.message.like('%say from%') | AdminLog.message.like('%whisper%'))
    ).all()
    session.close()
    return result
