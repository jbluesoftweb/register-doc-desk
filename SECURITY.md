# Política de seguridad

## Versiones con soporte

| Versión | Soporte de seguridad |
|---------|----------------------|
| 1.x     | Sí                   |
| < 1.0   | No (en desarrollo)   |

## Cómo reportar una vulnerabilidad

**No abras un issue público** para reportar un problema de seguridad.

Usa el reporte privado de GitHub:

1. Entra a la pestaña **Security** del repositorio.
2. Pulsa **Report a vulnerability**.
3. Describe el problema, los pasos para reproducirlo y su impacto posible.

Recibirás una respuesta lo antes posible. Una vez corregido el problema, se
publicará una nota con el crédito correspondiente, si lo deseas.

## Alcance

Este software es una aplicación de escritorio local, sin conexión a red.
Son de interés los problemas relacionados con:

- Autenticación, contraseñas y control de permisos por rol.
- Inyección SQL o manejo inseguro de datos.
- Exposición de información sensible en archivos o registros.

## Recomendaciones para quien instala el software

- Cambiar de inmediato cualquier contraseña temporal.
- Restringir los permisos de la carpeta de datos a las cuentas necesarias.
- Hacer copias de seguridad periódicas y guardarlas fuera del equipo.
- No subir nunca la base de datos a un repositorio ni compartirla sin proteger.