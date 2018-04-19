FROM python:3.6-alpine3.7

ENV HOSTNAME=www.yahoo.com

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY healthcheck.py ./

CMD ["gunicorn", "-b", "0.0.0.0",  "healthcheck:api"]

EXPOSE 8000
