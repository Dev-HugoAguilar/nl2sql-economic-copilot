# Arquitectura, validaciones y contrato

## Capas

```text
┌───────────────────────────────────────────────┐
│ web/  aplicación estática                     │
│  · consulta, SQL mostrado, tabla y resumen    │
└───────────────────┬───────────────────────────┘
                    │ mismo contrato
┌───────────────────▼───────────────────────────┐
│ src/app/nl_sql/service.py                     │
│  · parser local / plan del modelo validado    │
│  · plantilla SQL con parámetros               │
│  · SQLite en modo solo lectura                │
│  · auditoría opcional sin la pregunta         │
└───────────────────┬───────────────────────────┘
                    │ opcional
┌───────────────────▼───────────────────────────┐
│ portfolio-api  (repositorio aparte)           │
└───────────────────────────────────────────────┘
```

## Flujo de una consulta

1. **Carga** — el snapshot se valida y se materializa en SQLite (`observations`),
   con índice por indicador y año. La base derivada se abre después en modo
   lectura para las consultas.
2. **Interpretación** — si hay proveedor configurado se pide un plan JSON; se
   valida y, si falla, se descarta sin ruido. En paralelo o en su defecto, el
   parser local léxico resuelve país, indicadores, años y operación.
3. **Construcción** — el plan se traduce a una plantilla SQL con marcadores `?`.
   Los valores viajan como parámetros; el texto de la pregunta no entra en la
   consulta.
4. **Ejecución** — `ejecutar_lectura()` rechaza cualquier sentencia que no empiece
   por `SELECT` y devuelve filas con conteo y parámetros.
5. **Resumen** — una plantilla redacta el resultado con los mismos datos
   devueltos; no hay generación libre en el camino local.
6. **Auditoría** — opcional; registra indicadores, modo, conteo y destino, sin el
   texto de la pregunta.

## Validaciones del plan

| Regla | Efecto si se viola |
|---|---|
| País debe ser `MEX` | `QuestionError("solo cubre México")` |
| Años dentro de 2019–2025 | `QuestionError` con el rango válido |
| Indicadores dentro del catálogo | Plan descartado; se usa el parser local |
| Máximo/mínimo exige un indicador | `QuestionError("un solo indicador")` |
| Sentencia de solo lectura | `QuestionError("SELECT")` |

## Contrato HTTP (implementado en `portfolio-api`)

| Método | Ruta | Respuesta |
|---|---|---|
| `GET` | `/api/v1/copiloto-nl-sql/health` | Salud, conteo, modo de SQLite y capacidades. |
| `GET` | `/api/v1/copiloto-nl-sql/datos` | Metadatos del snapshot servido. |
| `GET` | `/api/v1/copiloto-nl-sql/query?question=…` | Plan, SQL, parámetros, filas y resumen. |

## No objetivos

- No es un copiloto económico general: un país y tres indicadores.
- No genera SQL libre desde texto ni ejecuta lo que proponga un modelo sin
  validarlo.
- No escribe en la base ni en sistemas externos durante una consulta.
