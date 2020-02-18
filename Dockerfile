FROM python:3.5


COPY requirements.txt /opt/flasky_app/requirements.txt

WORKDIR /opt/flasky_app

RUN pip3 install --no-cache-dir -r requirements.txt

#COPY . /opt/flasky_app

EXPOSE 5000
