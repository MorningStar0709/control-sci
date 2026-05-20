# ALGORITHM 4.2 Generalized direct self-tuning algorithm

Data: Given the prediction horizon, d, the order of the controller, $\deg R^{*}$ and $\deg S^{*}$ , the stable observer polynomial, $A_{o}^{*}$ , and the stable polynomials $Q^{*}$ and $P^{*}$ , define the filtered signals

$$y _ {f} (t) = \frac {Q ^ {*}}{P ^ {*}} y (t) \quad y _ {f} ^ {\prime} (t) = \frac {1}{P ^ {*}} y (t)$$

Step 1: Estimate the coefficients of the polynomials $R^{*}$ and $S^{*}$ of the model

$$y _ {f} (t + d) = \frac {R ^ {*}}{A _ {o} ^ {*}} u (t) + \frac {S ^ {*}}{A _ {o} ^ {*}} y _ {f} ^ {\prime} (t) + \varepsilon (t + d) \tag {4.32}$$

using the least-squares method.

Step 2: Calculate the control signal from

$$u (t) = - \frac {S ^ {*}}{R ^ {*}} y _ {f} ^ {\prime} (t)$$

with $R^{*}$ and $S^{*}$ given by the estimates obtained in Step 1.

Repeat Steps 1 and 2 at each sampling period.

□

From Eq. (4.31) and Theorems 4.1 and 4.2 it follows that if the estimates converge, then the closed-loop system will be

$$y _ {f} (t) = R _ {1} ^ {*} e (t)$$

or

$$y (t) = \frac {P ^ {*} R _ {1} ^ {*}}{Q ^ {*}} e (t) \tag {4.33}$$

where $R_{1}^{*}$ is given by the identity

$$C ^ {*} Q ^ {*} = A ^ {*} P ^ {*} R _ {1} ^ {*} + q ^ {- d} B ^ {- *} S ^ {\prime} \tag {4.34}$$

and the control signal is given by

$$u (t) = - \frac {S ^ {*}}{R ^ {*}} y _ {f} ^ {\prime} (t) = - \frac {S ^ {*}}{R ^ {*} P ^ {*}} y (t) \tag {4.35}$$

where $R^{*} = B^{**}R_{1}^{*}$ . The closed-loop poles will thus be influenced by $Q^{*}$ , and additional zeros can be introduced through $P^{*}$ . The introduction of the filter $Q^{*}/P^{*}$ gives what is sometimes called a detuned minimum-variance algorithm.

Algorithm 4.2 is essentially the same as Algorithm 4.1 applied to filtered signals. The filter $Q^{*}/P^{*}$ and the prediction horizon will determine the pulse transfer operator of the closed-loop system. The optimal observer polynomial is $C^{*}$ , which is unknown. Instead, an approximation $A_{o}^{*}$ is used. The observer polynomial $A_{o}^{*}$ will determine the convergence properties. This will not influence the asymptotic properties as long as the filter $Q^{*}/P^{*}$ and its inverse are stable.
