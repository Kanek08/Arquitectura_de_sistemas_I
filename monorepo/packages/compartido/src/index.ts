// Estos datos y esta función se usan en las dos aplicaciones.
export interface Tarea {
  id: string;
  titulo: string;
  completada: boolean;
}

export interface CrearTarea {
  titulo: string;
}

export interface ActualizarTarea {
  completada: boolean;
}

export interface ErrorApi {
  mensaje: string;
}

// Si el título está bien, devuelve una cadena vacía.
export function validarTitulo(titulo: unknown): string {
  if (typeof titulo !== "string" || titulo.trim().length === 0) {
    return "Escribe un título para la tarea.";
  }
  if (titulo.trim().length < 3) {
    return "El título debe tener al menos 3 caracteres.";
  }
  if (titulo.trim().length > 100) {
    return "El título no debe pasar de 100 caracteres.";
  }
  return "";
}
