from sqlalchemy.orm import Session
from app.db import models
from app.schemas.ledger import LedgerBase

def create_ledger(db: Session, ledger: LedgerBase, user_id: int):
    new_entry = models.Ledger(**ledger.dict(), user_id=user_id)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_ledgers(db: Session, user_id: int):
    return db.query(models.Ledger).filter(models.Ledger.user_id == user_id).all()
