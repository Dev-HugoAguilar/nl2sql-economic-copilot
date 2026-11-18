# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
las versiones usan [Versionado Semántico](https://semver.org/lang/es/).

## [1.0.0] — 2026-11-26

### Añadido

- Primera publicación como repositorio independiente.
- Aplicación estática con consulta, SQL generado, tabla de resultados y resumen.
- Servicio de dominio con parser local léxico, plan validado y plantilla SQL
  parametrizada.
- Conexión SQLite en modo solo lectura y rechazo de sentencias que no son
  `SELECT`.
- Integración opcional con un proveedor de modelos que solo puede proponer un
  plan JSON, descartado si no pasa las validaciones.
- Auditoría opcional en MongoDB que no guarda el texto de la pregunta.
- Once pruebas con sqlite3 real, incluidas el intento de inyección y el rechazo de
  escrituras.
- Integración continua de pruebas, sintaxis, integridad y credenciales.
