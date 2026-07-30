from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from cybershield_forense.db.base import Base

class Atacante(Base):
    __tablename__ = "atacantes"

    id = Column(Integer, primary_key=True, index=True)
    ip_origem = Column(String, unique=True, nullable=False, index=True)
    pais = Column(String, default="Desconhecido")
    asn = Column(String, default="Desconhecido")
    reputacao_score = Column(Float, default=0.0)

    incidentes = relationship("Incidente", back_populates="atacante", cascade="all, delete-orphan")