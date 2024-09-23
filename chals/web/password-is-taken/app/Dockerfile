FROM node AS build

WORKDIR /app

COPY package*.json .

RUN npm ci

COPY . .

RUN npm run prisma-generate

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

ENV DATABASE_URL="postgresql://postgres:password@password-is-taken-db:5432/mydb?schema=public"
ENV FLAG="fallctf{never_reuse_passwords}"
ENV PORT=1337

CMD ["sh", "-c", "npx prisma migrate dev && node build"]
