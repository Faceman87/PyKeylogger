@echo off
tasklist /nh /fi "imagename eq pythonw.exe" | find /i "pythonw.exe" > nul || (start "" "C:\Users\cgain\Documents\GainesPythonScript.pyw")
start "" "c:\Program Files (x86)\Internet Explorer\iexplore.exe"