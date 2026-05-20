# ■ Theorem 4.2

The system of Figure 4.11 is internally stable if, and only if, the transfer functions $F(s)$ and $P(s)$ are stable.

Proof: For the two-input, two-output system of Figure 4.11,

$$y (s) = F P y _ {d} (s) + P v (s)z (s) = F y _ {d} (s)$$

or, in vector-matrix form,

$$
\left[ \begin{array}{l} y (s) \\ z (s) \end{array} \right] = \left[ \begin{array}{c c} F P & P \\ F & 0 \end{array} \right] \left[ \begin{array}{l} y _ {d} (s) \\ v (s) \end{array} \right]. \tag {4.18}
$$

Because the realization is controllable and observable, it is internally stable if, and only if, it is input-output stable, i.e., if all elements of the matrix transfer function of Equation 4.18 are stable. Thus, $P(s), F(s)$ , and $F(s)P(s)$ must have only LHP poles.

If $P(s)$ and $F(s)$ are stable transfer functions, so is $F(s)P(s)$ , because all poles of $FP$ are necessarily poles of either $F$ or $P$ . Therefore, if $P(s)$ and $F(s)$ are stable, the condition that $FP$ be stable is redundant, and the theorem is established.

Since the systems of Figures 4.10 and 4.11 differ only in the matter of inputs and outputs, they have identical internal stability properties. Therefore, Theorem 4.2 applies as well to the system of Figure 4.10 as to that of Figure 4.11.
