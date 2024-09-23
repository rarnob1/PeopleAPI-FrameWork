@echo off
call venv\scripts\activate
pytest -s -v -m "sanity or regression" .\test_cases\test_login_admin.py --browser firefox -n 3 --html reports/report.html
pause
