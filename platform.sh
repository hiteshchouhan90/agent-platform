#!/usr/bin/env bash
set -euo pipefail

echo "Checking Homebrew..."
if ! command -v brew >/dev/null 2>&1; then
  echo "Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  if [ -f /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  elif [ -f /usr/local/bin/brew ]; then
    eval "$(/usr/local/bin/brew shellenv)"
  fi
fi

echo "Updating Homebrew..."
brew update

echo "Installing latest Python..."
brew install python

echo "Creating virtual environment..."
mkdir -p "$HOME/venvs"
PYTHON_BIN="$(brew --prefix)/bin/python3"
"$PYTHON_BIN" -m venv "$HOME/venvs/agent-platform"

echo "Installing packages..."
source "$HOME/venvs/agent-platform/bin/activate"
python -m pip install --upgrade pip
python -m pip install "fastapi[standard]" uvicorn

echo
echo "Done!"
echo "Activate it with:"
echo "  source ~/venvs/agent-platform/bin/activate"
echo "Use this interpreter in VS Code:"
echo "  ~/venvs/agent-platform/bin/python"