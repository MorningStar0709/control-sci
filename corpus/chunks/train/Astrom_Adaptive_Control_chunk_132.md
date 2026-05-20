# EXAMPLE 2.19 Reparameterization

Consider the circuit in Fig. 2.14. The state space representation is

$$
\frac {d x}{d t} = \left( \begin{array}{c c} 0 & - 1 / C \\ 1 / L & - R / L \end{array} \right) x + \binom{1 / C}{0} u

y = \left( \begin{array}{c c} 0 & R \end{array} \right) x
$$

and the transfer function is

$$G (s) = \frac {\frac {R}{L C}}{s ^ {2} + \frac {R}{L} s + \frac {1}{L C}}$$

Let $\theta_{1} = R, \theta_{2} = 1 / L$ , and $\theta_{3} = 1 / C$ . Then

$$G (s) = \frac {\theta_ {1} \theta_ {2} \theta_ {3}}{s ^ {2} + \theta_ {1} \theta_ {2} s + \theta_ {2} \theta_ {3}}$$

The coefficients are nonlinear (although of special structure) in the physical parameters R, 1/L, and 1/C. The system can be written as

$$G (s) = \frac {k _ {1}}{s ^ {2} + k _ {2} s + k _ {3}} \tag {2.56}$$

and it is possible to make an estimation of $\theta_{1}$ , $\theta_{2}$ , and $\theta_{3}$ by using Eq. (2.56). However, the estimates must be constrained such that the relations

$$\boldsymbol {k} _ {1} = \theta_ {1} \theta_ {2} \theta_ {3}k _ {2} = \theta_ {1} \theta_ {2}k _ {3} = \theta_ {2} \theta_ {3}$$

are fulfilled.

![](image/b06426627f2494b4a6f75ec8254d306bb93d50d4f4d633c258669b96b7631862.jpg)

For indirect self-tuning regulators it is possible to estimate the continuous-time process parameters from discrete-time measurements. The model can then be sampled and the controller designed for the chosen sampling interval.
