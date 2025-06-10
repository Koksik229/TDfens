@echo off
chcp 65001 >nul
cd /d "C:\Users\Rabot\OneDrive\Рабочий стол\Работа\Project\backend"
call venv\Scripts\activate
uvicorn main:app --reload
pause
