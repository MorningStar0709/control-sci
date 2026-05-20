# Example 12.8 Cancellation of unstable process zero

Consider a system described by the polynomials

$$A (z) = (z - 1) (z - 0. 7)B (z) = 0. 9 z + 1C (z) = z (z - 0. 7)$$

The polynomial $B(z)$ has a zero z = -10/9, which is outside the unit disc. A simulation when using (12.27) is shown in Fig. 12.5. The presence of the unstable mode is clearly seen in the control signal, although it is not noticeable in the system output. If the simulation is continued, the control signal will finally be so large that overflow or numerical errors occur. In a practical problem the signal will quickly be so large that the linear approximation is no longer valid. After a short time the unstable mode will then be noticeable in the output.

The minimum-variance control law is extended to the case when the polynomial B has zeros outside the unit disc in Theorem 12.3.

THEOREM 12.3 MINIMUM-VARIANCE CONTROL—GENERAL CASE Consider a system described by (12.5). Factor the polynomial $B(z)$ as

$$B (z) = B ^ {+} (z) B ^ {-} (z) \tag {12.30}$$

where $B^{-*}(z)$ is monic. All zeros of the polynomial $B^{+}(z)$ are inside the unit disc and all zeros of $B^{-}(z)$ are outside the unit disc or on the unit circle. Assume that all the zeros of polynomial $C(z)$ are inside the unit disc and that the polynomials $A(z)$ and $B^{-}(z)$ do not have any common factors. The minimum-variance control law is then given by

$$u (k) = - \frac {G (q)}{B ^ {+} (q) F (q)} y (k) \tag {12.31}$$

where $F(q)$ and $C(q)$ are polynomials that satisfy the Diophantine equation

$$q ^ {d - 1} C (q) B ^ {- *} (q) = A (q) F (q) + B ^ {-} (q) G (q) \tag {12.32}$$

in which $\deg F = d + \deg B^{-} - 1$ and $\deg G < \deg A = n$ .

Proof. The proof is based on a clever trick introduced by Wiener in his original work on prediction. An alternative method is used in the proof of Theorem 12.4. Consider the operator

$$\frac {1}{q + a}$$

where $|a| > 1$ . This operator is normally interpreted as a causal unstable (unbounded) operator. Because $|a| > 1$ and the shift operator has the norm $\|q\| = 1$ , the series expansion

$$\frac {1}{q + a} = \frac {1}{a} \frac {1}{1 + q / a} = \frac {1}{a} \left(1 - \frac {q}{a} + \frac {q ^ {2}}{a ^ {2}} - \dots\right)$$

converges. Thus the operator $(q + a)^{-1}$ can be interpreted as a noncausal stable operator; that is,

$$\frac {1}{q + a} y (k) = \frac {1}{a} \left(y (k) - \frac {1}{a} y (k + 1) + \frac {1}{a ^ {2}} y (k + 2) - \dots\right)$$

With this interpretation, it follows that
