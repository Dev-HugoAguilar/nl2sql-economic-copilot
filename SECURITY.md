# Política de seguridad

## Alcance

La demo funciona con el snapshot incluido. El servicio abre una base SQLite derivada en modo solo lectura, rechaza sentencias distintas de SELECT y no escribe en sistemas externos durante una consulta. La auditoría en MongoDB y el proveedor de modelos son opcionales y están apagados por omisión.



## Cómo reportar

Si encuentras una vulnerabilidad, usa los **avisos privados de seguridad** de
GitHub: pestaña *Security* → *Report a vulnerability*. Evita abrir un *issue*
público con detalles explotables.

Incluye, cuando aplique:

- versión o commit afectado;
- pasos mínimos para reproducir;
- impacto esperado y observable;
- cualquier mitigación que ya hayas probado.

## Buenas prácticas para quien despliega

- No añadas credenciales al repositorio; usa variables de entorno.
- Sirve la demo detrás de HTTPS si la expones fuera de `127.0.0.1`.
- Revisa el resultado de la verificación de credenciales de la integración
  continua antes de fusionar cambios.

Este es un proyecto de portafolio mantenido de forma individual: se revisan los
reportes por orden de llegada y se responde con una evaluación inicial cuando el
reporte contiene pasos reproducibles.
