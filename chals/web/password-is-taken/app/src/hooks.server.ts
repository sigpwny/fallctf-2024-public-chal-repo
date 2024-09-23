import type { Handle } from "@sveltejs/kit";
import { db } from "$lib/server/database";

const excludedPaths = ["/login", "/logout", "/register"]; // someone tell me the better way to do this

export const handle = (async ({ event, resolve }) => {
  if (excludedPaths.includes(event.url.pathname)) return await resolve(event);

  const user = await db.user.findUnique({
    where: {
      token: event.cookies.get("session") ?? "",
    },
  });
  if (!user) {
    return new Response("", {
      status: 303,
      headers: { location: "/login" },
    });
  }
  event.locals.user = user;

  return await resolve(event);
}) satisfies Handle;
