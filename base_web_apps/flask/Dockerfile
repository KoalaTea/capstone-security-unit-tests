FROM ubuntu:16.04

WORKDIR /exampleapp

COPY requirements.txt /exampleapp
RUN apt-get update -y \
    && apt-get install python3 -y \
    && rm -rf /var/lib/apt/lists/*
COPY exampleapp /exampleapp
RUN python3 -r /exampleapp/requirements.txt
EXPOSE 5000

CMD ["python3" "/exampleapp/run.py"]
