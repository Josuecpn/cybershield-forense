from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from cybershield_forense.db.base import Base

class Incidente(Base):
    __tablename__ = "incidentes"

    id = Column(Integer, primary_key=True, index=True)
    # Estabelece o vínculo relacional com a tabela de atacantes
    atacante_id = Column(Integer, ForeignKey("atacantes.id", ondelete="CASCADE"), nullable=False)
    
    # Armazena o horário do ataque adotando a boa prática de fusos horários
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC), index=True)
    
    metodo_http = Column(String(10), nullable=False)
    url_requisitada = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    payload_suspeito = Column(Text, nullable=True)
    user_agent = Column(String, nullable=True)
    tipo_ataque = Column(String, default="Varredura Genérica")

    # Mapeia o relacionamento inverso (Muitos Incidentes pertencem a um Atacante)
    atacante = relationship("Atacante", back_populates="incidentes")