# Datos: fuente, licencia y límites

## Origen

`web/data.json` contiene un snapshot de **World Development Indicators** del
Banco Mundial para México, años 2019–2025.

| Campo | Valor |
|---|---|
| `dataset_id` | `WDI-MEX-2019-2025` (snapshot del 2026-11-15) |
| Cobertura | México (`MEX`), 2019–2025 |
| Observaciones | 21 (3 indicadores × 7 años) |
| Licencia | **CC BY 4.0** |

## Indicadores

| Código | Indicador | Unidad |
|---|---|---|
| `NY.GDP.MKTP.KD.ZG` | Crecimiento del PIB real | % anual |
| `FP.CPI.TOTL.ZG` | Inflación al consumidor | % anual |
| `SL.UEM.TOTL.ZS` | Desempleo total · estimación OIT | % de la fuerza laboral |

Cada indicador conserva en `sources` su título, URL de origen, URL de la API con
el filtro exacto y su definición publicada. La descarga se puede reproducir con
`pipeline/refresh_worldbank.py`.

## Verificaciones que el servicio aplica al cargar

- El snapshot debe contener los tres indicadores del catálogo.
- Cada fila debe traer un `year` entero y un `indicator_code` conocido.
- Un snapshot incompleto produce `DatasetError`; no se degrada en silencio a una
  base parcial.

## Atribución

> World Development Indicators, Banco Mundial. Datos bajo CC BY 4.0. Se cita el
> código de indicador, la unidad y el periodo en cada respuesta.

Este repositorio no incluye un archivo `LICENSE` propio. Las condiciones de la
fuente se respetan y se documentan aquí; cualquier reutilización del snapshot debe
conservar la atribución al Banco Mundial.

## Límites de interpretación

- Es un extracto de tres indicadores, no una serie económica completa.
- `SL.UEM.TOTL.ZS` es una estimación modelada de la OIT: no mide informalidad ni
  subempleo.
- La inflación es el índice general, no el componente subyacente ni la meta del
  banco central.
- Los valores son anuales; preguntas de corto plazo quedan fuera de alcance.
- El copiloto no calcula proyecciones ni escenarios: describe lo observado y
  agrega con plantillas.
