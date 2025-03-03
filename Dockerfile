FROM python:3.9-alpine

WORKDIR /app

COPY script.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .

RUN mkdir -p output

CMD ["python", "script.py"]