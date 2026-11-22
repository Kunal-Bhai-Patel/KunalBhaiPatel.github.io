@echo off
setlocal
cd /d "%~dp0"

echo =======================================================
echo  Publishing Portfolio to GitHub: KunalBhaiPatel.github.io
echo =======================================================
echo.
echo Target Remote: https://github.com/Kunal-Bhai-Patel/KunalBhaiPatel.github.io.git
echo Branch:        main
echo.
echo Pushing local commit e78c272 to GitHub...
echo (If prompted, click "Sign in with your browser" to authorize Git)
echo.

git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo =======================================================
    echo  SUCCESS! Your portfolio code has been pushed to GitHub.
    echo =======================================================
    echo.
    echo GitHub Actions will now automatically build and publish your site.
    echo You can track the deployment here:
    echo https://github.com/Kunal-Bhai-Patel/KunalBhaiPatel.github.io/actions
    echo.
) else (
    echo.
    echo [ERROR] Push failed. Please check the error message above.
    echo.
)

pause
endlocal
