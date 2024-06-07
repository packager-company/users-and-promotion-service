# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación Flask al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación Flask está escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
