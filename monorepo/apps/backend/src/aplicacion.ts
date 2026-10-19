import express, { type ErrorRequestHandler as ManejadorError } from "express";
import { randomUUID as crearIdentificador } from "node:crypto";
import { validarTitulo, type Tarea } from "@gestor/compartido";

export function crearAplicacion() {
  const aplicacion = express();
  // La lista vive en memoria mientras el servidor esté encendido.
  const tareas: Tarea[] = [];
  aplicacion.use(express.json({ limit: "10kb" }));

  aplicacion.get("/api/tareas", (_solicitud, respuesta) => {
    respuesta.json(tareas);
  });

  aplicacion.post("/api/tareas", (solicitud, respuesta) => {
    const titulo = solicitud.body?.titulo;
    const mensaje = validarTitulo(titulo);
    if (mensaje) {
      respuesta.status(400).json({ mensaje });
      return;
    }

    const tarea: Tarea = {
      id: crearIdentificador(),
      titulo: titulo.trim(),
      completada: false,
    };
    tareas.push(tarea);
    respuesta.status(201).json(tarea);
  });

  aplicacion.patch("/api/tareas/:id", (solicitud, respuesta) => {
    const tarea = tareas.find((tareaActual) => tareaActual.id === solicitud.params.id);
    if (!tarea) {
      respuesta.status(404).json({ mensaje: "No se encontró la tarea." });
      return;
    }
    if (typeof solicitud.body?.completada !== "boolean") {
      respuesta.status(400).json({ mensaje: "Indica si la tarea está completada." });
      return;
    }
    tarea.completada = solicitud.body.completada;
    respuesta.json(tarea);
  });

  aplicacion.delete("/api/tareas/:id", (solicitud, respuesta) => {
    const posicion = tareas.findIndex((tarea) => tarea.id === solicitud.params.id);
    if (posicion === -1) {
      respuesta.status(404).json({ mensaje: "No se encontró la tarea." });
      return;
    }
    tareas.splice(posicion, 1);
    respuesta.status(204).send();
  });

  aplicacion.use((_solicitud, respuesta) => {
    respuesta.status(404).json({ mensaje: "La ruta no existe." });
  });

  const manejarError: ManejadorError = (error, _solicitud, respuesta, _siguiente) => {
    if (error.type === "entity.parse.failed") {
      respuesta.status(400).json({ mensaje: "El contenido enviado no es un JSON válido." });
      return;
    }
    if (error.type === "entity.too.large") {
      respuesta.status(413).json({ mensaje: "El contenido enviado es demasiado grande." });
      return;
    }
    console.error(error);
    respuesta.status(500).json({ mensaje: "Ocurrió un problema en el servidor." });
  };
  aplicacion.use(manejarError);
  return aplicacion;
}
