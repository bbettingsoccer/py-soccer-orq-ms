# Pull de la imagen base oficial
FROM python:3.11-slim


# setup del directorio de trabajo
WORKDIR /app

# Configuración de las variables de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000:8000/tcp
ENTRYPOINT python3 main.py