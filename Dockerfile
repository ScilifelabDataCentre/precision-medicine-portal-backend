FROM python:3.13.0a3

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]