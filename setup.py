import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

def check_command(cmd, version_flag="--version"):
    try:
        subprocess.run([cmd, version_flag], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception:
        return False

def run(cmd, shell=False):
    subprocess.run(cmd, check=True, shell=shell)

def main():
    print("🚀 Shodan Mapper Setup (with timestamped output folder)")

    # ----------------------------
    # Detect OS
    # ----------------------------
platform = sys.platform
print(f"🔹 Detected platform: {platform}")

    # ----------------------------
    # Check Python
    # ----------------------------
if not check_command("python") and not check_command("python3"):
        print("❌ Python is not installed! Please install Python 3.x first.")
        sys.exit(1)
else:
    python_cmd = "python3" if check_command("python3") else "python"
    version = subprocess.run([python_cmd, "--version"], capture_output=True, text=True).stdout.strip()
    print(f"✅ Python found: {version}")

    # ----------------------------
    # Check pip
    # ----------------------------
if not check_command("pip") and not check_command("pip3"):
    print("❌ pip is not installed! Please install pip.")
    sys.exit(1)
else:
    pip_cmd = "pip3" if check_command("pip3") else "pip"
    version = subprocess.run([pip_cmd, "--version"], capture_output=True, text=True).stdout.strip()
    print(f"✅ pip found: {version}")

    # ----------------------------
    # Check venv availability
    # ----------------------------
try:
        run([python_cmd, "-m", "venv", "--help"])
        print("✅ venv module available")
except Exception:
        print("❌ venv module not available. Install it (e.g., sudo apt install python3-venv)")
        sys.exit(1)

    # ----------------------------
    # Create virtual environment
    # ----------------------------
venv_dir = Path("venv")
if not venv_dir.exists():
    print("📦 Creating virtual environment...")
    run([python_cmd, "-m", "venv", "venv"])
else:
    print("✅ Virtual environment already exists.")

    # ----------------------------
    # Activate venv
    # ----------------------------
activate_cmd = venv_dir / ("Scripts" if platform.startswith("win") else "bin") / "activate"
print(f"⚠️ To activate manually: {activate_cmd}")

# ----------------------------
# Upgrade pip
# ----------------------------
print("🔹 Upgrading pip...")
run([str(venv_dir / ("Scripts" if platform.startswith("win") else "bin") / "python"),
     "-m", "pip", "install", "--upgrade", "pip"])

# ----------------------------
# Install dependencies from requirements.txt
# ----------------------------
req_file = Path("requirements.txt")
if not req_file.exists():
    print("❌ requirements.txt not found! Please create it with your project dependencies.")
    sys.exit(1)

print(f"📦 Installing dependencies from {req_file} ...")
run([str(venv_dir / ("Scripts" if platform.startswith("win") else "bin") / "python"),
     "-m", "pip", "install", "-r", str(req_file)])

# ----------------------------
# VSCode integration
# ----------------------------
vscode_dir = Path(".vscode")
vscode_dir.mkdir(exist_ok=True)
settings_file = vscode_dir / "settings.json"

settings_content = f"""
{{
  "python.defaultInterpreterPath": "{venv_dir / ('Scripts' if platform.startswith('win') else 'bin') / 'python'}",
  "python.analysis.extraPaths": ["{venv_dir / ('Lib' if platform.startswith('win') else 'lib') / f'python{sys.version_info.major}.{sys.version_info.minor}' / 'site-packages'}"]
}}
"""
settings_file.write_text(settings_content)
print(f"✅ VSCode configured to use virtual environment: {settings_file}")

# ----------------------------
# Create timestamped output folder
# ----------------------------
base_output_dir = Path("reports")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = base_output_dir / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
print(f"📂 Output folder created for reports: {output_dir}")

# ----------------------------
# API Key instructions
# ----------------------------
print("\n✅ Setup completed!")
print("👉 Please set your Shodan API Key before running the project:")
print("   - Option 1: export SHODAN_API_KEY='YOUR_API_KEY'  (Linux/macOS/WSL)")
print("   - Option 2: setx SHODAN_API_KEY 'YOUR_API_KEY'   (Windows CMD)")
print("   - Option 3: Add SHODAN_API_KEY=YOUR_API_KEY to a .env file in project root")

print("\nYou can now activate the virtual environment and run the project:")
print(f"   source {activate_cmd}  (Linux/macOS/WSL)")
print(f"   {activate_cmd}         (Windows)")
print(f"\nReports will be saved automatically in: {output_dir}")
print("   Example usage: python main.py --output_dir", output_dir)

if __name__ == "__main__":
    main()
