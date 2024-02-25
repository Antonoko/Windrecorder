@echo off
title Windrecorder
mode con cols=70 lines=10
color 75
echo.
echo   Initializing Windrecorder, please stand by...
echo.
echo   Please do not leave this window until it disappears
echo.

cd /d %~dp0
for /F "tokens=* USEBACKQ" %%A in (`python -m poetry env info --path`) do call %%A\Scripts\activate.bat

python "%~dp0\main.py"