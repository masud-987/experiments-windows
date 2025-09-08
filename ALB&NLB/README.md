# ALB & NLB Demo

Minimal backend (FastAPI) + frontend (HTML/JS).

## Backend (Flask)

Requirements are in `backend/requirements.txt`.

### Setup (Windows PowerShell)

```powershell
cd backend
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Then test endpoints:

- Health: `http://localhost:8000/api/health`

## Frontend

Open `frontend/index.html` in your browser. It calls the backend `GET /api/greet/{name}`.

If you host the frontend elsewhere, set `apiBase` to your API origin.

## Notes

- CORS is enabled for all origins for demo simplicity.
- Adjust as needed for production.

## Tests

Install pytest and run from the repo root:

```powershell
pip install -r requirements-test.txt
pytest -q
```

Flask app with sessions is now in `backend/main.py`:

- `GET /` home shows login status
- `POST /login` with form field `username` sets session
- `GET /logout` clears session and redirects to home
