from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from cybershield_forense.db.session import get_db

router = APIRouter(prefix="/api/v1/monitor", tags=["Dashboard e Estatísticas"])