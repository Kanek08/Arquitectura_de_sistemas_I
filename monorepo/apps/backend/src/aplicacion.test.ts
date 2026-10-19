import { test as prueba } from "node:test";
import assert from "node:assert/strict";
import { once as esperarEvento } from "node:events";
import { crearAplicacion } from "./aplicacion";
import { validarTitulo } from "@gestor/compartido";

prueba("el título necesita entre 3 y 100 caracteres sin contar espacios externos", () => {
  for (const titulo of [undefined, null, 42, "", "   ", "ab", "a".repeat(101)]) {
    assert.notEqual(validarTitulo(titulo), "");
  }
  assert.equal(validarTitulo("  Estudiar  "), "");
  assert.equal(validarTitulo("a".repeat(100)), "");
});

prueba("la API permite crear, consultar, completar y eliminar tareas", async () => {
  const servidor = crearAplicacion().listen(0, "127.0.0.1");
  await esperarEvento(servidor, "listening");
  const direccion = servidor.address();
  if (!direccion || typeof direccion === "string") throw new Error("No se obtuvo el puerto.");
  const ruta = `http://127.0.0.1:${direccion.port}/api/tareas`;
  try {
    const invalida = await fetch(ruta, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo: "  " }),
    });
    assert.equal(invalida.status, 400);
    const creada = await fetch(ruta, {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo: "  Estudiar para el examen  " }),
    });
    assert.equal(creada.status, 201);
    const tarea = await creada.json();
    assert.equal(tarea.titulo, "Estudiar para el examen");
    assert.equal(tarea.completada, false);
    assert.deepEqual(await (await fetch(ruta)).json(), [tarea]);
    const estadoInvalido = await fetch(`${ruta}/${tarea.id}`, {
      method: "PATCH", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completada: "sí" }),
    });
    assert.equal(estadoInvalido.status, 400);
    for (const completada of [true, false]) {
      const actualizada = await fetch(`${ruta}/${tarea.id}`, {
        method: "PATCH", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completada }),
      });
      assert.equal(actualizada.status, 200);
      assert.equal((await actualizada.json()).completada, completada);
    }
    const eliminada = await fetch(`${ruta}/${tarea.id}`, { method: "DELETE" });
    assert.equal(eliminada.status, 204);
    assert.deepEqual(await (await fetch(ruta)).json(), []);
    assert.equal((await fetch(`${ruta}/${tarea.id}`, { method: "DELETE" })).status, 404);
    const malformada = await fetch(ruta, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: "{",
    });
    assert.equal(malformada.status, 400);
  } finally {
    await new Promise<void>((resolver, rechazar) => {
      servidor.close((error) => error ? rechazar(error) : resolver());
      servidor.closeAllConnections();
    });
  }
});
