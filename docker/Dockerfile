FROM python:3.9

WORKDIR /app

COPY requirements.txt .
#poetry
RUN pip install -r requirements.txt

COPY . .

# Phishing.py dosyasını kopyala

COPY phishing.py .
#COPY api.py .


CMD ["sh", "-c", "python phishing.py & uvicorn api:app --host 0.0.0.0 --port 8000"]