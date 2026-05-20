Nyquist Stability Criterion Applied to Inverse Polar Plots. In the previous analyses, the Nyquist stability criterion was applied to polar plots of the open-loop transfer function $G ( s ) H ( s )$ .

In analyzing multiple-loop systems, the inverse transfer function may sometimes be used in order to permit graphical analysis; this avoids much of the numerical calculation. (The Nyquist stability criterion can be applied equally well to inverse polar plots. The mathematical derivation of the Nyquist stability criterion for inverse polar plots is the same as that for direct polar plots.)

The inverse polar plot of $G ( j \omega ) H ( j \omega )$ is a graph of $1 / \big [ G ( j \omega ) H ( j \omega ) \big ]$ as a function of v. For example, if $G ( j \omega ) H ( j \omega )$ is

$$G (j \omega) H (j \omega) = \frac {j \omega T}{1 + j \omega T}$$

then

$$\frac {1}{G (j \omega) H (j \omega)} = \frac {1}{j \omega T} + 1$$

The inverse polar plot for $\omega \geq 0$ is the lower half of the vertical line starting at the point (1, 0) on the real axis.

The Nyquist stability criterion applied to inverse plots may be stated as follows: For a closed-loop system to be stable, the encirclement, if any, of the $- 1 + j 0$ point by the $1 / \big [ G ( s ) H ( s ) \big ]$ locus (as s moves along the Nyquist path) must be counterclockwise, and the number of such encirclements must be equal to the number of poles of $1 / { \big [ } G ( s ) H ( s ) { \big ] }$ [that is, the zeros of $G ( s ) H ( s ) ]$ that lie in the right-half s plane. [The number of zeros of $G ( s ) H ( s )$ in the right-half s plane may be determined by the use of the Routh stability criterion.] If the open-loop transfer function $G ( s ) H ( s )$ has no zeros in the righthalf s plane, then for a closed-loop system to be stable, the number of encirclements of the $- 1 + j 0$ point by the $1 / \lbrack G ( s ) \rbrack { H ( s ) } \rbrack$ locus must be zero.

Note that although the Nyquist stability criterion can be applied to inverse polar plots, if experimental frequency-response data are incorporated, counting the number of encirclements of the $1 / \bar { [ } G ( s ) \dot { H } ( s ) \dot { ] }$ locus may be difficult because the phase shift corresponding to the infinite semicircular path in the s plane is difficult to measure. For example, if the open-loop transfer function $G ( s ) H ( s )$ involves transport lag such that

$$G (s) H (s) = \frac {K e ^ {- j \omega L}}{s (T s + 1)}$$
