# Farha Installation Guide

## Bismillah ir-Rahman ir-Raheem

### Prerequisites:
```bash
# Install required packages on Ubuntu/Debian:
sudo apt update
sudo apt install build-essential cmake

# On CentOS/RHEL:
sudo yum install gcc-c++ cmake

# On Fedora:
sudo dnf install gcc-c++ cmake
```

### Installation Steps:

#### For Version 1 (Basic):
```bash
cd Version1_Basic
chmod +x build_farha.sh
./build_farha.sh
cd build
./farha_game
```

#### For Version 2 (Enhanced):
```bash
cd Version2_Enhanced
chmod +x build_enhanced.sh
./build_enhanced.sh
cd build_enhanced
./farha_enhanced
```

#### For Version 3 (Allah Inspired):
```bash
cd Version3_AllahInspired
chmod +x build_allah_inspired.sh
./build_allah_inspired.sh
cd build_allah_inspired
./farha_v3
```

### Troubleshooting:

#### Build Errors:
- Ensure C++ compiler is installed
- Check CMake version (minimum 3.10)
- Verify build scripts have execute permissions

#### Runtime Issues:
- Check if executable was created successfully
- Run from the correct build directory
- Verify all files are present

### Clean Build:
```bash
# Remove build directory and rebuild:
rm -rf build
./build_script.sh
```

### System Compatibility:
- ✅ Linux (Ubuntu, Debian, CentOS, Fedora)
- ✅ macOS (with Xcode Command Line Tools)
- ⚠️ Windows (requires WSL or MinGW)

May Allah make your installation successful!