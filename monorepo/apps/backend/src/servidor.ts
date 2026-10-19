import { crearAplicacion } from "./aplicacion";

const puerto = 3001;
const aplicacion = crearAplicacion();

aplicacion.listen(puerto, "127.0.0.1", () => {
  console.log(`Backend listo en http://127.0.0.1:${puerto}`);
});
