$$(q + a) \left(\frac {1}{q + a} y (k)\right) = y (k)$$

The calculations required for the proof are conveniently done using the backward-shift operator. It follows from the process model of (12.5) that

$$y (k + d) = \frac {B ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} u (k) + \frac {C ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} e (k + d)$$

We introduce

$$w (k) = \frac {B ^ {-} (q ^ {- 1})}{B ^ {- *} (q ^ {- 1})} y (k)$$

where the operator $1/B^{-*}(q^{-1})$ is interpreted as a noncausal stable operator. The signals y and w have the same steady-state variance because $B^{-}$ and $B^{-*}$ are reciprocal polynomials and

$$\left| \frac {B ^ {-} (e ^ {- i \omega})}{B ^ {- *} (e ^ {- i \omega})} \right| = 1$$

An admissible control law that minimizes the variance of w also minimizes the variance of y. It follows that

$$w (k + d) = \frac {B ^ {* *} (q ^ {- 1}) B ^ {-} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} u (k) + \frac {C ^ {*} (q ^ {- 1}) B ^ {-} (q ^ {- 1})}{A ^ {*} (q ^ {- 1}) B ^ {- *} (q ^ {- 1})} e (k + d) \tag {12.33}$$

The assumption that $A(z)$ and $B^{-}(z)$ are relatively prime guarantees that (12.32) has a solution. Equation (12.32) implies that

$$C ^ {*} (q ^ {- 1}) B ^ {-} (q ^ {- 1}) = A ^ {*} (q ^ {- 1}) F ^ {*} (q ^ {- 1}) + q ^ {- d} B ^ {- *} (q ^ {- 1}) G ^ {*} (q ^ {- 1})$$

Division by $A^{*}B^{-*}$ gives

$$\frac {C ^ {*} (q ^ {- 1}) B ^ {-} (q ^ {- 1})}{A ^ {*} (q ^ {- 1}) B ^ {- *} (q ^ {- 1})} = \frac {F ^ {*} (q ^ {- 1})}{B ^ {- *} (q ^ {- 1})} + q ^ {- d} \frac {G ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})}$$

By using this equation, (12.33) can be written as

$$w (k + d) = \frac {F ^ {*} (q ^ {- 1})}{B ^ {- *} (q ^ {- 1})} e (k + d) + \frac {B ^ {+ *} (q ^ {- 1}) B ^ {-} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} u (k) + \frac {G ^ {*} (q ^ {- 1})}{A ^ {*} (q ^ {- 1})} e (k) \tag {12.34}$$

Because the operator $1 / B^{-*}(q^{-1})$ is interpreted as a bounded noncausal operator and because $\deg F^{*} = d + \deg B^{-} - 1$ , it follows that

$$\frac {F ^ {*} (q ^ {- 1})}{B ^ {- *} (q ^ {- 1})} e (k + d) = \alpha_ {1} e (k + 1) + \alpha_ {2} e (k + 2) + \dots$$

These terms are all independent of the last two terms in (12.34). Using the arguments given in detail in the proof of Theorem 12.2, we find that the optimal control law is obtained by putting the sum of the last two terms in (12.34) equal to zero. This gives

$$u (k) = - \frac {G ^ {*} (q ^ {- 1})}{B ^ {+ *} (q ^ {- 1}) B ^ {-} (q ^ {- 1})} e (k) \tag {12.35}$$

and

$$y (k) = \frac {B ^ {- *} (q ^ {- 1})}{B (q ^ {- 1})} w (k) = \frac {F ^ {*} (q ^ {- 1})}{B ^ {-} (q ^ {- 1})} e (k) = \frac {F (q)}{q ^ {d - 1} B ^ {- *} (q)} e (k) \tag {12.36}$$

Elimination of $e(k)$ between (12.35) and (12.36) gives
