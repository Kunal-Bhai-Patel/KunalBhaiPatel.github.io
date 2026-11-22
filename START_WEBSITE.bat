@echo off
setlocal
cd /d "%~dp0"

echo =======================================================
echo  Kunal Bhai Patel - Portfolio Website Launcher
echo =======================================================
echo.

:: Check Python installation
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python 3 was not found in your system PATH.
    echo Please install Python 3 or add it to your PATH to run the portfolio.
    echo.
    pause
    exit /b 1
)

echo [1/3] Building static website with Python static generator...
python build.py
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Static site build failed. Please check build errors above.
    pause
    exit /b 1
)

echo.
echo [2/3] Launching default web browser at http://localhost:8080/en/ ...
start http://localhost:8080/en/

echo.
echo [3/3] Starting local preview server on port 8080...
echo Serving directory: %~dp0dist
echo Press Ctrl+C in this terminal window to stop the server.
echo.
python serve.py 8080

endlocal
