#!/usr/bin/env python3
"""
Installation script for The Falcon Press Office
Installs all required dependencies with fallbacks for optional components
"""

import subprocess
import sys
import importlib
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    
    print(f"✅ Python version: {sys.version}")
    return True

def install_package(package, import_name=None):
    """Install a package using pip"""
    if import_name is None:
        import_name = package.split('>=')[0].split('==')[0]
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package} already installed")
        return True
    except ImportError:
        print(f"📦 Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False

def install_core_dependencies():
    """Install core required dependencies"""
    print("\n🔧 Installing core dependencies...")
    
    core_packages = [
        ("numpy>=1.24.0", "numpy"),
        ("pandas>=2.0.0", "pandas"),
        ("matplotlib>=3.7.0", "matplotlib"),
        ("seaborn>=0.12.0", "seaborn"),
        ("scikit-learn>=1.3.0", "sklearn"),
        ("plotly>=5.15.0", "plotly"),
        ("networkx>=3.1.0", "networkx"),
        ("requests>=2.31.0", "requests"),
        ("beautifulsoup4>=4.12.0", "bs4"),
        ("lxml>=4.9.0", "lxml"),
        ("python-dateutil>=2.8.0", "dateutil"),
        ("urllib3>=2.0.0", "urllib3"),
        ("certifi>=2023.7.0", "certifi")
    ]
    
    failed_packages = []
    
    for package, import_name in core_packages:
        if not install_package(package, import_name):
            failed_packages.append(package)
    
    return failed_packages

def install_optional_dependencies():
    """Install optional dependencies with graceful fallback"""
    print("\n🔧 Installing optional dependencies...")
    
    optional_packages = [
        ("transformers>=4.30.0", "transformers", "AI/ML capabilities"),
        ("torch>=2.0.0", "torch", "Deep learning framework"),
        ("spacy>=3.6.0", "spacy", "Advanced NLP"),
        ("nltk>=3.8.0", "nltk", "Natural language processing")
    ]
    
    failed_optional = []
    
    for package, import_name, description in optional_packages:
        try:
            if install_package(package, import_name):
                print(f"✅ {description} enabled")
            else:
                print(f"⚠️  {description} not available (will use fallbacks)")
                failed_optional.append(package)
        except Exception as e:
            print(f"⚠️  {description} not available (will use fallbacks): {e}")
            failed_optional.append(package)
    
    return failed_optional

def setup_gui():
    """Check and setup GUI components"""
    print("\n🖥️  Checking GUI components...")
    
    try:
        import tkinter
        print("✅ tkinter available")
    except ImportError:
        print("❌ tkinter not available - GUI will not work")
        print("On Ubuntu/Debian: sudo apt-get install python3-tk")
        return False
    
    return True

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    
    directories = [
        "data",
        "libraries", 
        "exports",
        "logs",
        "cache"
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Created {directory}/ directory")
        except Exception as e:
            print(f"❌ Failed to create {directory}/: {e}")
    
    return True

def verify_installation():
    """Verify that all components are working"""
    print("\n🧪 Verifying installation...")
    
    # Test imports
    test_imports = [
        ("numpy", "np"),
        ("pandas", "pd"),
        ("matplotlib.pyplot", "plt"),
        ("plotly.graph_objects", "go"),
        ("requests", "requests"),
        ("bs4", "bs4"),
        ("sklearn", "sklearn")
    ]
    
    failed_imports = []
    
    for module_name, alias in test_imports:
        try:
            importlib.import_module(module_name)
            print(f"✅ {module_name} imported successfully")
        except ImportError as e:
            print(f"❌ Failed to import {module_name}: {e}")
            failed_imports.append(module_name)
    
    return len(failed_imports) == 0

def create_startup_script():
    """Create startup script"""
    print("\n📜 Creating startup script...")
    
    startup_script = """#!/bin/bash
# The Falcon Press Office Startup Script

echo "🚀 Starting The Falcon Press Office..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Check if required files exist
if [ ! -f "falcon_press_office.py" ]; then
    echo "❌ falcon_press_office.py not found"
    exit 1
fi

# Start the application
echo "🎯 Launching The Falcon Press Office..."
python3 falcon_press_office.py
"""
    
    with open("start_falcon.sh", "w") as f:
        f.write(startup_script)
    
    # Make executable on Unix systems
    try:
        os.chmod("start_falcon.sh", 0o755)
        print("✅ Created start_falcon.sh (Unix/Linux)")
    except:
        print("⚠️  Could not make start_falcon.sh executable")
    
    # Create Windows batch file
    windows_script = """@echo off
echo 🚀 Starting The Falcon Press Office...

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "falcon_press_office.py" (
    echo ❌ falcon_press_office.py not found
    pause
    exit /b 1
)

echo 🎯 Launching The Falcon Press Office...
python falcon_press_office.py
pause
"""
    
    with open("start_falcon.bat", "w") as f:
        f.write(windows_script)
    
    print("✅ Created start_falcon.bat (Windows)")

def main():
    """Main installation process"""
    print("🎯 The Falcon Press Office - Installation Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    failed_core = install_core_dependencies()
    failed_optional = install_optional_dependencies()
    
    # Setup GUI
    if not setup_gui():
        print("⚠️  GUI components missing - application may not work properly")
    
    # Create directories
    create_directories()
    
    # Verify installation
    if not verify_installation():
        print("\n❌ Some components failed to install")
        if failed_core:
            print(f"Core packages that failed: {', '.join(failed_core)}")
    else:
        print("\n✅ All core components installed successfully")
    
    # Create startup scripts
    create_startup_script()
    
    # Installation summary
    print("\n" + "=" * 50)
    print("📊 Installation Summary")
    print("=" * 50)
    
    if failed_core:
        print(f"❌ Core packages failed: {len(failed_core)}")
        for pkg in failed_core:
            print(f"   - {pkg}")
    
    if failed_optional:
        print(f"⚠️  Optional packages not installed: {len(failed_optional)}")
        print("   (The application will use fallback methods)")
    
    if not failed_core:
        print("\n✅ Installation completed successfully!")
        print("\n🚀 To start The Falcon Press Office:")
        print("   Unix/Linux: ./start_falcon.sh")
        print("   Windows: start_falcon.bat")
        print("   Or directly: python3 falcon_press_office.py")
    else:
        print("\n❌ Installation incomplete - please resolve failed packages")
        print("You can try installing manually: pip install -r requirements.txt")
    
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main()