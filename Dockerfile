FROM python:3.5

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r /requirements.txt

EXPOSE 8000
