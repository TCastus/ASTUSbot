FROM python:3.9-slim

WORKDIR /bot

RUN apt-get update \
    && apt-get upgrade gcc -y \
    && apt-get upgrade libseccomp2 -y \
    && pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt



COPY . .

RUN mkdir -p ./cogs/calendar/Assets


CMD ["python", "main.py"]
