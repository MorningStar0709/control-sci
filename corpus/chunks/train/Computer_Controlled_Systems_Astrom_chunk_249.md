# Example 4.9 Reduced-order observer for the double integrator

The observer (4.32) applied to the double integrator gives the equations

$$
\begin{array}{l} \hat {x} (k \mid k) = \left( \begin{array}{c c} 1 - k _ {1} & h (1 - k _ {1}) \\ - k _ {2} & 1 - h k _ {2} \end{array} \right) \hat {x} (k - 1 \mid k - 1) \\ + \binom{(1 - k _ {1}) h ^ {2} / 2}{h (1 - h k _ {2} / 2)} u (k - 1) + \binom{k _ {1}}{k _ {2}} y (k) \\ \end{array}
$$

If $I - CK = 0$ — that is, if $k_{1} = 1$ — then the first equation is reduced to

$$\hat {x} _ {1} (k \mid k) = y (k)$$

The reduced-order observer is now given by the second equation, which can be simplified to

$$
\begin{array}{l} \hat {x} _ {2} (k \mid k) = (1 - h k _ {2}) \hat {x} _ {2} (k - 1 \mid k - 1) \\ + k _ {2} (y (k) - y (k - 1)) + h (1 - h k _ {2} / 2) u (k - 1) \\ \end{array}
$$

By choosing $k_{2}$ , the reduced-order observer can be given an arbitrary eigenvalue. For instance, if $k_{2} = 1/h$ , the deadbeat response, then the same result is obtained as when making the direct calculation in Example 4.7.
