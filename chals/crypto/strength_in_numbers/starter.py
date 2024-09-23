from Crypto.Util.number import long_to_bytes
from output import e, n, c

# TODO: find d
# Consider using SageMath!
#   https://github.com/cryptohack/cryptohack-docker
#   https://sagecell.sagemath.org/
#   https://cocalc.com/features/sage
# or other resources outside of just pure Python to attack this challenge
d = _

# Once you have d this code will give you the flag
m = pow(c, d, n)                    # m = c^d (mod n)
FLAG_bytes = long_to_bytes(m)       # turn number back into bytes
print(FLAG_bytes.decode("utf-8"))   # bytes -> string
