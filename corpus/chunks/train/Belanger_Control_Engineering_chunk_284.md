# Example 5.18 (dc Servo)

In the dc servo model of Example 2.1 (Chapter 2), some parameters may vary, as follows: $0.04 \leq K_{m} \leq 0.06$ , $6 \times 10^{-4} \leq J_{m} \leq 10^{-3}$ , $0.01 \leq J \leq 0.05$ .

1. Write the Kharitonov polynomial, and give the range of k for which all four are stable.   
2. Calculate the true range of k for stability, under pure-gain feedback, of this family of plants.

Solution The transfer function is

$$P (s) = \frac {\theta}{v} = \frac {N K _ {m} / J _ {e} L}{s ^ {3} + (R / L) s ^ {2} + \left(\frac {N ^ {2} K _ {m} {} ^ {2}}{J _ {e} L}\right) s}.$$

With a control gain $k$ , the characteristic polynomial is

$$s ^ {3} + \frac {R}{L} s ^ {2} + \frac {N ^ {2} K _ {m} {} ^ {2}}{J _ {e} L} s + k \frac {N K _ {m}}{J _ {e} L}$$

and

$$\frac {R}{L} = 2 4, \quad 2 3. 7 5 \leq \frac {N ^ {2} K _ {m} {} ^ {2}}{J _ {e} L} \leq 1 0 7. 5, \quad 4 9. 4 8 \leq \frac {N K _ {m}}{J _ {e} L} \leq 1 4 9. 4.$$

The Kharitonov polynomials are

$$k _ {1} = 4 9. 4 8 k + 2 3. 7 5 s + 2 4 s ^ {2} + s ^ {3}k _ {2} = 1 4 9. 4 k + 1 0 7. 5 s + 2 4 s ^ {2} + s ^ {3}k _ {3} = 1 4 9. 4 k + 2 3. 7 5 s + 2 4 s ^ {2} + s ^ {3}k _ {4} = 4 9. 4 8 k + 1 0 7. 5 s + 2 4 s ^ {2} + s ^ {3}.$$

Let

$$k _ {i} = A _ {i} k + B _ {i} s + 2 4 s ^ {2} + s ^ {3}.$$

Applying the Routh criterion yields $0 < k < (24B_{i})/A_{i}$ for stability. The upper limit is 11.52 for $k_{1}$ , 17.26 for $k_{2}$ , 3.815 for $k_{3}$ , and 52.14 for $k_{4}$ . The result is therefore 0 < k < 3.815 as a sufficient condition for stability.

This result is conservative; $k_{3}$ is obtained with $a_{0}^{+}$ (maximum $K_{m}$ , minimum $J_{m}$ and J) and $a_{1}^{-}$ (minimum $K_{m}$ , maximum $J_{m}$ and J), which, of course, is impossible. Thus, $k_{3}$ is not a member of the set P.

To calculate the true range of k for stability, we observe that the Nyquist plot for the open-loop plant has a real-axis crossing at $\omega = \omega_{0}$ such that

$$I _ {m} \left[ - j \omega_ {0} ^ {3} - 2 4 \omega_ {0} ^ {2} + j \frac {N ^ {2} K _ {m} {} ^ {2}}{J _ {e} L} \omega_ {0} \right] = 0$$

or

$$\omega_ {0} = \frac {N K _ {m}}{\sqrt {J _ {e} L}}$$

and

$$P (j \omega_ {0}) = \frac {\frac {N K _ {m}}{J _ {e} L}}{\frac {- 2 4 N ^ {2} K _ {m} {} ^ {2}}{J _ {e} L}} = - \frac {1}{2 4 N K _ {m}}.$$

For stability, the number of encirclements must be zero, so

$$- \frac {1}{k} < - \frac {1}{2 4 N K _ {m}}$$

or

$$0 < k < 2 4 N K _ {m}.$$

To satisfy this under all conditions requires $k < 11.52$ . (Note that this result can also be obtained by applying the Routh criterion directly to the characteristic polynomial.)
