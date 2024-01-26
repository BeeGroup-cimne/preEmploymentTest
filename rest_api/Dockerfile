FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY electricity.db /app/electricity.db
COPY main.py /app/main.py

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]