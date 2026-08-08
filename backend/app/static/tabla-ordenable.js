// Ordenar una tabla haciendo clic en sus encabezados (<th data-col="N">).
// Reordena solo las filas ya presentes en el DOM — no vuelve a pedirle nada al
// servidor, así que no afecta ningún filtro que la página ya haya aplicado.
// Cada <td> puede llevar un atributo data-sort con el valor "real" a comparar
// (fecha ISO, número de prioridad, etc.) cuando el texto visible no alcanza
// para ordenar bien (ej: "22/07" no debe compararse como texto contra "05/08").
function activarOrdenamiento(tablaId) {
  const tabla = document.getElementById(tablaId);
  if (!tabla) return;
  const cuerpo = tabla.querySelector('tbody');
  const encabezados = tabla.querySelectorAll('th[data-col]');

  encabezados.forEach(th => {
    th.classList.add('ordenable');
    th.addEventListener('click', () => ordenarPor(th));
  });

  function ordenarPor(th) {
    const idx = Number(th.dataset.col);
    const direccionNueva = th.dataset.dir === 'asc' ? 'desc' : 'asc';
    encabezados.forEach(h => { h.dataset.dir = ''; h.classList.remove('asc', 'desc'); });
    th.dataset.dir = direccionNueva;
    th.classList.add(direccionNueva);

    const filas = Array.from(cuerpo.querySelectorAll('tr'));
    filas.sort((a, b) => {
      const va = valorCelda(a, idx);
      const vb = valorCelda(b, idx);
      if (va < vb) return direccionNueva === 'asc' ? -1 : 1;
      if (va > vb) return direccionNueva === 'asc' ? 1 : -1;
      return 0;
    });
    filas.forEach(f => cuerpo.appendChild(f));
  }

  function valorCelda(fila, idx) {
    const celda = fila.children[idx];
    const attr = celda.getAttribute('data-sort');
    if (attr === null) return celda.textContent.trim().toLowerCase();
    if (attr === '') return attr;
    const n = Number(attr);
    return Number.isFinite(n) ? n : attr;
  }
}
