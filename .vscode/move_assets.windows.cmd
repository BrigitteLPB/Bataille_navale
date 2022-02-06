robocopy .\assets .\build\assets **.* /s /j /purge
if %ERRORLEVEL% GEQ 9 exit /b 1
exit /b 0
