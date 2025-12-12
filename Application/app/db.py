
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from app.config import DATABASE_URL


engine: Engine = create_engine(
    DATABASE_URL,
    future=True,
    pool_pre_ping=True,
)

def execute_query(sql: str, params: dict | None = None):
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        return result
