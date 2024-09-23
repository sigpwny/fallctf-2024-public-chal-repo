FROM ubuntu:20.04

ENV FLAG "fallctf{a3s_CBC_g0t_m3_fl1pp1n_oU7}"
ENV KEY "THIS IS A SECRET"

RUN apt-get update && apt-get install -y socat build-essential python3 python3-pip

RUN mkdir /chal
WORKDIR /chal
COPY chal.py /chal
COPY requirements.txt /chal

RUN chmod 555 chal.py
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

RUN adduser --disabled-login chalhost
USER chalhost

CMD socat TCP-LISTEN:1337,fork,reuseaddr EXEC:"python3 chal.py"