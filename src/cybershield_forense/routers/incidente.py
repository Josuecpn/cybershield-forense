from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from cybershield_forense.db.session import get_db
from cybershield_forense.models import Atacante, Incidente
from cybershield_forense.schemas.incidente import IncidenteCreate, IncidenteResponse

# Definimos o prefixo exclusivo para o domínio de incidentes telemáticos
router = APIRouter(prefix="/api/v1/incidentes", tags=["Gestão de Incidentes"])

@router.post("", response_model=IncidenteResponse, status_code=status.HTTP_201_CREATED)
async def criar_incidente(payload: IncidenteCreate, db: Session = Depends(get_db)):
    """Busca o IP do atacante e registra a tentativa de ataque no banco de dados real."""
    
    # 1. Triagem Forense: Busca se o IP enviado já está cadastrado na tabela de atacantes
    atacante = db.query(Atacante).filter(Atacante.ip_origem == payload.ip_origem).first()
    
    # Se o IP não foi triado previamente, a investigação não pode criar o vínculo
    if not atacante:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"IP de origem {payload.ip_origem} não encontrado. Cadastre o atacante primeiro."
        )

    # 2. Persistência Relacional: Cria o incidente injetando o ID real do atacante encontrado
    novo_incidente = Incidente(
        atacante_id=atacante.id,  # <-- Vínculo da chave estrangeira (ondelete=CASCADE)
        metodo_http=payload.metodo_http,
        url_requisitada=payload.url_requisitada,
        status_code=payload.status_code,
        payload_suspeito=payload.payload_suspeito,
        user_agent=payload.user_agent,
        tipo_ataque=payload.tipo_ataque
    )
    
    db.add(novo_incidente)
    db.commit()
    db.refresh(novo_incidente)
    
    return novo_incidente