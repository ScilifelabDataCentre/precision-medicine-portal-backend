FROM python:3.13.0a1

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]