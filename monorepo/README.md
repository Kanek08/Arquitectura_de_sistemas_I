# Gestor de tareas

Una aplicación para anotar pendientes, marcarlos como completados y eliminarlos.

## Cómo ejecutarla

Necesitas Node.js 22 o posterior y npm. Desde esta carpeta:

```sh
npm install
npm run dev
```

Abre http://127.0.0.1:5173. El backend escucha en http://127.0.0.1:3001.
Vite manda las peticiones que empiezan con /api al backend.

También puedes iniciar cada aplicación en una terminal distinta:

```sh
npm run dev:backend
npm run dev:frontend
```

## Qué hay en cada carpeta

- apps/frontend: pantalla hecha con React, Vite y TypeScript.
- apps/backend: API hecha con Express y TypeScript.
- packages/compartido: tipos de las tareas y la función validarTitulo.

Las funciones y variables propias están en español. Algunos nombres como
scripts, dependencies y los métodos de Express se mantienen porque las herramientas
los necesitan así.

## Cómo funciona

1. Escribes un título de entre 3 y 100 caracteres.
2. El frontend lo revisa con validarTitulo y lo manda al backend.
3. El backend usa la misma función para revisarlo y lo agrega a su lista.
4. La pantalla muestra la tarea. Puedes marcarla, desmarcarla o eliminarla.

Las tareas se guardan en memoria: se pierden al reiniciar el backend.
No hace falta una base de datos para esta versión.

## Comandos

| Comando | Para qué sirve |
| --- | --- |
| npm run dev | Inicia ambas aplicaciones |
| npm run dev:frontend | Inicia solo la pantalla |
| npm run dev:backend | Inicia solo la API |
| npm run build | Compila la librería y las aplicaciones |
| npm run check-types | Revisa los tipos de TypeScript |
| npm run test | Prueba la validación y las operaciones de la API |

Turborepo organiza los comandos. Antes de iniciar las aplicaciones se compila
la librería compartida. Si cambias esa librería durante el desarrollo, vuelve a
ejecutar npm run dev para compilarla de nuevo.

Después de compilar, puedes iniciar el backend con
`npm run start --workspace=@gestor/backend`.
La compilación del frontend queda en apps/frontend/dist. Para revisarla en local,
inicia el backend y ejecuta
`npm run preview --workspace=@gestor/frontend -- --port 5173`.

## Rutas de la API

| Método | Ruta | Datos que recibe |
| --- | --- | --- |
| GET | /api/tareas | Ninguno |
| POST | /api/tareas | { "titulo": "Estudiar para el examen" } |
| PATCH | /api/tareas/:id | { "completada": true } |
| DELETE | /api/tareas/:id | Ninguno |

## Commits

Usa mensajes como estos para seguir Conventional Commits:

```text
feat: agregar lista de tareas
fix: corregir validación del título
docs: explicar cómo iniciar las aplicaciones
```
