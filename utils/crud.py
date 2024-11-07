from sqlalchemy import select
from .models import AdminLog
from utils.db_alchemy import get_db


def get_user_messages() -> list[AdminLog]:
    db = next(get_db())
    statement = select(AdminLog).where(
        AdminLog.type == 61,
        (AdminLog.message.like('%say from%') | AdminLog.message.like('%whisper from%'))
    )
    result = db.scalars(statement).all()
    return result
