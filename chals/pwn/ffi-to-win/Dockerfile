FROM oven/bun:debian@sha256:c829f8ea23c2703e163f2122f11d2a9329f51abb395af3878a57bb5654f60990

RUN apt-get update && apt-get install -y socat

WORKDIR /home/user
COPY src ./

RUN bun install

ENV FLAG fallctf{who_knew_about_c_functions_in_typescript_c1456cae}

CMD socat -T60 TCP-LISTEN:1337,fork,reuseaddr EXEC:"bun run index.ts"