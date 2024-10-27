from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import AdminLog
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

DATABASE_PATH = os.getenv("DATABASE_PATH")

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
