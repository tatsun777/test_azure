# frontend/Dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install streamlit requests

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
