FROM tiangolo/uvicorn-gunicorn:python3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/data
EXPOSE 8000
CMD sh -c "pytest --maxfail=1 --disable-warnings && uvicorn app.main:app --host 0.0.0.0 --port 8000"
