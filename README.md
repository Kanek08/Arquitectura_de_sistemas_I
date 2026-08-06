# Arquitectura_de_sistemas_I
Git para el curso de arquitectura de sistemas I, Universidad Mesoamericana
<<<<<<< Updated upstream
=======

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

# Ejecutar la aplicación

npm run dev

# Acceder a la API

Una vez iniciado el servidor, la API estará disponible en:
http://localhost:3000

# Ver la documentación automática

La documentación generada con Swagger se encuentra en:

http://localhost:3000/docs

Desde esa página es posible consultar y probar todos los métodos HTTP implementados:

- GET
- POST
- PUT
- PATCH
- DELETE

>>>>>>> Stashed changes
