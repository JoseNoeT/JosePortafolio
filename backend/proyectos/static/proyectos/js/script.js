// ==========================================================
// Script global para el portafolio
// - Detecta cuando el DOM está cargado
// - Aplica efectos dinámicos al header al hacer scroll
// ==========================================================

document.addEventListener('DOMContentLoaded', function () {
    console.log("Script cargado correctamente.");

    // Detectar el navbar
    const nav = document.getElementById('mainNav');

    // Cambiar estilo al hacer scroll
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled'); // Agrega el estilo dinámico
        } else {
            nav.classList.remove('scrolled'); // Vuelve al estilo original
        }
    });
});
