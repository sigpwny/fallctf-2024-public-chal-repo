# This Dockerfile should NOT be provided.
# Users must figure out how to run the binary on their own.
FROM s390x/ubuntu

RUN apt update && apt install -y gcc make git

WORKDIR /chal

COPY main.c Makefile ./

RUN make

# docker cp CONTAINER:/chal/works-on-my-machine .