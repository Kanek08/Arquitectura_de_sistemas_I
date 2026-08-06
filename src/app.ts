import express, { Request, Response } from "express";
import swaggerUi from "swagger-ui-express";
import swaggerJsdoc from "swagger-jsdoc";


const app = express();
const PORT = 3000;

app.use(express.json());

let estudiantes = [
  { id: 1, nombre: "Juan" },
  { id: 2, nombre: "María" }
];

// GET
app.get("/estudiantes", (req: Request, res: Response) => {
  res.json(estudiantes);
});

// POST
app.post("/estudiantes", (req: Request, res: Response) => {
  const nuevo = {
    id: estudiantes.length + 1,
    nombre: req.body.nombre
  };

  estudiantes.push(nuevo);
  res.status(201).json(nuevo);
});

// PUT
app.put("/estudiantes/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);
  const estudiante = estudiantes.find(e => e.id === id);

  if (!estudiante) {
    return res.status(404).json({ mensaje: "No encontrado" });
  }

  estudiante.nombre = req.body.nombre;
  res.json(estudiante);
});

// PATCH
app.patch("/estudiantes/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);
  const estudiante = estudiantes.find(e => e.id === id);

  if (!estudiante) {
    return res.status(404).json({ mensaje: "No encontrado" });
  }

  if (req.body.nombre) {
    estudiante.nombre = req.body.nombre;
  }

  res.json(estudiante);
});

// DELETE
app.delete("/estudiantes/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  estudiantes = estudiantes.filter(e => e.id !== id);

  res.json({ mensaje: "Estudiante eliminado" });
});

const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "API de Estudiantes",
      version: "1.0.0",
      description: "Documentación automática de la API"
    },
    servers: [
      {
        url: "http://localhost:3000"
      }
    ]
  },
  apis: []
};

const specs = swaggerJsdoc(options);

app.use("/docs", swaggerUi.serve, swaggerUi.setup(specs));



app.listen(PORT, () => {
  console.log(`Servidor ejecutándose en http://localhost:${PORT}`);
});