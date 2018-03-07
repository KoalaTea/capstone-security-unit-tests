FROM python:3

WORKDIR /app

RUN mkdir /app/exampleapp
COPY run.py /app
COPY config.py /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY exampleapp /app/exampleapp

CMD ["python3", "-u", "/app/run.py"]
