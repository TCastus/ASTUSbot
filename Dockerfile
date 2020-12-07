FROM python:3.8-slim

WORKDIR /bot

COPY . .

RUN apt-get update \
    && apt-get upgrade gcc -y \
    && pip install --upgrade pip\
    && pip install -r requirements.txt\
    && rm requirements.txt\
    && mkdir -p ./cogs/calendar/Assets

CMD ["python", "main.py"]
