from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class AtacanteCreate(BaseModel):
    """Contrato de Entrada: Dados necessários para registrar uma ameaça."""
    ip_origem: str = Field(..., description="Endereço IP do suspeito")
    pais: Optional[str] = "Desconhecido"
    asn: Optional[str] = "Desconhecido"
    reputacao_score: float = Field(0.0, ge=0.0, le=10.0, description="Score de risco de 0 a 10")

class AtacanteResponse(BaseModel):
    """Contrato de Saída: Dados retornados após o processamento."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    ip_origem: str
    pais: str
    asn: str
    reputacao_score: float
