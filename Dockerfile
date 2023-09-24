FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /batima
COPY requirements.txt /batima/
RUN apt-get update && \
    apt-get install -y nano && \
    pip install -r requirements.txt
COPY . /batima/
