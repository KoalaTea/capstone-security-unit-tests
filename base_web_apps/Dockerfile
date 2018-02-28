FROM ubuntu:16.04
ADD . /exampleapp
WORKDIR /exampleapp
RUN apt-get update -y && apt-get install build-essential python3
COPY ./* /exampleapp
RUN python3 -r /exampleapp/requirements.txt
CMD ["python3 /exampleapp/run.py"]
