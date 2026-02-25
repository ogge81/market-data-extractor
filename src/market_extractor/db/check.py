import re

from sqlalchemy import text
from .engine import make_engine


def get_tables() -> list[str]:
    """Return a list of current tables (schema-qualified)."""
    engine = make_engine()
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

def get_table_columns(table_name: str) -> list[str]:
    """Return a list of columns for a given table."""
    engine = make_engine()
    with engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        )
        return [row[0] for row in result]

def get_table(table_name: str) -> list[dict]:
    """Return all rows from a table (e.g. core.market) as a list of dicts."""
    table_name = table_name.strip().lower()
    if not re.match(r"^[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*$", table_name):
        raise ValueError(f"Invalid table name: {table_name!r}")

    engine = make_engine()
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        return [dict(row._mapping) for row in result]

def delete_table(table_name: str) -> None:
    """Delete a given table."""
    engine = make_engine()
    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
        conn.commit()
