FROM python:3.12-slim
WORKDIR /app

COPY libraries.txt .
RUN pip install --no-cache-dir -r libraries.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]