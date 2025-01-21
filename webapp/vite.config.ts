import { resolve } from 'path'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  // Matches Django's STATIC_URL setting
  base: "/static/",
  build: {
    // Used by django_vite to map artifacts to Django's static files
    manifest: "manifest.json",
    // Matches Django's STATIC_ROOT setting, used by collectstatic for production
    outDir: resolve("./dist"),
    // Our entry points
    rollupOptions: {
      input: {
        main: resolve('./src/main.ts'),
        tailwind: resolve('./src/style.css')
      }
    }
  }
})