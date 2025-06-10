@echo off
chcp 65001 >nul
cd /d "C:\Users\Rabot\OneDrive\Рабочий стол\Работа\Project"
if not exist .git (
    echo ❌ Git-репозиторий не найден в этой папке!
    pause
    exit /b
)

git add .
set /p msg=Введите комментарий к коммиту:
git commit -m "%msg%"
git push
pause
