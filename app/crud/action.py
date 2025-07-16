from sqlalchemy.orm import Session
from app.models.action import Action
from app.schemas.action import ActionCreate

def create_action(db: Session, action: ActionCreate, user_id: int):
    db_action = Action(**action.dict(), user_id=user_id)
    db.add(db_action)
    db.commit()
    db.refresh(db_action)
    return db_action

def get_actions_by_user(db: Session, user_id: int):
    return db.query(Action).filter(Action.user_id == user_id).all()

def delete_action(db: Session, action_id: int, user_id: int):
    action = db.query(Action).filter(Action.id == action_id, Action.user_id == user_id).first()
    if action:
        db.delete(action)
        db.commit()
        return True
    return False
