@echo off
chcp 65001 >nul
cd /d "C:\Users\Rabot\OneDrive\Рабочий стол\Работа\Project"
echo Добавление всех изменений...
git add .
set /p msg=Введите комментарий к коммиту:
git commit -m "%msg%"
echo Отправка на GitHub...
git push
pause
