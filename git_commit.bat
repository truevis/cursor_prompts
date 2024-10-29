@echo off
echo Starting Git operations...

REM Remove secrets.toml from git tracking
echo Removing secrets.toml from git tracking...
git rm --cached .streamlit/secrets.toml
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to remove secrets.toml from tracking
    pause
    exit /b 1
)

REM Commit the untracking of secrets.toml
echo Committing changes...
git commit -m "Remove secrets.toml from git tracking"
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to commit changes
    pause
    exit /b 1
)

REM Add all other changes
echo Adding other changes...
git add .
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to add changes
    pause
    exit /b 1
)

REM Commit all changes
git commit -m "Update repository files"
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to commit changes
    pause
    exit /b 1
)

REM Push changes
echo Pushing to remote repository...
git push origin main
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to push changes
    pause
    exit /b 1
)

echo Git operations completed successfully!
pause 