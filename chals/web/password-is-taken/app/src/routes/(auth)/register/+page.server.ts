import { fail, redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";
import { db } from "$lib/server/database";

const positionOfFirstDifference = (pass1: string, pass2: string) => {
  if (pass1 == pass2) return pass1.length + 1;
  if (pass1.length < pass2.length) [pass1, pass2] = [pass2, pass1];
  return pass1.split("").findIndex((chr, i) => chr !== pass2[i]);
};

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

    const user = await db.user.findUnique({
      where: { username: username.trim() },
    });
    if (user) {
      return fail(400, {
        error: true,
        message: "<strong>Username</strong> already exists.",
      });
    }

    const collidedUser = await db.user.findUnique({
      where: {
        password: {
          startsWith: password,
        },
        username: "admin",
      },
    });
    if (collidedUser) {
      const diffIndex = positionOfFirstDifference(
        password,
        collidedUser.password
      );
      return fail(400, {
        error: true,
        message: `<strong>User ${
          collidedUser.username
        } already used partial password ${password.slice(
          0,
          diffIndex
        )}</strong>`,
      });
    }

    const newUser = await db.user.create({
      data: {
        username: username.trim(),
        password: password,
        token: crypto.randomUUID(),
        role: "user",
      },
    });

    cookies.set("session", String(newUser.token), {
      path: "/",
      httpOnly: true,
      sameSite: "strict",
      secure: process.env.NODE_ENV === "production",
      maxAge: 60 * 60 * 24 * 30,
    });

    redirect(302, "/");
  },
} satisfies Actions;
