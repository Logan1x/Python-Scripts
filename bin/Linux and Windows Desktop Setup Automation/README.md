# 🛠️ In Development

This repository contains a collection of **automation and optimization scripts**, aiming to improve the **development environment on Linux** and **gaming performance on Windows**.  

---

## 🐧 Linux Automation Scripts

The Python script **`automation_script.py`** is designed to streamline the setup of a new development environment on Linux.  
It automates the installation of essential tools, ensuring everything is ready to get you started quickly.  

### Linux Script Features
- **System Updates**: Runs `apt update` and `apt upgrade` to keep packages up to date.  
- **Essential Tools**: Automatically installs `htop` (process monitor), `Git` (version control), and `Neofetch` (system information).  
- **Development Environment**: Installs **Visual Studio Code** via Snap.  
- **Customization**: Includes `GNOME Tweaks` and `GNOME Shell Extensions` to customize the user interface.  

---

## 🎮 Windows Optimization Scripts

The PowerShell script **`windows_gaming_tweaks.ps1`** is an interactive tool for optimizing Windows and boosting gaming performance.  
It provides a simple, straightforward menu to run system maintenance and repair tasks.  

### 💻 Windows Script Features
- **SFC/SCANNOW**: Scans and repairs corrupted system files.  
- **CHKDSK**: Analyzes and fixes disk errors to maintain data integrity.  
- **Temporary File Cleanup**: Removes unnecessary files that take up space and slow down the system.  
- **DISM**: Repairs the operating system image, ensuring updates work properly.  

---

## How to Use

### 🔹 On Linux
1. Clone the repository:  
   ```bash
   git clone https://github.com/Logan1x/Python-Scripts.gitgit
   ```

2. Enter the repository directory:
   ```bash
   cd Python-Scripts
   ```

3. Execute the script:
   ```bash
   python3 automation_script.py
   ```

### 🔹 On Windows

1. Open PowerShell as Administrator. To do this, right-click the Start Menu icon and select `Windows PowerShell (Admin)` or `Terminal (Admin)`.

2. Navigate to the directory where the script is saved:
   ```bash
   cd C:\path\to\repository
   ```

3. Execute the script:
   ```bash
   .\windows_gaming_tweaks.ps1
   ```

Note: If the script doesn't run, you might need to adjust the PowerShell execution policy. Use the command `Set-ExecutionPolicy RemoteSigned` (run as Administrator) to allow local scripts to execute.