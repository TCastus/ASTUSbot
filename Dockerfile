FROM python:3.8-slim

WORKDIR /bot
ENV BOT_TOKEN={the bot TOKEN} \
    IPINFO_TOKEN={the ipinfo token}

COPY ./requirements.txt .
RUN pip install -r requirements.txt &&\
    mkdir -p ./cogs/calendar/Assets

COPY ./cogs/calendar/*.py ./cogs/calendar/
COPY ./cogs/*.py ./cogs/
COPY ./*.py ./

RUN ["python", "main.py"]