"""Punto de entrada para el .exe empaquetado: arranca el servidor sin mostrar
ninguna consola y abre el navegador solo en cuanto está listo."""
import ctypes
import os
import sys
import threading
import time
import traceback
import webbrowser

# En modo --windowed no hay consola: sys.stdout/stderr pueden ser None y
# rompen cualquier librería que intente escribir ahí (uvicorn incluida).
if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

HOST = "127.0.0.1"
PORT = 8000


def _carpeta_datos():
    if getattr(sys, "frozen", False):
        from pathlib import Path
        return Path(sys.executable).parent
    from pathlib import Path
    return Path(__file__).resolve().parent


def _avisar_error(mensaje: str):
    try:
        (_carpeta_datos() / "error.log").write_text(mensaje, encoding="utf-8")
    except Exception:
        pass
    try:
        ctypes.windll.user32.MessageBoxW(
            0,
            "NODO no pudo arrancar. Se guardó el detalle en error.log, "
            "al lado del programa.\n\n" + mensaje[-500:],
            "NODO — Error al iniciar",
            0x10,  # MB_ICONERROR
        )
    except Exception:
        pass


def _abrir_navegador(demora=1.5):
    time.sleep(demora)
    webbrowser.open(f"http://{HOST}:{PORT}")


def _ya_esta_corriendo() -> bool:
    """Si cerraste la pestaña sin usar "Cerrar aplicación", el servidor sigue
    vivo en segundo plano. En ese caso no tiene sentido intentar levantar otro
    (fallaría porque el puerto ya está ocupado) — alcanza con abrir una
    pestaña nueva apuntando al que ya está corriendo."""
    import urllib.request
    try:
        with urllib.request.urlopen(f"http://{HOST}:{PORT}/healthz", timeout=0.5) as r:
            return r.status == 200
    except Exception:
        return False


def main():
    if _ya_esta_corriendo():
        _abrir_navegador(demora=0)
        return

    try:
        import uvicorn
        from app.main import app
    except Exception:
        _avisar_error(traceback.format_exc())
        return

    threading.Thread(target=_abrir_navegador, daemon=True).start()
    try:
        uvicorn.run(app, host=HOST, port=PORT, log_level="warning")
    except Exception:
        _avisar_error(traceback.format_exc())


if __name__ == "__main__":
    main()
