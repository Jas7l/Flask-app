FROM python:3.11-slim

WORKDIR /app/backend

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/backend

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . /app/backend

EXPOSE 5000

CMD ["python", "-m", "backend.main"]