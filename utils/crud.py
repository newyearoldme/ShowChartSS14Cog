from sqlalchemy.orm import Session

from .models import AdminLog
from .db_alchemy import get_db

# CREATE
def create_log(log_data):
    db = next(get_db())
    new_log = AdminLog(**log_data)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

# READ
def get_user_messages():
    db = next(get_db())
    result = db.query(AdminLog).filter(
        AdminLog.type == 61,
        (AdminLog.message.like('%say from%') | AdminLog.message.like('%whisper from%'))
    ).all()
    if not result:
        return None
    return result

# UPDATE
def update_log(log_id, updated_data):
    db = next(get_db())
    log_entry = db.query(AdminLog).get(log_id)
    if log_entry:
        for key, value in updated_data.items():
            setattr(log_entry, key, value)
        db.commit()
        db.refresh(log_entry)
    return log_entry

# DELETE
def delete_log(log_id):
    db = next(get_db())
    log_entry = db.query(AdminLog).get(log_id)
    if log_entry:
        db.delete(log_entry)
        db.commit()
