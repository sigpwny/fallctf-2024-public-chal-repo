FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip

WORKDIR /app

COPY startup.sh main.py requirements.txt /app/
RUN python3 -m pip install -r requirements.txt && playwright install && playwright install-deps

COPY internal-service /app/internal-service
COPY static /app/static
RUN chmod +x /app/startup.sh

EXPOSE 1337

CMD /app/startup.sh