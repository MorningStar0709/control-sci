# Interpretation as Pole-Placement Design

The minimum-variance control law can be interpreted in terms of the poleplacement design discussed in Chapter 5. To see the relationships, the closed-loop system obtained when the control law of (12.27) is applied to the system of (12.5) is analyzed. Equations (12.5) and (12.27) can be written as

$$
\left( \begin{array}{c c} A (q) & - B (q) \\ G (q) & F (q) B (q) \end{array} \right) \binom {y (k)} {u (k)} = \binom {C (q)} {0} e (k) \tag {12.28}
$$

The characteristic polynomial of the closed-loop system is the determinant of the matrix on the left-hand side of (12.28). Hence,

$$A (q) F (q) B (q) + G (q) B (q) = q ^ {d - 1} B (q) C (q) \tag {12.29}$$

where Eq. (12.17), with $m = d$ , is used to obtain the first equality. The closed-loop system is of order $2n - 1$ . It has $2n - d$ poles at the zeros of $B$ and $C$ and an additional $d - 1$ poles at the origin.

The minimum-variance control strategy can be interpreted as a pole-placement design, where the poles are placed at the zeros given by (12.29). The similarities to pole placement are seen even more clearly if the control law of (12.27) is written as

$$u (k) = - \frac {G (q)}{B (q) F (q)} y (k) = - \frac {S (q)}{R (q)} y (k)$$

where $S = G$ and $R = FB$ [compare with Eq. (5.2)]. Multiplication of (12.17) by $B$ gives

$$q ^ {d - 1} C (q) B (q) = A (q) F (q) B (q) + G (q) B (q) = A (q) R (q) + B (q) S (q)$$

This equation is a special case of the Diophantine equation in (5.22) when $B^{+} = B$ and with $A_{c} = q^{d-1}B$ and $A_{o} = C$ .
