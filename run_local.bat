@echo off
cd /d %~dp0

if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo.
        echo No se pudo crear el entorno virtual. Revisa que Python este instalado y en el PATH.
        pause
        exit /b 1
    )
)

call venv\Scripts\activate.bat

echo Actualizando pip...
python -m pip install --upgrade pip >nul

echo Instalando dependencias...
pip install -r backend\requirements-local.txt
if errorlevel 1 (
    echo.
    echo Fallo la instalacion de dependencias. Revisa el error de arriba.
    pause
    exit /b 1
)

echo Creando/actualizando la base de datos local...
python init_local_db.py
if errorlevel 1 (
    echo.
    echo Fallo la creacion de la base de datos. Revisa el error de arriba.
    pause
    exit /b 1
)

echo.
echo Abri http://localhost:8000 en el navegador cuando diga "Application startup complete".
echo Para cortar el servidor: Ctrl+C en esta ventana.
echo.

cd backend
uvicorn app.main:app --reload
pause
