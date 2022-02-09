robocopy .\src .\build\ **.py /s /j /purge
if %ERRORLEVEL% GEQ 9 exit /b 1

copy /V /Y .env .\build\
