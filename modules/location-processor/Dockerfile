FROM python:3.7-alpine

WORKDIR .

COPY ./modules/location-processor/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY ./modules/location-processor/ .
CMD ["python", "consumer.py"]