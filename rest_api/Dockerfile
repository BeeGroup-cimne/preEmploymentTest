FROM python:3.9.10-alpine3.14
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask
COPY . /srv
ENV FLASK_APP=app
ENV FLASK_ENV='development'
CMD ["python","app.py"]