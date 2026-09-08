# Imagem base 
FROM python:3.12-slim

WORKDIR /app

# Copia as dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . .

# Expõe a porta 5000 para acesso web
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]