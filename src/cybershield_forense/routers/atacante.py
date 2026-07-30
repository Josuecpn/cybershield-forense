from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from cybershield_forense.db.session import get_db
from cybershield_forense.models import Atacante
from cybershield_forense.schemas.atacante import AtacanteCreate, AtacanteResponse

# Mudamos o prefixo para isolar o domínio de atacantes
router = APIRouter(prefix="/api/v1/atacantes", tags=["Gestão de Atacantes"])

@router.get("", response_model=list[AtacanteResponse])
async def listar_atacantes(db: Session = Depends(get_db)):
    """Busca todos os atacantes registrados no banco de dados."""
    return db.query(Atacante).all()

@router.post("", response_model=AtacanteResponse, status_code=status.HTTP_201_CREATED)
async def criar_atacante(payload: AtacanteCreate, db: Session = Depends(get_db)):
    """Registra uma nova ameaça cibernética no banco de dados."""
    novo_atacante = Atacante(
        ip_origem=payload.ip_origem,
        pais=payload.pais,
        asn=payload.asn,
        reputacao_score=payload.reputacao_score
    )
    db.add(novo_atacante)
    db.commit()
    db.refresh(novo_atacante)
    return novo_atacante
