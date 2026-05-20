# Example 12.12 LQG for system with a time-delay

Consider the case

$$
\begin{array}{l} \boldsymbol {A} (z) = z \\ \boldsymbol {B} (z) = \boldsymbol {b} \\ C (z) = z + c \\ \end{array}
$$

The spectral factorization problem (12.45) has the solution

$$P (z) = z \quad r = \rho + b ^ {2}$$

Assuming that it is desired to have a controller with no extra delay we require that $\deg S(z) = \deg R(z) = 1$ . The Diophantine equation (12.47) with the constraint $\deg S^{*}(z) = 0$ becomes

$$z (z + r _ {1}) + b s _ {0} z = z (z + c)$$

Identification of coefficients of equal power of z gives only one equation

$$r _ {1} + b s _ {0} = c$$

to determine two parameters $r_{1}$ and $s_{0}$ . The approach with the Diophantine equation thus does not work in this case. Equation (12.49) gives

$$
\begin{array}{l} x _ {0} + r s _ {0} z = b (1 + c z) \\ b x _ {0} z - r z (1 + r _ {1} z) = - \rho z (1 + c z) \\ \end{array}
$$

Identification of coefficients of equal power of z gives linear equations which have the solution

$$
\begin{array}{l} x _ {0} = b \\ r _ {1} = \frac {\rho c}{r} = \frac {\rho c}{\rho + b ^ {2}} \\ s _ {0} = \frac {b c}{r} \\ \end{array}
$$
