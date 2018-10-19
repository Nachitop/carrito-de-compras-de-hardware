@echo off
@echo "Enter APP name"
set /p app_name=
set building="Building django app %app_name%"
@echo %building%
python C:/Python27/Scripts/django-admin.py startapp %app_name%
pause