FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev


CMD ["python", "main.py"]
