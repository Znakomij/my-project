FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

RUN pip install .

CMD ["python", "src/my_package/main.py"]