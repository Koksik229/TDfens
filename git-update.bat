@echo off
chcp 65001 >nul
<<<<<<< HEAD
cd /d "C:\Users\Rabot\OneDrive\Рабочий стол\Работа\Project"
=======
cd /d %~dp0
>>>>>>> 71d4628bb2d5f6ecfeb6110ebe4b36fce3dbf7f2
echo Добавление всех изменений...
git add .
set /p msg=Введите комментарий к коммиту:
git commit -m "%msg%"
echo Отправка на GitHub...
git push
pause
