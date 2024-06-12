import sys
import subprocess
import os
from setuptools import setup, find_packages

# Package meta-data
NAME = "dbt_project"
VERSION = "1.0.1"
DESCRIPTION = "DBT project for beginners"
REQUIRES_PYTHON = ">=3.11.0"


# Packages required for the module
def list_reqs(filename="requirements.txt"):
    with open(filename) as f:
        return f.read().splitlines()


def create_virtualenv():
    platform = sys.platform
    if platform == "win32":  # Windows
        #subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        subprocess.check_call(["python", "-m", "venv", "venv"])
        activate_script = os.path.join("venv", "Scripts", "activate.bat")
        # Activation de l'environnement virtuel
        subprocess.call(activate_script, shell=True)
    elif platform == "linux" or platform == "linux2":  # Linux
        # Uncomment the following lines to apply them for Linux
        # subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        # activate_script = os.path.join("venv", "bin", "activate")
        # subprocess.call(f"source {activate_script}", shell=True)
        pass
    else:
        raise OSError("Unsupported OS")

def install_requirements():
    # Utilisation de --user pour éviter les problèmes de permissions
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "-r", "requirements.txt"])


if __name__ == "__main__":
    # Create and activate the virtual environment
    create_virtualenv()
    
    # Install required packages inside the virtual environment
    install_requirements()

    # Setup configuration
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        python_requires=REQUIRES_PYTHON,
        packages=find_packages(exclude=("tests",)),
        install_requires=list_reqs(),
    )
