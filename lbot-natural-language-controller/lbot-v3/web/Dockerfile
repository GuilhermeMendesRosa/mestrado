FROM python:3.10-slim

WORKDIR /app

# Copia arquivos necessários para a API
COPY lbot_api.py .
COPY lbot_translator.pt .
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "lbot_api:app", "--host", "0.0.0.0", "--port", "8000"]
