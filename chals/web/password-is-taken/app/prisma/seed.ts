import { User, PrismaClient } from "@prisma/client";
import * as crypto from "crypto";

const prisma = new PrismaClient();

async function addUser() {
  let user: User | null = await prisma.user.findUnique({
    where: {
      username: "admin",
    },
  });

  if (!user) {
    user = await prisma.user.create({
      data: {
        username: "admin",
        password: "password" + crypto.randomBytes(12).toString("hex"), // its random so it must be secure :)
        role: "admin",
        token: crypto.randomUUID(),
      },
    });
  }

  return user;
}

async function addFlagPost(user: User) {
  const flagPostTitle = "flag";
  let flagPost = await prisma.post.findFirst({
    where: {
      title: flagPostTitle,
    },
  });

  if (!flagPost) {
    flagPost = await prisma.post.create({
      data: {
        authorId: user.id,
        title: flagPostTitle,
        content: process.env.FLAG ?? "fallctf{fake_flag}",
      },
    });
  }

  return flagPost;
}

async function main() {
  const user = await addUser();
  const flagPost = await addFlagPost(user);
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
