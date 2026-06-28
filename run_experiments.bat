@echo off
setlocal

cd /d "%~dp0"
python run_experiments.py %*
exit /b %ERRORLEVEL%
