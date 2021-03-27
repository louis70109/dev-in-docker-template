
FROM python:3.6-alpine

WORKDIR /app
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt --user

ADD . /app

EXPOSE 5000
CMD ["python", "api.py"]