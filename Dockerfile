FROM python:3.11.7

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]