FROM python:3.12.0

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]