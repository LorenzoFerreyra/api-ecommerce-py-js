FROM python:3.12
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY ./services/user /app
CMD ["fastapi", "dev", "--host", "0.0.0.0", "--port", "8003"]