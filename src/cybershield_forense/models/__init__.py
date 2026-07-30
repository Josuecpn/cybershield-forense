from cybershield_forense.db.base import Base
from cybershield_forense.models.atacante import Atacante
from cybershield_forense.models.incidente import Incidente

# Vincula o metadado centralizado
metadata = Base.metadata

__all__ = ["Base", "Atacante", "Incidente", "metadata"]