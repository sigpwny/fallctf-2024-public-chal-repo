# Solution
Euler's phi function is multiplicative so that `phi(xy) = phi(x) * phi(y)`.
Then for a prime $p$, `phi(p) = p - 1`.
So if we can factor `n` then we can find `d = phi(n)`.

As $n$ has many relatively small prime factors, the easy way out is to do `ecm.factor(n)` in SageMath.
This uses the Elliptic Curve factoring method, which works particularly well when $n$ has many small factors.
Instead of SageMath, one could also use this [online tool](https://www.alpertron.com.ar/ECM.HTM).
ECM will grab all of $n$'s factors within reasonable time.
After that, multiply all the factors minus 1 together to get `phi_n`, and use this to find `d`.
