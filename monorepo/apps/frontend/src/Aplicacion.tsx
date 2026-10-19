import { useEffect as usarEfecto, useState as usarEstado, type FormEvent as EventoFormulario } from "react";
import { validarTitulo, type Tarea } from "@gestor/compartido";

export default function Aplicacion() {
  const [tareas, cambiarTareas] = usarEstado<Tarea[]>([]);
  const [titulo, cambiarTitulo] = usarEstado("");
  const [mensaje, cambiarMensaje] = usarEstado("");
  const [cargando, cambiarCargando] = usarEstado(true);
  const [guardando, cambiarGuardando] = usarEstado(false);
  const [tareaOcupada, cambiarTareaOcupada] = usarEstado<string | null>(null);
  const completadas = tareas.filter((tarea) => tarea.completada).length;

  async function consultarTareas() {
    cambiarCargando(true);
    cambiarMensaje("");
    try {
      const respuesta = await fetch("/api/tareas");
      if (!respuesta.ok) throw new Error("No se pudieron cargar las tareas.");
      const lista: Tarea[] = await respuesta.json();
      cambiarTareas(lista);
    } catch {
      cambiarMensaje("No se pudieron cargar las tareas. Revisa que el backend esté encendido.");
    } finally {
      cambiarCargando(false);
    }
  }

  usarEfecto(() => { void consultarTareas(); }, []);

  async function agregarTarea(evento: EventoFormulario<HTMLFormElement>) {
    evento.preventDefault();
    const errorTitulo = validarTitulo(titulo);
    cambiarMensaje(errorTitulo);
    if (errorTitulo) return;

    cambiarGuardando(true);
    try {
      const respuesta = await fetch("/api/tareas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo }),
      });
      if (!respuesta.ok) {
        const error = await respuesta.json();
        throw new Error(error.mensaje);
      }
      const nuevaTarea: Tarea = await respuesta.json();
      cambiarTareas((lista) => [...lista, nuevaTarea]);
      cambiarTitulo("");
    } catch (error) {
      cambiarMensaje(error instanceof Error ? error.message : "No se pudo agregar la tarea.");
    } finally {
      cambiarGuardando(false);
    }
  }

  async function cambiarEstado(tarea: Tarea) {
    cambiarTareaOcupada(tarea.id);
    cambiarMensaje("");
    try {
      const respuesta = await fetch(`/api/tareas/${tarea.id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completada: !tarea.completada }),
      });
      if (!respuesta.ok) throw new Error("No se pudo cambiar el estado de la tarea.");
      const tareaActualizada: Tarea = await respuesta.json();
      cambiarTareas((lista) => lista.map((actual) => actual.id === tarea.id ? tareaActualizada : actual));
    } catch (error) {
      cambiarMensaje(error instanceof Error ? error.message : "No se pudo actualizar la tarea.");
    } finally {
      cambiarTareaOcupada(null);
    }
  }

  async function eliminarTarea(identificador: string) {
    cambiarTareaOcupada(identificador);
    cambiarMensaje("");
    try {
      const respuesta = await fetch(`/api/tareas/${identificador}`, { method: "DELETE" });
      if (!respuesta.ok) throw new Error("No se pudo eliminar la tarea.");
      cambiarTareas((lista) => lista.filter((tarea) => tarea.id !== identificador));
    } catch (error) {
      cambiarMensaje(error instanceof Error ? error.message : "No se pudo eliminar la tarea.");
    } finally {
      cambiarTareaOcupada(null);
    }
  }

  return (
    <main className="contenedor">
      <header>
        <p className="etiqueta">UN PASO A LA VEZ</p>
        <h1>Mis tareas</h1>
        <p>Organiza lo que tienes pendiente para hoy.</p>
      </header>

      <section className="tarjeta" aria-label="Agregar y consultar tareas">
        <form onSubmit={agregarTarea}>
          <label htmlFor="titulo">¿Qué necesitas hacer?</label>
          <div className="formulario">
            <input id="titulo" value={titulo} onChange={(evento) => cambiarTitulo(evento.target.value)}
              placeholder="Ej. Estudiar para el examen" maxLength={100} disabled={guardando || cargando} />
            <button disabled={guardando || cargando}>{guardando ? "Agregando..." : "Agregar"}</button>
          </div>
          <small>Entre 3 y 100 caracteres.</small>
        </form>

        {mensaje && <p className="mensaje" role="alert">{mensaje}</p>}
        <div className="resumen">
          <h2>Tu lista</h2>
          <span>{completadas} de {tareas.length} completadas</span>
        </div>

        {cargando ? <p role="status">Cargando tareas...</p> : (
          <>
            {tareas.length === 0 && <p className="vacio">Todavía no tienes tareas. Agrega la primera.</p>}
            <ul className="lista">
              {tareas.map((tarea) => (
                <li key={tarea.id} className={tarea.completada ? "completada" : ""}>
                  <label className="nombre-tarea">
                    <input type="checkbox" checked={tarea.completada} disabled={tareaOcupada !== null}
                      onChange={() => void cambiarEstado(tarea)} />
                    <span>{tarea.titulo}</span>
                  </label>
                  <button type="button" className="eliminar" disabled={tareaOcupada !== null}
                    aria-label={`Eliminar tarea: ${tarea.titulo}`}
                    onClick={() => void eliminarTarea(tarea.id)}>Eliminar</button>
                </li>
              ))}
            </ul>
            <button type="button" className="recargar" disabled={guardando || tareaOcupada !== null}
              onClick={() => void consultarTareas()}>Actualizar lista</button>
          </>
        )}
      </section>
      <p className="nota">Las tareas se guardan mientras el backend esté encendido.</p>
    </main>
  );
}
