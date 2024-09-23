// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
import type { User } from "@prisma/client";

declare global {
  namespace App {
    // interface Error {}
    interface Locals {
      user: User;
    }
    // interface PageData {}
    // interface PageState {}
    // interface Platform {}
  }
}

export {};
