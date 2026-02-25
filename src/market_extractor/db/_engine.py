import os
from sqlalchemy import Engine, create_engine, text
from dotenv import load_dotenv

load_dotenv()

def make_engine():
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME", "marketdb")
    user = os.getenv("DB_USER", "market")
    pwd  = os.getenv("DB_PASSWORD", "market")

    url = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{name}"
    return create_engine(url, pool_pre_ping=True)

def health_check(engine: Engine):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT schemaname || '.' || tablename AS table_name
                FROM pg_tables
                WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
                ORDER BY schemaname, tablename
            """)
        )
        return [row[0] for row in result]