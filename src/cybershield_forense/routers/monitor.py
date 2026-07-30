from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/monitor", tags=["Monitoramento Forense"])

@router.get("/atacantes")
async def listar_atacantes_estatico():
    """Retorna um array vazio apenas para fazer o primeiro teste passar (TDD Green)."""
    return []
