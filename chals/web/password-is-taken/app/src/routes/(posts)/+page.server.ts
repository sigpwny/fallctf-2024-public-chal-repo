import type { PageServerLoad } from "./$types";
import { db } from "$lib/server/database";

export const load = (async ({ locals }) => {
  const posts = await db.post.findMany({
    orderBy: [{ id: "desc" }],
    where: {
      authorId: locals.user.id,
    },
  });

  return { posts };
}) satisfies PageServerLoad;
