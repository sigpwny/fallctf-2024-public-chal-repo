FROM node AS build

WORKDIR /app

COPY package*.json .

RUN npm ci

COPY . .

RUN npx prisma generate

RUN npm run build
RUN npm prune --production

FROM node AS run

ENV NODE_ENV=production

WORKDIR /app
COPY --from=build /app/build ./build
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/prisma ./prisma

RUN ulimit -c unlimited

ENV FLAG="fallctf{google_tsa_sql_injection_2024}"
ENV PORT=1337
ENV DATABASE_URL="file:./dev.db"

CMD ["sh", "-c", "npx prisma migrate dev && node build"]