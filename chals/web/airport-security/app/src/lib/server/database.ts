import { PrismaClient } from "@prisma/client";

const globalForPrisma = globalThis as unknown as { db: PrismaClient };

export const db = globalForPrisma.db || new PrismaClient();

if (process.env.NODE_ENV === "development") {
  globalForPrisma.db = db;
}
