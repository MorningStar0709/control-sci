# Example 3.11 A second-order system

Consider the following system, which is written in observable canonical form:

$$
x (k + 1) = \left( \begin{array}{l l} - a _ {1} & 1 \\ - a _ {2} & 0 \end{array} \right) x (k) + \binom{b _ {1}}{b _ {2}} u (k)

y (k) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x (k)
$$

The pulse-transfer operator is

$$
\begin{array}{l} H (q) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) \left( \begin{array}{c c} q + a _ {1} & - 1 \\ a _ {2} & q \end{array} \right) ^ {- 1} \binom{b _ {1}}{b _ {2}} \\ = \frac {1}{q ^ {2} + a _ {1} q + a _ {2}} \left( \begin{array}{l l} 1 & 0 \end{array} \right) \left( \begin{array}{c c} q & 1 \\ - a _ {2} & q + a _ {1} \end{array} \right) \binom{b _ {1}}{b _ {2}} \\ = \frac {b _ {1} q + b _ {2}}{q ^ {2} + a _ {1} q + a _ {2}} = \frac {b _ {1} q ^ {- 1} + b _ {2} q ^ {- 2}}{1 + a _ {1} q ^ {- 1} + a _ {2} q ^ {- 2}} \\ \end{array}
$$

Thus the $a_{i}$ 's and $b_{i}$ 's in the canonical form are defining the polynomials $A$ and $B$ , respectively. This is true for $n$ th-order systems also, in both observable and controllable form.
