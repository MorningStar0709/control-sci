# Solution

We form the matrix

$$
H (\mu) = \left[ \begin{array}{c c} A & \mu B B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 2 \mu & - \mu \\ - 2 & - 3 & - \mu & \mu \\ - 1 & 0 & 0 & 2 \\ 0 & - 1 & - 1 & 3 \end{array} \right]
$$

where $\mu = \gamma^{-2}$ has been used. The characteristic polynomial of $H$ is

$$\det (s I - H) = s ^ {4} + s ^ {2} (3 \mu - 5) + \mu^ {2} - 2 1 \mu + 4.$$

Note that only even powers of $s$ are present. This leads to roots that are symmetrically located with respect to both the real and the imaginary axes.

For $\mu = 0(\gamma = \infty)$ , the characteristic polynomial is

$$s ^ {4} - 5 s ^ {2} + 4$$

with roots $s^{2}=+4,+1$ , and thus $s=\pm2,\pm1$ . Indeed, with $\mu=0,H$ is block triangular and its eigenvalues are those of A and $-A^{T}$ , i.e., of A and -A; those are -1,-2,+1, and +2.

Now, $H$ has imaginary-axis eigenvalues when $s^{*^2} < 0$ , where $s^*$ is a root of the characteristic polynomial. For $\mu = 0$ , $s^{*^2}$ has the values 1 and 4; as $\mu$ increases, $s^{*^2}$ crosses zero to become negative. We have $s^{*^2} = 0$ for

$$\mu^ {2} - 2 1 \mu + 4 = 0$$

or

$$\mu = \frac {2 1 \pm \sqrt {4 2 5}}{2}.$$

We take the smaller of the two values, corresponding to the largest value of $\gamma$ that results in imaginary-axis eigenvalues. Thus, $\mu = 0.1922$ and $\|G\|_{\infty} = \gamma = 1/\sqrt{\mu} = 2.281$ .
