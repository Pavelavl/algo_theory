# Этап 1: тестирование
FROM tiangolo/uvicorn-gunicorn:python3.10-slim AS test
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/data /app/reports && \
    python -c "import sqlite3; conn = sqlite3.connect('/app/data/library_test.db'); conn.executescript(open('/app/migrations.sql').read()); conn.close()"
ENV DATABASE_PATH="/app/data/library_test.db"
RUN pytest --disable-warnings --maxfail=1

# Этап 2: приложение
FROM tiangolo/uvicorn-gunicorn:python3.10-slim AS app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DATABASE_PATH="/app/data/library.db"
RUN mkdir -p /app/data /app/reports
EXPOSE 8081
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
