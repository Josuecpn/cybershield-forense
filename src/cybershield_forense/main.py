from fastapi import FastAPI
from cybershield_forense.routers.monitor import router as monitor_router

app = FastAPI(
    title="CyberShield-Forense API",
    description="API de Triagem de Incidentes Cibernéticos e Inteligência Forense para a Polícia Federal.",
    version="1.0.0"
)

app.include_router(monitor_router)

@app.get("/", tags=["Root"])
async def root():
    return {
        "status": "Operacional",
        "sistema": "CyberShield-Forense"
    }
