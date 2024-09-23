import { fail, redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";
import { db } from "$lib/server/database";

export const actions = {
  default: async ({ cookies, request }) => {
    const { username, password } = Object.fromEntries(
      await request.formData()
    ) as Record<string, string>;

    if (!username || !password) {
      return fail(400, {
        error: true,
        message:
          "<strong>Username</strong> and/or <strong>password</strong> can not be blank.",
      });
    }

    let user = await db.user.findUnique({
      where: { username: username.trim() },
    });

    if (!user) {
      return fail(400, {
        error: true,
        message: "User does not exist.",
      });
    } else {
      if (password !== user.password) {
        return fail(400, {
          error: true,
          message: "You have entered invalid credentials.",
        });
      }
    }

    cookies.set("session", String(user.token), {
      path: "/",
      httpOnly: true,
      sameSite: "strict",
      secure: process.env.NODE_ENV === "production",
      maxAge: 60 * 60 * 24 * 30,
    });

    redirect(302, "/");
  },
} satisfies Actions;
