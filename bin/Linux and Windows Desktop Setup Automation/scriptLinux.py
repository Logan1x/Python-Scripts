#In development

import subprocess
import sys

def autom_sudoapt(command):
    try:
        subprocess.run(command, check=True, text=True, shell=True)
        print(f"Comando '{command}' executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando '{command}': {e}", file=sys.stderr)
        sys.exit(1)

def main():
    print("Iniciando a atualização e instalação do htop, vscode e git...")

    autom_sudoapt("sudo apt update -y")
    
    autom_sudoapt("sudo apt upgrade -y")

    autom_sudoapt("sudo apt install -y htop")

    autom_sudoapt("sudo apt install -y git")

    autom_sudoapt("sudo snap install -y --classic code")
    
    autom_sudoapt("sudo apt install neofetch -y")
    
    autom_sudoapt("sudo apt install gnome-tweaks -y")
    
    autom_sudoapt("sudo apt install gnome-shell-extensions -y")
    
    autom_sudoapt("sudo apt install gnome-terminal -y")
    
    print("Atualização e instalação concluídos!")

if __name__ == "__main__":
    main()