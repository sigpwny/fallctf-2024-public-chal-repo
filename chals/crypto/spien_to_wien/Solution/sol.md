# Solution

To apply the Wiener method to approximate $d$ (which based on the chosen $n, e$ should be relatively small), we first need to find the continued fraction form of $\frac{e}{N}$

To understand how continued fractions and convergents work, let's say we have
$\langle N, e \rangle = \langle 90851, 17993\rangle$. 
Then
$$\frac{e}{N} = \frac{17993}{90851} = \frac{1}{5 + \frac{1}{29 + \dots + \frac{1}{3}}} = [0, 5, 29, 4, 1, 3, 4, 3]$$

From this continued fraction expansion (you can use WA, sage, or python to find it; refer to `continued_fracs.py`), we then find the convergents by computing every intermediate continued fraction.

So for our example, this would be

$$\frac{k}{d} = 0, \frac{1}{5}, \frac{29}{146}, \frac{117}{589}, \frac{146}{735}, \frac{555}{2794}, \frac{1256}{6323}, \frac{5579}{28086}, \frac{17993}{90581}$$

We can verify that the first convergent does not give us a factor of $n$.
However, the second one, $\frac{1}{5}$ gives:
$$\phi(N) = \frac{ed - 1}{k} = 89964$$

Now we just solve the quadratic equation:

$$x^2 - ((N - \phi(N))+1)x + N = 0$$

or 

$$x^2 - 618x + 90851 = 0$$

And finding the roots gives us $x = 379, 239$ which are our factors.
Thus, $N = 90851 = 379 \cdot 239 = pq$.

In general, this will work if 
$$d < \frac{N^{1/4}}{3}$$

Given the convergents, the general idea is to check if $k$ is nonzero and $ed - 1$ is divisible by $k$. Then check the quadratic from above and see if it has valid integer roots. If it does, return $d$ as the private exponent. The script below does that.

```py
def win(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if x^2 - s*x + n = 0 has integer roots
            D = s**2 - 4 * n
            if D >= 0:
                sq = math.isqrt(D)
                if sq * sq == D and (s + sq) % 2 == 0: return d
```
