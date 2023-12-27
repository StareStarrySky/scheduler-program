@echo off
setlocal

if not defined CONDA_HOME (
    echo The environment variable CONDA_HOME is not set.
    exit /B 1
)

dir %CONDA_HOME% 1>NUL || (
    echo The path %CONDA_HOME% does not exist or is not a directory.
    exit /B 1
)

call %CONDA_HOME%\activate.bat scheduler-program
if %errorlevel% equ 0 (
    python ./build.py
) else (
    echo run activate.bat failed
)

endlocal
