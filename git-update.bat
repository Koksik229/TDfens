@echo off
chcp 65001 >nul
cd /d %~dp0
echo Добавление всех изменений...
git add .
set /p msg=Введите комментарий к коммиту:
git commit -m "%msg%"
echo Отправка на GitHub...
git push
pause
