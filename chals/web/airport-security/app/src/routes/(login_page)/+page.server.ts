import { fail, redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";
import { db } from "$lib/server/database";
import { Prisma, type User } from "@prisma/client";

export const actions = {
  default: async ({ cookies, request }) => {
    const data = Object.fromEntries(await request.formData());

    const username = data.username as string;
    const password = data.password as string;

    if (!username || !password)
      return fail(400, {
        error: true,
        message:
          "<strong>Username</strong> and/or <strong>password</strong> cannot be blank",
      });

    if (username !== "admin")
      return fail(400, {
        error: true,
        message: "The only allowed user is: admin",
      });

    let admin: User;
    try {
      const response = await db.$queryRaw<User[]>(
        Prisma.raw(
          `SELECT * FROM "User" WHERE username = '${username}' AND password = '${password}'`
        )
      );
      admin = response?.[0];
    } catch (e: any) {
      console.log(e);
      return fail(500, {
        error: true,
        message: e.message,
      });
    }

    if (admin) {
      cookies.set("session", admin.token, {
        path: "/",
        httpOnly: true,
        sameSite: "strict",
        secure: process.env.NODE_ENV === "production",
        maxAge: 60 * 60 * 24 * 30,
      });
      redirect(302, "/admin_panel");
      return;
    }

    return fail(400, {
      error: true,
      message: "Incorrect username and/or password",
    });
  },
} satisfies Actions;
