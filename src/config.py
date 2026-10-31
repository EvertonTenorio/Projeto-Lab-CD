"""Configurações e caminhos do projeto."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"

# Em produção, defina a variável de ambiente SECRET_KEY.
SECRET_KEY = os.environ.get("SECRET_KEY", "chave-de-desenvolvimento")
