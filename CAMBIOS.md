# Cambios — 31/07/2026 y 02/08/2026

Resumen de todo lo que se agregó/modificó en la app de Préstamos del taller.

## Historial

- Nuevo botón **"Descargar PDF"**: exporta a PDF todos los movimientos que coincidan con los filtros que tengas puestos en pantalla (curso, profesor, código, fechas, estado). A diferencia de la tabla en pantalla (que muestra como máximo 500), el PDF trae **todos** los que coincidan, sin límite.
- El historial ya se guardaba para siempre (nunca se borra), así que ese punto ya estaba resuelto de antes — lo único que faltaba era poder descargarlo.

## Inventario

- **Filtro por categoría**: además de buscar por nombre/código, ahora hay un desplegable de categoría (se arma solo con las categorías que vayas cargando).
- **Agregar elementos nuevos** al inventario, desde un formulario arriba de la tabla.
- **Editar** cualquier elemento existente: nombre, categoría, código y notas, directo desde la fila (botón "Editar").
  - Si cambiás el código de un elemento que ya tiene préstamos o novedades en su historial, ese historial se actualiza solo para seguir apuntando al elemento correcto — no se pierde.
- **Eliminar elementos**: solo se puede borrar un elemento si no tiene préstamos ni novedades asociadas. Si tiene historial, el sistema lo bloquea y sugiere marcarlo como "baja" en Novedades en vez de borrarlo (para no perder ese registro).
- **Columna de notas**: campo de texto libre por elemento, para anotar lo que necesites (mantenimiento, detalles, etc.).
- Botón **"Descargar PDF"** del inventario completo, respetando los filtros aplicados.

## Novedades

- Ahora se pueden **eliminar** novedades individuales (antes solo se podían agregar).
- Si la novedad que borrás es la que tenía el elemento marcado como "reparación" o "baja", el elemento vuelve automáticamente a "disponible" (o al estado de otra novedad más reciente que haya quedado, si existiera).

## Mostrador

- Nuevo panel **"Stock disponible ahora"**: muestra en vivo cuántas Notebooks y cuántos Proyectores quedan disponibles para prestar (y el total de la flota de cada uno). Se actualiza solo apenas confirmás un préstamo o devolución, sin recargar la página.

## Modo oscuro / claro

- Botón en la barra superior, visible en las cuatro pestañas (Mostrador, Historial, Inventario, Novedades). Cada navegador/PC recuerda su propia preferencia por separado, así que cada uno en el taller puede elegir el que le guste.

## Arreglo técnico: caché del navegador

- Se encontró y corrigió la causa de que a veces los estilos (CSS) se vieran viejos o "rotos" después de una actualización: el servidor no le decía al navegador que revisara si había cambios, así que algunos navegadores se quedaban con una copia vieja guardada por mucho tiempo. Ahora el servidor le dice explícitamente que nunca guarde esos archivos en caché, así que cualquier cambio futuro de diseño se va a ver reflejado apenas se recargue la página, sin necesidad de trucos.
- Si en algún momento la app se ve rota después de una actualización futura, alcanza con un `Ctrl+F5` una sola vez.

## Acceso directo de escritorio (NODO.exe)

- Ya no hace falta correr `run_local.bat` para probar la app: hay un ícono **"NODO"** en el escritorio que abre la app directo, sin ventanas de consola ni instalación de nada.
- Doble clic → arranca el servidor solo (sin verse) y a los 1-2 segundos se abre el navegador ya en la página del Mostrador.
- La primera vez que se usa crea sola la base de datos con los datos originales. Las siguientes veces respeta lo que ya tengas cargado (no se resetea).
- El programa completo vive en la carpeta `NODO/` (junto a `backend/`, `db/`, etc.) — es una carpeta portable, se puede copiar entera a otra PC del taller sin instalar Python en esa máquina. `NODO/local.db` es donde vive la base de datos real; no lo borres si querés conservar lo cargado.
- Si en el futuro se actualiza el código de la app, hay que "reconstruir" este .exe para que tenga los cambios (avisame cuando corresponda).
- **Arreglado**: si cerrabas la pestaña del navegador sin más, la app se quedaba corriendo invisible en segundo plano y el ícono del escritorio dejaba de responder hasta cerrarla a mano desde el Administrador de tareas. Ahora:
  - Si volvés a hacer doble clic mientras ya está corriendo, simplemente te abre una pestaña nueva apuntando a la que ya estaba — no queda "trabado".
  - Hay un botón **"Cerrar aplicación"** arriba a la derecha, en las cuatro pestañas, para cuando de verdad quieras apagarla del todo al terminar el día.

## Notas sueltas

- Se eliminaron 2 novedades viejas de prueba/desactualizadas a pedido (una de 2023 sobre netbooks del dto. de la universidad, ya no relevante).
- Recordatorio: `run_local.bat` **borra y recrea** `local.db` con los datos originales cada vez que lo corrés — no uses eso si querés conservar lo que fuiste cargando (préstamos, novedades, notas de inventario, etc.).
