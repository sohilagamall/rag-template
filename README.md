# rag-template

Reusable RAG template for FastAPI projects: text extraction, chunking, embedding, and hybrid search.

**Stack:** FastAPI · SQLAlchemy 2.0 · Alembic · PostgreSQL 18 + pgvector · Pydantic v2 · uv · Python 3.12

## Quick start

```bash
docker compose up -d          # Postgres 18 + pgvector on :5435
uv sync
cp .env.example .env          # set database_url
uv run fastapi dev src/rag_template/main.py
```

## Structure

```
src/rag_template/
├── main.py            # FastAPI app
├── core/              # config, db
├── parsers/           # html, pdf, docx, youtube, text
├── chunking/          # token-based splitter
├── providers/         # embedding providers
├── features/          # sources, search
└── jobs/              # background ingest
alembic/  tests/  docker-compose.yml
```

## Config

| Variable | Example |
|---|---|
| `database_url` | `postgresql+psycopg://postgres:postgres@localhost:5435/rag_template` |

## Commands

```bash
docker compose up -d
uv run pytest
uv run alembic upgrade head
```

## Starting the project (every time)

```bash
cd ~/Documents/projects/rag-template

# 1. Start the database (Postgres 18 + pgvector on :5435)
docker compose up -d
sleep 5                      # wait for Postgres to finish initializing

# 2. Verify it's up (optional)
docker compose ps

# 3. Run the app / tests / migrations
uv run fastapi dev src/rag_template/main.py
uv run pytest
uv run alembic upgrade head
```

**Stop when done:**

```bash
docker compose down          # stops DB, keeps data in ./pgdata
```

**Full wipe and start fresh:**

```bash
docker compose down -v
sudo rm -rf pgdata
docker compose up -d
```
