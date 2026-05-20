$S(j\omega), T(j\omega)$ . Figure 6.7 illustrates the complex vectors $L(j\omega)$ and $1 + L(j\omega)$ . Since

$$S (j \omega) = \frac {1}{1 + L (j \omega)}$$

it follows that $|S(j\omega)| = S_0$ for all $L(j\omega)$ such that

$$\left| 1 + L (j \omega) \right| = 1 / S _ {0}. \tag {6.19}$$

That is, the locus of points in the $L(j\omega)$ plane corresponding to constant magnitude $S_0$ satisfies Equation 6.19. This locus is just a circle of radius $1 / S_0$ , centered at $(-1, 0)$ . Figure 6.8 shows constant- $|S|$ circles for $|S| = .5, 1$ , and 2. If, for example, $|S(j\omega)|$ is to be less than 1 at $\omega = \omega_0$ , then $L(j\omega_0)$ must be outside the circle corresponding to $|S| = 1$ .

The loci of constant $|T|$ are a bit more involved. Let $L(j\omega) = X + jY$ . Then

$$T = \frac {L}{1 + L} = \frac {X + j Y}{1 + X + j Y}$$

and

$$| T | ^ {2} = \frac {X ^ {2} + Y ^ {2}}{(1 + X) ^ {2} + Y ^ {2}}.$$

The locus of points $(X, Y)$ for which $|T| = M$ satisfies

$$M ^ {2} (1 + 2 X + X ^ {2}) + M ^ {2} Y ^ {2} = X ^ {2} + Y ^ {2}$$

or

$$(M ^ {2} - 1) Y ^ {2} + (M ^ {2} - 1) X ^ {2} + 2 M ^ {2} X + M ^ {2} = 0. \tag {6.20}$$

![](image/1712d80e8e8e95beab3ef7ed562ade895f171fbffaffd856d1ba13f7e2f04356.jpg)

<details>
<summary>contour</summary>

| Real Range | Imaginary Range | S₀ Value |
| --- | --- | --- |
| -3 to 1 | -2 to 2 | 0.5 |
| -3 to 1 | -2 to 2 | 1 |
| -3 to 1 | -2 to 2 | 2 |
</details>

Figure 6.8 Constant sensitivity circles

If $M = 1$ , then Equation 6.20 reduces to

$$X = - \frac {1}{2}. \tag {6.21}$$

That is, the vertical straight line $\operatorname{Re} L(j\omega) = -1/2$ is the locus of points where $|T(j\omega)| = 1$ .

If $M \neq 1$ ,

$$Y ^ {2} + X ^ {2} + 2 \frac {M ^ {2}}{M ^ {2} - 1} X + \frac {M ^ {4}}{(M ^ {2} - 1) ^ {2}} + \frac {M ^ {2}}{M ^ {2} - 1} = \frac {M ^ {4}}{(M ^ {2} - 1) ^ {2}}$$

or

$$Y ^ {2} + \left(X + \frac {M ^ {2}}{M ^ {2} - 1}\right) ^ {2} = \frac {M ^ {2}}{(M ^ {2} - 1) ^ {2}}. \tag {6.22}$$

Equation 6.22 represents a circle of radius $M / |M^2 - 1|$ , centered on the real axis ( $Y = 0$ ) at $X = -M^2 / (M^2 - 1)$ . Figure 6.9 shows several of the constant- $|T|$ circles, also called $M$ -circles. For example, if $|T(j\omega)|$ is required to be less than 2 at $\omega = \omega_0$ , then $L(j\omega_0)$ must lie outside the circle corresponding to $M = 2$ .
