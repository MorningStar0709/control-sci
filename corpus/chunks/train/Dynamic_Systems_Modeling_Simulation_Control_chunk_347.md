$$y _ {H} (t) = c _ {1} e ^ {r _ {1} t} + c _ {2} t e ^ {r _ {1} t} + c _ {3} e ^ {r _ {3} t} + \dots + c _ {n} e ^ {r _ {n} t} \tag {7.8}$$

In either case, the n coefficients $c _ { i }$ are computed after the particular solution $y _ { P } ( t )$ is determined.

The particular solution $y _ { P } ( t )$ must satisfy the nonhomogeneous differential equation (7.2) and it can be found using the method of undetermined coefficients, where we assume a functional form for $y _ { P } ( t )$ that generally matches the forcing (or input) function $f ( t )$ and its derivatives. For example, if the forcing function $f ( t )$ is a constant, we can assume that the particular solution is also an undetermined constant. And, if the forcing function is $f ( t ) = \sin 4 t .$ , we can assume that the particular solution is $y _ { P } ( t ) = a \sin { 4 t } + b$ cos 4t, with unknown amplitude coefficients a and b. The assumed solution form for $y _ { P } ( t )$ is substituted into the original differential equation (7.2) and the unknown coefficients are determined by equating the corresponding terms. After the particular solution is found, the unknown coefficients $c _ { i }$ for the homogeneous solution in Eq. (7.7) are determined by applying the known initial conditions of the output $y ( t )$ and its derivatives at time $t = 0$ :

$$y (0) = y _ {0}, \dot {y} (0) = \dot {y} _ {0}, \ddot {y} (0) = \ddot {y} _ {0}, \dots , y ^ {(n - 1)} (0) = y _ {0} ^ {(n - 1)}$$

The following examples illustrate the general steps for solving low-order differential equations.
