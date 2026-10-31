# Projeto-Lab-CD

Aplicação web em Python com Flask.

## Estrutura

```
app.py              Ponto de entrada e rotas
src/                Configuração e módulos de dados e gráficos
templates/          Páginas HTML (Jinja2)
static/             CSS e outros arquivos estáticos
dados/              Arquivos de dados
```

## Como executar

No PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

A aplicação fica disponível em http://127.0.0.1:5000.
