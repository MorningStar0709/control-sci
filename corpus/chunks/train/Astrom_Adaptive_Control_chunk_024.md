# EXAMPLE 1.3 Integrator with unknown sign

Consider a process whose dynamics is described by

$$G _ {0} (s) - \frac {k _ {p}}{s} \tag {1.2}$$

where the gain $k_{p}$ can assume both positive and negative values. This is a very severe variation because the phase of the system can change by $180^{\circ}$ . This process cannot be controlled by a linear controller with a rational transfer function. This can be seen as follows. Let the controller transfer function be $S(s)/R(s)$ , where $R(s)$ and $S(s)$ are polynomials. Assume that $\deg R \geq \deg S$ . The characteristic polynomial of the closed-loop system is then

$$P (s) = s R (s) + k _ {p} S (s)$$

Without lack of generality it can be assumed that the coefficient of the highest power of s in the polynomial $R(s)$ is 1. The coefficient of the highest power of s of $P(s)$ is thus also 1. The constant coefficient of polynomial $k_{p}S(s)$ is proportional to $k_{p}$ and can thus be either positive or negative. A necessary condition for $P(s)$ to have all roots in the left half-plane is that all coefficients are positive. Since $k_{p}$ can be both positive and negative, the polynomial $P(s)$ will always have a zero in the right half-plane for some value of $k_{p}$ .
