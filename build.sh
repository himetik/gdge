#!/bin/bash

python -m venv .venv
source .venv/bin/activate

curl -LsSf https://astral.sh/uv/install.sh | sh

export PATH="$HOME/.local/bin:$PATH"

which uv

uv pip install .
