import express, { Request, Response } from "express";

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

app.listen(PORT, () => {
  console.log(`Servidor ejecutándose en http://localhost:${PORT}`);
});