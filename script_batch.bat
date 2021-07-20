@echo off
echo hi

https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe
start %cd%/python-3.6.8-amd64.exe
py -m pip install pyautogui

curl https://raw.githubusercontent.com/esquim0/toRemove/main/script_autoclick.py > script_autoclick.py
python script_autoclick.py
pause