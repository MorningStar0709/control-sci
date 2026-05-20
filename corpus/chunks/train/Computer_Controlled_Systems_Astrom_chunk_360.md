Now consider the system with delay. Determine a controller that gives a closed-loop system with the characteristic polynomial $z^{d}A(z)A'_{cl}(z)$ . The Diophantine equation for this problem is

$$A R + B S = z ^ {d} A A _ {c l} \tag {5.63}$$

The solution is such that $S = A\bar{S}$ . Hence

$$R + B \bar {S} = z ^ {d} A _ {c l} \tag {5.64}$$

Among the infinitely many solutions to this equation we choose

$$\bar {S} = S ^ {\prime} \tag {5.65}R = z ^ {d} A _ {c l} - \bar {S}$$

This solution is causal because $\deg S = \deg A + \deg A' - 1$ and $\deg R = d + 2\deg A' - 1 = \deg A + \deg A^+ - 1$ . Notice that

$$R = z ^ {d} A _ {c l} - \bar {S} = z ^ {d} A ^ {\prime} R ^ {\prime} + (z ^ {d} - 1) B S ^ {\prime} = A R ^ {\prime} + (z ^ {d} - 1) B S ^ {\prime}$$

Furthermore $T = AT'$ . The controller

$$R u = T u _ {c} - S y$$

then becomes

$$\left(A R ^ {\prime} + (z ^ {d} - 1) B S ^ {\prime}\right) u = A T ^ {\prime} u _ {c} - A S ^ {\prime} y$$

This control law can be written as

$$u = \frac {T ^ {\prime}}{R ^ {\prime}} u _ {c} - \frac {S ^ {\prime}}{R ^ {\prime}} \left(y - z ^ {d} \frac {B}{A} u\right) = \frac {T ^ {\prime}}{R ^ {\prime}} u _ {c} - \frac {S ^ {\prime}}{R ^ {\prime}} \left(y - \left(1 - z ^ {- d} \frac {B}{A ^ {\prime}} u\right)\right) \tag {5.66}$$

A comparison with Fig. 5.29 shows that the controller is the discrete-time equivalent of the Smith-predictor in the figure. Notice that we can immediately conclude that the Smith-predictor is based on cancellation of all process poles. Thus it can only be applied to stable processes. It is, however, easy to modify the procedure to give a stable closed-loop system simply by replacing A on the right-hand side in Eq. (5.63) with a stable polynomial.
