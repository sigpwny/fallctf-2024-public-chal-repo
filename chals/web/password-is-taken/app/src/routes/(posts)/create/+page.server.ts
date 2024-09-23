import { fail, redirect } from "@sveltejs/kit";
import type { Actions } from "./$types";
import { db } from "$lib/server/database";

export const actions = {
  default: async ({ locals, request }) => {
    const data = Object.fromEntries(await request.formData());

    const title = data.title as string;
    const content = data.content as string;

    if (title.length == 0) {
      return fail(400, {
        error: true,
        message: "<strong>Title</strong> can not be blank.",
      });
    }
    const post = await db.post.create({
      data: {
        title: title.trim(),
        content: content.trim(),
        authorId: locals.user.id,
      },
    });

    redirect(302, `/`);
  },
} satisfies Actions;
