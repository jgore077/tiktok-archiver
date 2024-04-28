# escape=`
FROM ubuntu:latest
LABEL Name=tiktokarchiver Version=1.0.0
ENV IDENTIFIER=
ENV USER=
ENV IA_USERNAME=
ENV IA_PASSWORD=
ENV SUBJECT=
ENV CREATOR=
ENV DESCRIPTION=
WORKDIR /app
COPY deps.txt .
COPY requirements.txt .
COPY invoke.py .
RUN apt-get -y update && apt-get -y install $(cat deps.txt)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | sh - 
RUN apt-get install -y nodejs
RUN git init && git remote add origin https://github.com/jgore077/tiktok-downloader && git pull --depth=1 origin docker
RUN python3.12 -m venv .venv && . .venv/bin/activate
RUN .venv/bin/pip3 install -r requirements.txt && npm ci
CMD .venv/bin/python3 invoke.py -i ${IDENTIFIER} -d downloads/@${USER} -m ${USER}
