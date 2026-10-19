import { defineConfig as definirConfiguracion } from "vite";
import react from "@vitejs/plugin-react";

export default definirConfiguracion({
  plugins: [react()],
  optimizeDeps: { include: ["@gestor/compartido"] },
  build: { commonjsOptions: { include: [/node_modules/, /compartido/] } },
  server: {
    port: 5173,
    strictPort: true,
    proxy: { "/api": "http://127.0.0.1:3001" },
  },
});
