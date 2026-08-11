from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from cybershield_forense.routers.monitor import router as monitor_router
from cybershield_forense.routers.atacante import router as atacante_router
from cybershield_forense.routers.incidente import router as incidente_router
import cybershield_forense.models

app = FastAPI(
    title="CyberShield-Forense API",
    description="API de Triagem de Incidentes Cibernéticos e Inteligência Forense para a Polícia Federal.",
    version="1.0.0",
    docs_url=None,
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

DARK_THEME_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-themes@3.0.0/themes/3.x/theme-dark.css"

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_css_url=DARK_THEME_URL,
    )
