import { dlopen, FFIType, ptr } from "bun:ffi";

export function cstr(str: string) {
  return ptr(new TextEncoder().encode(str + "\0"));
}

const {
  symbols: { printf, gets, atoi },
} = dlopen("libc.so.6", {
  printf: {
    args: ["cstring", "cstring"],
    returns: "void",
  },
  gets: {
    args: ["pointer"],
    returns: "void",
  },
  atoi: {
    args: ["cstring"],
    returns: FFIType.u64_fast,
  },
});

export { printf, gets, atoi };
