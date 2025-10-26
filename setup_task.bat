@echo off
echo Setting up Task Scheduler for Daily Words Popup...
schtasks /create /tn "Daily Words Popup" /tr "\"%~dp0dist\wordshow.exe\"" /sc onlogon /rl highest /f
if %ERRORLEVEL%==0 (
    echo Task created successfully. wordshow.exe will run automatically on login.
) else (
    echo Failed to create task. Run as Administrator.
)
pause