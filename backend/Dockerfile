# backend/Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app
WORKDIR /app

# FastAPIアプリを直接指定して起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
