"""Paquete de dominio del copiloto NL-to-SQL.

Repositorio autónomo: el copiloto funciona con el snapshot incluido y sqlite3 de
la biblioteca estándar. Atlas (auditoría) y un proveedor de modelos son
opcionales y están apagados por omisión.
"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

#: Raíz del repositorio (``src/app/config.py`` → tres niveles arriba).
REPO_ROOT = Path(__file__).resolve().parents[2]
#: Aplicación estática incluida en el repositorio.
WEB_APP = REPO_ROOT / "web"
#: Documentación y material de apoyo.
DOCS_DIR = REPO_ROOT / "docs"


class Settings(BaseSettings):
    """Ajustes del copiloto.

    Todos los campos tienen un valor por omisión válido para un clon limpio. La
    base SQLite se crea en un archivo temporal dentro del repositorio de trabajo
    y se abre en modo de solo lectura para las consultas.
    """

    model_config = SettingsConfigDict(
        env_file=None,
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    #: Snapshot WDI que se carga en la base SQLite.
    nl_sql_data_path: str = str(WEB_APP / "data.json")
    #: Ubicación del archivo SQLite derivado. Se abre en modo lectura.
    nl_sql_db_path: str = str(REPO_ROOT / "tmp" / "wdi.sqlite3")
    #: Auditoría opcional en MongoDB. Apagada por omisión.
    nl_sql_audit_enabled: bool = False
    nl_sql_audit_db: str = "portfolio_demos"
    nl_sql_audit_collection: str = "nl_sql_query_audit"
    #: URI usada solo para derivar la etiqueta ``local`` / ``atlas``.
    mongodb_uri: str = "mongodb://127.0.0.1:27017/portfolio_demos"
    #: Proveedor de modelos opcional. Sin las tres variables, el parser local
    #: resuelve la pregunta con reglas y plantillas.
    llm_base_url: str | None = None
    llm_api_key: str | None = None
    llm_model: str | None = None
