# Arquitectura_de_sistemas_I
Git para el curso de arquitectura de sistemas I, Universidad Mesoamericana

# Descripción

API desarrollada con **Node.js**, **Express** y **TypeScript**. Permite realizar operaciones CRUD utilizando los métodos HTTP vistos en clase.

# Ejecutar el proyecto
npm run dev

### Obtener todos los estudiantes

**GET**

GET /estudiantes

Ejemplo:
http://localhost:3000/estudiantes

# Agregar un estudiante
**POST**
POST /estudiantes

Body (JSON):

json
{
    "nombre": "Carlos"
}

# Actualizar un estudiante
**PUT**
PUT /estudiantes/:id

Ejemplo:
PUT /estudiantes/1

Body:
json
{
    "nombre": "Pedro"
}

# Actualizar parcialmente un estudiante
**PATCH**
PATCH /estudiantes/:id

Ejemplo:
PATCH /estudiantes/1

Body:
json
{
    "nombre": "Ana"
}

# Eliminar un estudiante
**DELETE**
DELETE /estudiantes/:id

Ejemplo:
DELETE /estudiantes/1

