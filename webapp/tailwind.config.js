/** @type {import('tailwindcss').Config} */
export default {
  content: [
      // Django
      "../templates/**/*.html",
      "../accounts/**/*.html",
      // Vue
      "./src/**/*.vue",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

