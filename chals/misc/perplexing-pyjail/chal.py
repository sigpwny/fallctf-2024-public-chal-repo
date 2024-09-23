def protect_names(names):
    co_names = []
    banned_names = ["breakpoint", "exec", "eval"]

    for name in names:
        if name not in banned_names:
            co_names.append(name)

    return tuple(reversed(co_names) or [""])  # Did you know empty arrays are falsy?


source = input("Gimme some python code and I'll make it safe and run it: ")

bytecode = compile(source, "", "exec")
bytecode = bytecode.replace(co_names=protect_names(bytecode.co_names))

exec(bytecode)
