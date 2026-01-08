@echo off
REM Enuanza Build Script for Windows
REM This script builds the C++ version of Enuanza with vcpkg dependencies

echo ================================================
echo    Enuanza C++ Build Script for Windows
echo ================================================

REM Check if we're in the right directory
if not exist "CMakeLists.txt" (
    echo ERROR: CMakeLists.txt not found. Please run this script from the enuanza_cpp directory.
    pause
    exit /b 1
)

REM Check for Visual Studio
if not defined VCINSTALLDIR (
    echo WARNING: Visual Studio environment not detected.
    echo Please run this script from a Developer Command Prompt for VS.
    echo You can find this in your Start Menu under Visual Studio Tools.
    pause
)

REM Check for vcpkg
if not defined VCPKG_ROOT (
    echo WARNING: VCPKG_ROOT not set. Attempting to find vcpkg...
    if exist "C:\vcpkg\scripts\buildsystems\vcpkg.cmake" (
        set VCPKG_ROOT=C:\vcpkg
        echo Found vcpkg at C:\vcpkg
    ) else if exist "D:\vcpkg\scripts\buildsystems\vcpkg.cmake" (
        set VCPKG_ROOT=D:\vcpkg
        echo Found vcpkg at D:\vcpkg
    ) else (
        echo ERROR: vcpkg not found. Please install vcpkg and set VCPKG_ROOT environment variable.
        echo See: https://vcpkg.io/en/getting-started.html
        pause
        exit /b 1
    )
)

REM Create build directory
echo [INFO] Creating build directory...
if not exist "build" mkdir build
cd build

REM Configure with CMake
echo [INFO] Configuring project with CMake...
cmake .. ^
    -DCMAKE_TOOLCHAIN_FILE="%VCPKG_ROOT%\scripts\buildsystems\vcpkg.cmake" ^
    -DCMAKE_BUILD_TYPE=Release ^
    -G "Visual Studio 16 2019" ^
    -A x64

if %ERRORLEVEL% neq 0 (
    echo ERROR: CMake configuration failed!
    pause
    exit /b 1
)

REM Build the project
echo [INFO] Building Enuanza...
cmake --build . --config Release

if %ERRORLEVEL% neq 0 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

REM Check if build was successful
if exist "Release\Enuanza.exe" (
    echo [INFO] Build successful! Executable created: %cd%\Release\Enuanza.exe
) else (
    echo ERROR: Build failed! Executable not found.
    pause
    exit /b 1
)

REM Copy required DLLs
echo [INFO] Copying runtime dependencies...
copy "%VCPKG_ROOT%\installed\x64-windows\bin\glfw3.dll" "Release&quot; >nul 2>&1
copy "%VCPKG_ROOT%\installed\x64-windows\bin\glew32.dll" "Release&quot; >nul 2>&1
copy "%VCPKG_ROOT%\installed\x64-windows\bin\OpenAL32.dll" "Release&quot; >nul 2>&1

echo.
echo [INFO] Build complete! To run Enuanza:
echo   cd %cd%\Release
echo   Enuanza.exe
echo.
echo [INFO] For VR support, ensure SteamVR is installed and running.
echo ================================================
pause