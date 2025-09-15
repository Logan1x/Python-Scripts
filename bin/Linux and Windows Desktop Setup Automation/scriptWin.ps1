#In development

# Check for administrator privileges
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "This script needs to be run as an Administrator. Restarting with elevated privileges..."
    Start-Process powershell "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Function to display the menu
function Show-Menu {
    Clear-Host
    Write-Host "------------------------------------------------------" -ForegroundColor Cyan
    Write-Host "Script for Windows optimization with a focus on games " -ForegroundColor White
    write-Host "            Developed by euopaulin                      " -ForegroundColor White
    Write-Host "------------------------------------------------------" -ForegroundColor Cyan
    Write-Host "            Choose an option:" -ForegroundColor White
    Write-Host "------------------------------------------------------" -ForegroundColor Cyan
    Write-Host "1.  Run SFC/SCANNOW" -ForegroundColor DarkRed
    Write-Host "2.  Run CHKDSK" -ForegroundColor DarkRed
    Write-Host "3.  Clean temporary files" -ForegroundColor DarkRed
    Write-Host "4.  Restore system image (DISM)" -ForegroundColor DarkRed
    Write-Host "5.  Exit" -ForegroundColor DarkGreen
    Write-Host "------------------------------------------------------" -ForegroundColor Cyan
}

# Main loop to show the menu and process user input
while ($true) {
    Show-Menu

    $choice = Read-Host "Enter the number of your choice"

    switch ($choice) {
        "1" {
            Write-Host "Option 1 selected: Running SFC/SCANNOW..." -ForegroundColor Yellow
            try {
                & sfc /scannow
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "SFC/SCANNOW executed successfully." -ForegroundColor Green
                } else {
                    Write-Host "Error running SFC/SCANNOW. Make sure to run the script as an Administrator." -ForegroundColor Red
                }
            } catch {
                Write-Host "An error occurred while running the command." -ForegroundColor Red
            }
            break
        }
        "2" {
            Write-Host "Option 2 selected: Running CHKDSK..." -ForegroundColor Yellow
            $drive = Read-Host "Enter the drive letter (e.g., C)"
            Write-Host "Checking drive $drive..." -ForegroundColor Yellow
            try {
                # Using the native PowerShell command
                Repair-Volume -DriveLetter $drive -Scan -Verbose
                Write-Host "CHKDSK executed successfully." -ForegroundColor Green
            } catch {
                Write-Host "An error occurred while running the command." -ForegroundColor Red
            }
            break
        }
        "3" {
            Write-Host "Option 3 selected: Cleaning temporary files..." -ForegroundColor Yellow
            try {
                $tempPaths = "$env:TEMP\*", "$env:SystemRoot\Temp\*"
                foreach ($tempPath in $tempPaths) {
                    if (Test-Path $tempPath) {
                        Remove-Item -Path $tempPath -Recurse -Force -ErrorAction SilentlyContinue
                    }
                }
                Write-Host "Temporary files cleaned successfully." -ForegroundColor Green
            } catch {
                Write-Host "An error occurred while cleaning temporary files." -ForegroundColor Red
            }
            break
        }
        "4" {
            Write-Host "Option 4 selected: Restoring system image (DISM)..." -ForegroundColor Yellow
            try {
                & dism /Online /Cleanup-Image /RestoreHealth
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "DISM executed successfully." -ForegroundColor Green
                } else {
                    Write-Host "Error running DISM. Make sure to run the script as an Administrator." -ForegroundColor Red
                }
            } catch {
                Write-Host "An error occurred while running the command." -ForegroundColor Red
            }
            break
        }
        "5" {
            Write-Host "Exiting the script. Goodbye!" -ForegroundColor Red
            Start-Sleep -Seconds 2
            exit
        }
        default {
            Write-Host "Invalid option. Please enter a number from 1 to 5." -ForegroundColor Red
            break
        }
    }
    
    Write-Host ""
    Write-Host "Press any key to continue..." -ForegroundColor White
    $null = [System.Console]::ReadKey($true)
}