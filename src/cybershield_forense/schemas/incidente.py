from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class IncidenteCreate(BaseModel):
    """Contrato de Entrada: Dados enviados ao registrar uma tentativa de ataque."""
    ip_origem: str = Field(..., description="IP do atacante para realizarmos o vínculo")
    metodo_http: str = Field(..., max_length=10, description="Método utilizado (GET, POST, etc.)")
    url_requisitada: str = Field(..., description="Endpoint que sofreu a tentativa de invasão")
    status_code: int = Field(..., ge=100, le=599, description="Código de resposta HTTP do servidor")
    payload_suspeito: Optional[str] = Field(None, description="Injeção ou código malicioso detectado")
    user_agent: Optional[str] = Field(None, description="Identificação do navegador ou ferramenta do hacker")
    tipo_ataque: Optional[str] = Field("Varredura Genérica", description="Classificação técnica do ataque")

class IncidenteResponse(BaseModel):
    """Contrato de Saída: Dados retornados pela API após persistência."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    atacante_id: int
    timestamp: datetime
    metodo_http: str
    url_requisitada: str
    status_code: int
    payload_suspeito: Optional[str]
    user_agent: Optional[str]
    tipo_ataque: str