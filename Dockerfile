FROM python:3.8-slim

WORKDIR /bot

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
RUN mkdir -p ./cogs/calendar/Assets ./cogs/tgg

COPY . /bot

CMD ["python", "main.py"]
