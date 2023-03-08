@echo off 
Title Descargando Módulos...
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python -m pip install -r requirements.txt
cls
Title Descargando Módulos
echo python Jesus-C.py >> start.bat
start start.bat
