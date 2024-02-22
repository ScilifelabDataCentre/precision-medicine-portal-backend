FROM python:3.13.0a4

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]