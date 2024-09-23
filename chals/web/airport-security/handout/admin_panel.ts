import type { Actions, PageServerLoad } from "./$types";
import { db } from "$lib/server/database";
import { Prisma, type Flight } from "@prisma/client";
import { fail } from "@sveltejs/kit";

export const actions = {
  default: async ({ cookies, request }) => {
    const data = Object.fromEntries(await request.formData());

    const from_text = data.from_text as string;

    let flights: Flight[];
    try {
      flights = await db.$queryRaw<Flight[]>(
        Prisma.raw(
          `SELECT "flight_number", "to", "from" FROM "Flight" WHERE "from" LIKE '${from_text}%' ORDER BY "flight_number" ASC`
        )
      );
    } catch (e: any) {
      return fail(500, {
        error: true,
        message: e.message,
      });
    }

    return { error: false, message: flights };
  },
} satisfies Actions;
