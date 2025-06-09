@echo off
chcp 65001 >nul
cd /d "C:\Users\Rabot\OneDrive\Рабочий стол\Работа\Project"

if exist .git (
    echo ✅ Git-репозиторий найден. Выполняю коммит...
    git add .
    set /p msg=Введите комментарий к коммиту:
    git commit -m "%msg%"
    echo Отправка на GitHub...
    git push
) else (
    echo ❌ Папка не является Git-репозиторием!
    echo Проверь, что ты в папке проекта, и выполни:
    echo.
    echo git init
    echo git remote add origin https://github.com/Koksik229/TDfens.git
    echo git branch -M main
    echo git add .
    echo git commit -m "initial"
    echo git push -u origin main
)
pause
