# Comparação de textos em PDF — v1.0

Aplicação para comparar dois PDFs com texto extraível. A interface React envia os documentos à API FastAPI, que combina similaridade lexical (40%) e semântica (60%) e retorna percentuais, trechos semelhantes, palavras-chave e indícios de duplicação ou paráfrase.

## Estrutura

- `backend/app/`: API, extração dos PDFs e serviços de comparação.
- `backend/requirements.txt`: dependências Python.
- `frontend/src/`: interface de upload e apresentação dos resultados.
- `frontend/package.json` e `frontend/package-lock.json`: dependências e comandos do frontend.

O repositório contém os arquivos da aplicação e este README. Dependências instaladas, ambientes virtuais, testes, documentação complementar e arquivos gerados ficam fora do versionamento, conforme o `.gitignore`.

## Execução local

Pré-requisitos: Python com suporte às dependências de `backend/requirements.txt`, Node.js e npm compatíveis com o Vite instalado. O projeto não declara versões mínimas dos ambientes em seus próprios manifestos.

Em um terminal PowerShell, a partir da raiz:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Em outro terminal, a partir da raiz:

```powershell
cd frontend
npm ci
npm run dev
```

Abra a interface em `http://localhost:5173`. A API usa `http://localhost:8000`, com documentação interativa em `/docs` e verificação de disponibilidade em `/health`.

**Ambiente encontrado em 29/10/2026:** o ambiente virtual copiado em `backend/.venv` aponta para um Python inexistente de outro perfil do Windows. Recrie esse ambiente com um Python local funcional antes de executar o backend. Na inspeção, `node` e `npm` também não estavam disponíveis no PATH do terminal. Os testes e a compilação não puderam ser executados nessa inspeção.
