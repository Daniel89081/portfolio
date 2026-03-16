@echo off
setlocal enabledelayedexpansion

cd /d "c:\Users\Fo\Documents\danieldietrich.tech"

echo.
echo ============================================================
echo  German HTML Translation Script
echo ============================================================
echo.

python translate_final.py
exit /b %ERRORLEVEL%
