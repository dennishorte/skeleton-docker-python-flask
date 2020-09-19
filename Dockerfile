FROM python:3.8
MAINTAINER Dennis Horte "dennis.horte@gmail.com"

COPY app /app
COPY requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
