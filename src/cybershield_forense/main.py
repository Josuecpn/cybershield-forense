from fastapi import FastAPI
from cybershield_forense.routers.monitor import router as monitor_router
from cybershield_forense.routers.atacante import router as atacante_router
from cybershield_forense.routers.incidente import router as incidente_router
import cybershield_forense.models

app = FastAPI(
    title="CyberShield-Forense API",
    description="API de Triagem de Incidentes Cibernéticos e Inteligência Forense para a Polícia Federal.",
    version="1.0.0"
)

app.include_router(atacante_router)
app.include_router(incidente_router)
app.include_router(monitor_router)

@app.get("/", tags=["Root"])
async def root():
    return {
        "status": "Operacional",
        "sistema": "CyberShield-Forense"
    }
