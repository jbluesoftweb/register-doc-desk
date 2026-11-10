# register-doc-desk

Aplicación de escritorio para **registrar y buscar documentos** (oficios, informes, etc.), pensada para funcionar en **una sola computadora con Windows 10 u 11, sin conexión a internet**.

> **Estado:** en desarrollo (aún sin versión publicada).

## Características previstas (v1.0)

- Inicio de sesión con tres roles: REGISTRADOR, ADMIN y SISTEMAS.
- Registro, edición, anulación y des-anulación de documentos.
- Búsqueda por asunto, con filtros por año y tipo de documento.
- Lista paginada (20 por página), ordenada por fecha del documento.
- Catálogo de tipos de documento (Oficio e Informe de inicio).
- Administración de usuarios según el rol.
- Bitácora de accesos.
- Respaldo de la base de datos.
- Instalador para Windows.

## Tecnologías

- Python 3 y Tkinter
- SQLite
- Arquitectura por capas (interfaz, servicios, repositorios)

## Seguridad

- Las contraseñas se guardan con hash (`scrypt`) y nunca en texto plano.
- No existe ninguna contraseña de fábrica: en el primer arranque, un asistente crea el usuario SISTEMAS.
- Para reportar una vulnerabilidad, consulta [SECURITY.md](SECURITY.md).

## Licencia

Distribuido bajo licencia [MIT](LICENSE).