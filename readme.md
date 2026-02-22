# RoadBuddy

Privacy-first parking notification app. Vehicle owners generate a QR sticker; anyone can scan and send a ping (Blocked / Wrong parking / Emergency). Owner receives an in-app notification.

## Repo structure
- `backend/` FastAPI + SQLAlchemy + Alembic
- `frontend/` Next.js (App Router) + shadcn/ui

## Local dev

### Backend
1. `cd backend`
2. Create `.env` from `.env.example`
3. Install + run:
   - `python -m venv .venv && source .venv/bin/activate` (or Windows equivalent)
   - `pip install -r requirements.txt`
   - `alembic upgrade head`
   - `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

### Frontend
1. `cd frontend`
2. Create `.env.local` from `.env.example`
3. `npm install`
4. `npm run dev`

## Deployment
(Coming soon)