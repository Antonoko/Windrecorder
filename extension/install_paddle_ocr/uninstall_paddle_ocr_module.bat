@echo off
echo Loading extension, please stand by.
echo.

cd /d %~dp0
chcp 65001

:start_install
cls
echo.
echo   Enter Y and press Enter to uninstall RapidOCR (Paddle OCR based on ONNXRuntime) module.
echo   输入 Y 后回车卸载 RapidOCR（Paddle OCR 的 ONNXRuntime 版本）。
echo.
echo   ================================================================================
echo.
set /p choice=   Please enter the options and press Enter:

if /I "%choice%"=="Y" (
    echo Uninstalling...
    goto uninstall_module
)

goto start_install


@REM -------------------------------------------------
:uninstall_module
poetry run pip uninstall rapidocr_onnxruntime
goto :finish


@REM -------------------------------------------------
:finish
for /F "tokens=* USEBACKQ" %%A in (`python -m poetry env info --path`) do call "%%A\Scripts\activate.bat"
python _uninstall.py
echo.
echo   The uninstallation script has been completed. 已执行完卸载脚本。
echo.
pause
exit