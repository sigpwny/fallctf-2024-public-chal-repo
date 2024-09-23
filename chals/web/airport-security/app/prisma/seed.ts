import { PrismaClient } from "@prisma/client";
import * as crypto from "crypto";
import flightData from "./flight_data.json" assert { type: "json" };

const prisma = new PrismaClient();

async function addAdminUser() {
  const admin = await prisma.user.findUnique({
    where: {
      username: "admin",
    },
  });
  if (!admin) {
    await prisma.user.create({
      data: {
        username: "admin",
        password: crypto.randomBytes(12).toString("hex"),
        token: crypto.randomUUID(),
      },
    });
  }
}

async function addFlightData() {
  const row = await prisma.flight.findUnique({
    where: {
      flight_number: "FL124", // FL 124 is the flag flight
    },
  });
  if (!row) {
    const data = [
      ...flightData,
      {
        flight_number: "FL124",
        to: "the flag",
        from: "CIF 3039",
        details: process.env.FLAG ?? "fallctf{fake_flag}",
      },
    ];
    await prisma.flight.createMany({
      data: data,
    });
  }
}

async function main() {
  addAdminUser();
  addFlightData();
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
