FROM python:3.11.4-slim-buster

# Directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Punto de entrada del contenedor
CMD ["python", "src/main.py"]
