FROM python:3.8-slim

WORKDIR /app

# Copy the backend code
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "app.main"]
