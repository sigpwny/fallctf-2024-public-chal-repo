# Solution

Given Alice's x coordinate, it isn't too difficult to extract the $y$ coordinate, as we know it must be on the defined Elliptic curve. Without sage, you can do this by calculating
$$y^2 = x^3 + ax + b$$ 
directly, and then doing a modular square root operation. This is done using the mod_sqrt function, which checks if $y^2$ is a quadratic residue mod $p$ (easy as $p$ is $3 \mod 4$),
and if so, does 
$$\left(y^2\right)^{\frac{p+1}{4}} \mod p$$

This should give one of the two possible points that could be the secret.

If you do use sage, the challenge becomes much easier. All you need to do is define the Elliptic curve object `E` using the params given and then call `E.lift_x(Q_a_x)` to find Alice's 2 possible $y$ coords, either from which you can find either shared secret through calculating the points on the curve corresponding to $S = [n_B]Q_a$

Either point works, as the x-coordinate is all you need.