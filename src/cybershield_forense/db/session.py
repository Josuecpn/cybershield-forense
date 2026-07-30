from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./cybershield.db"

# Configura o motor de conexão desativando a checagem de threads para o SQLite funcionar com o FastAPI
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Gera uma sessão de banco de dados para cada requisição da API."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
