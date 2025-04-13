# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto donde correrá el servidor de Django
EXPOSE 8000

# Comando por defecto para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
