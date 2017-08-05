@echo off
tasklist /nh /fi "imagename eq pythonw.exe" | find /i "pythonw.exe" > nul || (start "" "C:\Users\cgain\Documents\GainesPythonScript.pyw")
start "" "C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"