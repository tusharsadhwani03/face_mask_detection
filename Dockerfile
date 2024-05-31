FROM python:3.11.7

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "detect.py"]