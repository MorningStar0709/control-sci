# PROBLEMS

11.1 How should the disturbance annihilation filter $H_{f}(q)$ be chosen if $v(t)$ in Eq. (11.17) is a sinusoidal?

11.2 Consider the data filter

$$H _ {f} (q) = \frac {(1 - \alpha) (1 - q)}{q - \alpha}$$

Discuss how the choice of the parameter $\alpha$ influences elimination of constant disturbances.

11.3 Plot the Bode diagram for a fourth-order Bessel filter, and compare it with a pure time delay. Consider the cases in Table 11.2.

11.4 Determine how the behavior of the anti-reset windup controller of Eqs. (11.1) is influenced by the filter $A_{o}$ .

11.5 Complete the algorithm skeleton for the cases of

(a) a direct self-tuner (Algorithm 3.3).   
(b) an indirect self-tuner without zero cancellation (Algorithm 3.2).

11.6 Perform a transformation of a second- and fourth-order Bessel filter, $\omega_{B} = 1$ , into band-pass filters, using the transformation

$$s \rightarrow \frac {s ^ {2} + \omega_ {l} \omega_ {h}}{s (\omega_ {h} - \omega_ {l})}$$

where $\omega_{l}$ and $\omega_{h}$ are the lower and upper cutoff frequencies, respectively. Use $\omega_{l} = 100$ and $\omega_{h} = 1000$ rad/s. Compare the band-pass characteristics by using Bode diagrams.

11.7 Use Euclid's algorithm to compute the greatest common divisor of

$$A = q ^ {3} - 2 q ^ {2} + 1. 4 5 q - 0. 3 5B = q ^ {2} - 1. 1 q + 0. 3$$

Also determine the polynomials $X$ and $Y$ in Eq. (11.8).

11.8 Consider the Diophantine equation

$$A R + B S = A _ {c}$$

and let

$$A (q) = (q - 1) (q - 0. 9)$$

Use the method in Section 11.4, and compute the resulting controller when (a) $B(q) = q - 0.6$ ; (b) $B(q) = q - 0.9$ . Assume that the desired closed characteristic polynomial is

$$A _ {m} (q) = q ^ {2} - q + 0. 7$$

11.9 One way to solve the Diophantine equation is to multiply it by a persistently exciting signal, such as white noise. Introduce the filtered signals

$$v _ {a} (t) = \frac {\hat {A}}{A _ {m} A _ {o}} v (t) \quad v _ {b} (t) = \frac {\hat {B}}{A _ {m} A _ {o}} v (t)$$

The Diophantine equation then becomes

$$R v _ {a} + S v _ {b} = v$$

The coefficients of the R and S polynomials can now be determined by using the method of least squares, and one iteration can be done at each sampling instance. Discuss the merits and drawbacks of this approach. (Hint: What is the convergence rate?)
