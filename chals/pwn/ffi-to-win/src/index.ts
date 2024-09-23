import { gets, printf, atoi, cstr } from "./lib.ts";
import { ptr } from "bun:ffi";
import type { Pointer } from "bun:ffi";

const flag = cstr(process.env.FLAG ?? "fallctf{fake_flag}");
console.log(flag); // i wanted to hack the system but all i got was a bunch of random numbers instead of the flag what gives?

const name = Buffer.alloc(20);
const address = Buffer.alloc(20);

printf(cstr("What is your name? "));
gets(ptr(name));
printf(cstr("What's the magic number? "));
gets(ptr(address));

printf(name, atoi(address) as Pointer);
