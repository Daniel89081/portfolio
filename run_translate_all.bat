@echo off
cd /d "c:\Users\Fo\Documents\danieldietrich.tech"
python translate_all.py
if %ERRORLEVEL% EQU 0 (
  echo.
  echo Translation completed successfully!
  pause
) else (
  echo.
  echo Translation failed with error code %ERRORLEVEL%
  pause
  exit /b %ERRORLEVEL%
)
