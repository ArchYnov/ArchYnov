/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#BB004B",
        secondary: "#FA7268",
        background: "#0f0e17",
        background_secondary: "#171726",
        neon: "hsl(329, 100%, 36%)",
      },
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
        aldrich: ["Aldrich", "sans-serif"],
        newake: ["Newake", "sans-serif"],
        josefin: ["Josefin Sans", "sans-serif"],
      },
      screens: {
        xs: "480px",
        ss: "620px",
        sm: "768px",
        md: "1060px",
        lg: "1200px",
        xl: "1700px",
      },
  },
  plugins: [],
}}
