from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.ledger import LedgerBase, LedgerDisplay
from app.auth.auth import get_current_user, get_db
from app.crud import ledger
from app.db import models
from typing import List

router = APIRouter(prefix="/ledger", tags=["Ledger"])

@router.post("/", response_model=LedgerDisplay)
def create_entry(entry: LedgerBase, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return ledger.create_ledger(db, entry, user.id)

@router.get("/", response_model=List[LedgerDisplay])
def list_entries(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return ledger.get_ledgers(db, user.id)
