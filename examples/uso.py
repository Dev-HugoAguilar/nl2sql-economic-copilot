"""Ejemplo ejecutable de extremo a extremo del copiloto NL-to-SQL.

Uso::

    python examples/uso.py

Requiere el paquete instalado (``python -m pip install -e .``). Lee el snapshot
incluido en ``web/data.json``, ejecuta la consulta completa (parser léxico ->
plantilla SQL parametrizada -> lectura SQLite en ``mode=ro``) e imprime el
resultado. El índice SQLite se crea en un directorio temporal, así que el
repositorio no se modifica.
"""

from __future__ import annotations

import gc
import tempfile
from pathlib import Path

from app.config import Settings
from app.nl_sql.service import CopilotoNlSql

PREGUNTA = "¿En qué año fue mayor la inflación entre 2019 y 2025?"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        settings = Settings(nl_sql_db_path=str(Path(tmp) / "wdi.sqlite3"))
        copiloto = CopilotoNlSql(db=None, settings=settings)

        print(f"Snapshot: {copiloto.data.get('dataset_id')}")
        print(f"Observaciones cargadas: {len(copiloto.rows)}")
        print(f"Pregunta: {PREGUNTA}")

        salida = copiloto.consultar(PREGUNTA)

        print(f"Modo de intención: {salida['intent_mode']}")
        print(f"Operación: {salida['spec']['kind']}")
        print(f"Indicadores: {salida['spec']['indicator_codes']}")
        print(f"Parámetros SQL: {salida['parameters']}")
        print(f"Filas devueltas: {salida['row_count']}")
        primero = salida["rows"][0]
        print(f"Primer lugar del ranking: {primero['year']} · {primero['value']:,.4f} % anual")
        print(f"Resumen: {salida['summary']}")
        print(f"Auditoría: {salida['audit']}")

        # Comprobación explícita de lo que se acaba de imprimir.
        assert salida["spec"]["kind"] == "ranking", salida["spec"]
        assert salida["parameters"] == ["MEX", "FP.CPI.TOTL.ZG", 2019, 2025], salida["parameters"]
        assert salida["row_count"] == 7, salida["row_count"]
        assert primero["year"] == 2022, primero

        # En Windows el manejador SQLite se libera al destruir la instancia; se
        # hace explícito para poder borrar el directorio temporal.
        del copiloto
        gc.collect()

    print("OK · consulta de extremo a extremo verificada")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
